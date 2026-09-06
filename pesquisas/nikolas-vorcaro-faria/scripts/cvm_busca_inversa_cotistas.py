"""Busca inversa nas bases CDA da CVM: quais fundos declaram cotas de um CNPJ alvo, e o que o alvo declara ter.
Uso: python3 cvm_busca_inversa_cotistas.py 202503 10.566.011/0001-97 [outro_cnpj ...]
Baixa https://dados.cvm.gov.br/dados/FI/DOC/CDA/DADOS/cda_fi_<AAAAMM>.zip (~20 MB) se nao existir.
"""
import sys,os,glob,zipfile,urllib.request
m=sys.argv[1]; targets=sys.argv[2:]
z=f"cda_fi_{m}.zip"
if not os.path.exists(z): urllib.request.urlretrieve(f"https://dados.cvm.gov.br/dados/FI/DOC/CDA/DADOS/{z}",z)
if not os.path.isdir(m): zipfile.ZipFile(z).extractall(m)
for f in sorted(glob.glob(f"{m}/cda_fi_*_{m}.csv")):
    with open(f,'rb') as fh:
        hdr=fh.readline().decode('latin1').strip().split(';')
        for line in fh:
            s=line.decode('latin1')
            for t in targets:
                if t in s:
                    d=dict(zip(hdr,s.strip().split(';')))
                    papel="COTISTA (declara cotas do alvo)" if d.get('CNPJ_FUNDO_CLASSE_COTA')==t else ("CARTEIRA do alvo" if d.get('CNPJ_FUNDO_CLASSE')==t else "mencao")
                    print(papel,"|",f.split('/')[-1],"|",d.get('CNPJ_FUNDO_CLASSE'),(d.get('DENOM_SOCIAL') or '')[:60],"|",d.get('TP_APLIC'),"|",(d.get('NM_FUNDO_CLASSE_COTA') or d.get('DS_ATIVO') or d.get('EMISSOR') or '')[:50],"|",d.get('VL_MERC_POS_FINAL'))
