"""Extrai do shapefile SIGMINE (ANM, dados abertos) os processos minerarios de um titular.
Uso: baixe https://dadosabertos.anm.gov.br/SIGMINE/PROCESSOS_MINERARIOS/MG.zip, descompacte e rode.
Requer: pip install pyshp
"""
import shapefile, csv, sys
TERMO = sys.argv[1].upper() if len(sys.argv) > 1 else "TOPAZIO IMPERIAL"
sf = shapefile.Reader("MG", encoding="utf-8")
fields = [f[0] for f in sf.fields[1:]]
rows = []
for sr in sf.iterShapeRecords():
    d = dict(zip(fields, sr.record))
    if TERMO in str(d["NOME"]).upper():
        pts = sr.shape.points
        d["lon"] = round(sum(p[0] for p in pts) / len(pts), 4)
        d["lat"] = round(sum(p[1] for p in pts) / len(pts), 4)
        rows.append(d)
with open("titulos_extraidos.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for d in rows:
    print(d["PROCESSO"], d["SUBS"], d["FASE"], d["AREA_HA"], "ha", d["lat"], d["lon"], "|", d["ULT_EVENTO"])
