"""Synchronize reviewed notes and audit local links/assets; never generate note prose."""
from pathlib import Path
from urllib.parse import unquote
import json,re,hashlib,sys,os
import yaml
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
DATE='2026-10-05'
ORIG=OUT/'originals/reading_notes'
REWRITTEN={p.stem for p in ORIG.glob('*.md') if not re.search(r'!\[|<img\b',p.read_text())}
assert len(REWRITTEN)==23

def image_links(s):
    return [(m[1],m[2]) if m[2] else ('',m[3]) for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)|<img[^>]+src=[\"\']([^\"\']+)',s)]

def resolve_note_link(p,v):
    return (p.parent/unquote(v.split(' "')[0].strip('<>').split('#')[0])).resolve()

# Normalize the source-coordinate formats used by the independent reading groups.
def provenance(asset_dir):
    records={}
    for name in ['figure_provenance.json','source_map_figures.json','reading_note_figure_sources.json','figure_sources.json']:
        p=asset_dir/name
        if not p.exists():continue
        blob=json.loads(p.read_text());rows=blob.get('figures',[]) if isinstance(blob,dict) else blob
        for x in rows:
            filename=x.get('file') or x.get('asset')
            if not filename:continue
            image_path=(ROOT/filename if filename.startswith('assets/') else asset_dir/filename).resolve()
            records[str(image_path)]={
                'page':x.get('pdf_page',x.get('page')),
                'crop_bbox':x.get('bbox_pt',x.get('rect',x.get('crop_box_points',x.get('source_crop_box',[])))),
                'number':str(x.get('figure',x.get('figure_number',''))),
                'provenance_path':str(p.relative_to(ROOT))}
    return records

records=[json.loads(x) for x in (ROOT/'metadata/papers.jsonl').read_text().splitlines() if x.strip()]
by_id={x['id']:x for x in records}
audit=[];errors=[]
for p in sorted((ROOT/'reading_notes').glob('*.md')):
    s=p.read_text();parts=s.split('---',2)
    try:front=yaml.safe_load(parts[1]);assert isinstance(front,dict)
    except Exception as e:errors.append({'note':p.name,'yaml_error':str(e)});continue
    body=parts[2];pid=front.get('id');assert pid==p.stem
    links=image_links(body);asset_dir=ROOT/'assets'/pid;prov=provenance(asset_dir) if pid in REWRITTEN else {}
    image_rows=[]
    for caption,v in links:
        if re.match(r'https?://|data:',v):
            errors.append({'note':p.name,'external_image':v});continue
        q=resolve_note_link(p,v)
        if not q.is_file():errors.append({'note':p.name,'broken_image':v});continue
        try:
            with Image.open(q) as im:width,height=im.size;im.verify()
        except Exception as e:errors.append({'note':p.name,'image_decode':v,'error':str(e)});continue
        row={'path':str(q.relative_to(ROOT)),'caption':caption,'width':width,'height':height}
        row.update(prov.get(str(q),{}));image_rows.append(row)
    if not links:errors.append({'note':p.name,'no_embedded_images':True})
    source_paths=[]
    for key in ['source_path','source_archive_path']:
        v=front.get(key)
        if v:
            q=resolve_note_link(p,v)
            if not q.exists():errors.append({'note':p.name,'broken_source':v})
            source_paths.append(str(q.relative_to(ROOT)))
    heads=re.findall(r'^#{2,6}\s+(.+)$',body,re.M)
    sections=[h for h in heads if re.match(r'^\d+(?:\.\d+)*\s',h)]
    if pid in REWRITTEN:
        rec=by_id[pid];existing={str((ROOT/f['path']).resolve()):f for f in rec.get('figures',[]) if f.get('path')}
        new_figs=list(rec.get('figures',[]))
        for row in image_rows:
            key=str((ROOT/row['path']).resolve())
            if key in existing:continue
            assert row.get('page') is not None,(pid,row)
            new_figs.append({'id':Path(row['path']).stem,'kind':'figure','path':row['path'],
              'caption':row['caption'],'page':row['page'],'crop_bbox':row.get('crop_bbox',[]),
              'number':row.get('number',''),'source':'pdf-crop',
              'source_ref':rec.get('source_path',''),'provenance_path':row.get('provenance_path','')})
        rec['figures']=new_figs;rec['sections']=sections;rec['status']='read';rec['updated_at']=DATE
        rec['paper_type']=front.get('paper_type',rec.get('paper_type'))
    level='source_grounded_full_body_rewrite' if pid in REWRITTEN else 'existing_body_structure_and_asset_check'
    if pid.startswith('2026_evoking-user-memory'):
        level='existing_body_plus_missing_related_work_completed'
        by_id[pid]['updated_at']=DATE
    audit.append({'id':pid,'title':front.get('title',pid),'note':str(p.relative_to(ROOT)),
        'review_level':level,'body_characters':len(body.strip()),'embedded_images':len(links),
        'unique_images':len(set(x['path'] for x in image_rows)),'images':image_rows,
        'source_paths':source_paths,'numbered_sections':sections,
        'note_sha256':hashlib.sha256(s.encode()).hexdigest(),'status':front.get('status')})
if errors:
    (OUT/'final_integrity_errors.json').write_text(json.dumps(errors,ensure_ascii=False,indent=2))
    raise SystemExit(json.dumps(errors,ensure_ascii=False))
# Re-read before mutation: retain concurrent changes to unrelated papers and fields.
latest=[json.loads(x) for x in (ROOT/'metadata/papers.jsonl').read_text().splitlines() if x.strip()]
for item in latest:
    pid=item['id']
    if pid in REWRITTEN:
        for key in ['figures','sections','status','updated_at','paper_type']:item[key]=by_id[pid][key]
    elif pid.startswith('2026_evoking-user-memory'):item['updated_at']=DATE
meta=ROOT/'metadata/papers.jsonl';temp=meta.with_suffix('.jsonl.repair-tmp')
temp.write_text(''.join(json.dumps(x,ensure_ascii=False,sort_keys=True)+'\n' for x in latest));os.replace(temp,meta)
result={'started':'2026-10-04','completed':DATE,'notes_checked':len(audit),'notes_rewritten':len(REWRITTEN),
 'rewritten_inline_images':sum(x['embedded_images'] for x in audit if x['id'] in REWRITTEN),
 'all_inline_images':sum(x['embedded_images'] for x in audit),'integrity_errors':errors,'notes':audit}
(OUT/'final_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='notes'},ensure_ascii=False))
