"""Le a remuneracao mensal de um secretario parlamentar no Portal da Transparencia da Camara.
Uso: python3 folha_camara_secretario.py <id_da_ficha> <ano_ini> <ano_fim>
O id vem do link 'Consultar' em https://www.camara.leg.br/deputados/<id_dep>/pessoal-gabinete
"""
import requests, re, html, sys
fid, a0, a1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
H = {"User-Agent": "Mozilla/5.0"}
f = lambda s: float(s.replace(".", "").replace(",", "."))
for y in range(a0, a1 + 1):
    for m in range(1, 13):
        t = requests.get(f"https://www.camara.leg.br/transparencia/recursos-humanos/remuneracao/{fid}?ano={y}&mes={m}", headers=H, timeout=60).text
        t = re.sub(r"<[^>]+>", " ", t); t = re.sub(r"\s+", " ", html.unescape(t))
        g = re.search(r"Função/cargo em comissão: (SP\d+).*?Função ou Cargo em Comissão ([\d\.,]+).*?Gratificação Natalina ([\d\.,]+).*?Férias \(1/3 Constitucional\) ([\d\.,]+).*?Auxílios ([\d\.,]+)", t)
        print(y, m, (g.group(1), f(g.group(2)), f(g.group(3)), f(g.group(4)), f(g.group(5))) if g else "sem folha")
