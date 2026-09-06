import json,matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Ellipse
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
def draw(ax,gj,fc,ec,lw,z=1):
    for f in gj['features']:
        g=f['geometry']; polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
        for poly in polys: ax.add_patch(Polygon(poly[0],closed=True,facecolor=fc,edgecolor=ec,lw=lw,zorder=z))
mg=json.load(open('mg.json')); mun=json.load(open('mg_mun.json')); fV=mpimg.imread('vorcaro_circle.png'); fN=mpimg.imread('nikolas_circle.png')
V="#7a1f14"; TP="#2f5d7c"; ORG="#b0730a"; KAL="#5b3f8c"
fig=plt.figure(figsize=(15,11),dpi=150); fig.patch.set_facecolor("#faf6f0")
ax=fig.add_axes([0.02,0.07,0.96,0.85]); ax.set_facecolor("#faf6f0"); draw(ax,mun,"#f8f4ee","#e3dccf",0.5,1)
xmin,xmax,ymin,ymax=-44.55,-42.90,-20.92,-19.40
qf=[(-44.05,-19.85),(-43.70,-19.55),(-43.20,-19.55),(-43.05,-20.05),(-43.35,-20.55),(-43.90,-20.55),(-44.15,-20.30)]
ax.add_patch(Polygon(qf,closed=True,facecolor="#c98a4b",edgecolor="none",alpha=0.08,zorder=2))
ax.text(-43.25,-19.98,"QUADRILÁTERO FERRÍFERO",fontsize=11,fontweight="bold",color="#8a5a25",ha="center",zorder=6,alpha=0.5)
def blob(lo,la,w,h,color,alpha=0.22): ax.add_patch(Ellipse((lo,la),w,h,facecolor=color,edgecolor="none",alpha=alpha,zorder=3))
def lab(text,xy,xyt,color="#222",fs=8.5,bold=False,ha="left",lw=0.8):
    ax.annotate(text,xy=xy,xytext=xyt,fontsize=fs,color=color,fontweight="bold" if bold else "normal",ha=ha,va="center",zorder=10,arrowprops=dict(arrowstyle="-",color=color,lw=lw,shrinkA=0,shrinkB=3),bbox=dict(boxstyle="round,pad=0.25",fc="#faf6f0",ec="none",alpha=0.9))
NV="#d0342c"; NN="#e07b00"
def lab2(name,body,xy,xyt,ncol,bcol,fs=10.5,lw=1.4,target=None):
    # arrow from xy to target (or to text)
    tx,ty=xyt
    ax.annotate("",xy=xy,xytext=(target if target else (tx,ty)),zorder=9,arrowprops=dict(arrowstyle="-",color=bcol,lw=lw,shrinkA=0,shrinkB=3))
    ax.text(tx,ty+0.028,name,fontsize=fs+1,fontweight="bold",color=ncol,ha="left",va="bottom",zorder=10,bbox=dict(boxstyle="round,pad=0.2",fc="#faf6f0",ec="none",alpha=0.9))
    ax.text(tx,ty+0.02,body,fontsize=fs,fontweight="bold",color=bcol,ha="left",va="top",zorder=10,bbox=dict(boxstyle="round,pad=0.2",fc="#faf6f0",ec="none",alpha=0.9))
def foto(img,lo,la,zoom=0.24): ax.add_artist(AnnotationBbox(OffsetImage(img,zoom=zoom),(lo,la),frameon=False,zorder=12))
C={"Belo Horizonte":((-43.94,-19.92),(-44.20,-19.62),True),"Nova Lima":((-43.85,-19.99),(-44.05,-19.76),False),"Sarzedo":((-44.14,-20.04),(-44.48,-20.22),False),"Ouro Preto":((-43.50,-20.39),(-43.08,-20.30),True)}
for n,(p,t,big) in C.items(): ax.plot(p[0],p[1],"o",ms=7 if big else 4.5,color="#444",zorder=8); lab(n,p,t,color="#444",fs=10.5 if big else 9,bold=big)
D={"Rodrigo Silva":((-43.65,-20.42),(-43.72,-20.24)),"Botafogo":((-43.59,-20.37),(-43.48,-20.19))}
for n,(p,t) in D.items(): ax.plot(p[0],p[1],"o",ms=4,color="#555",zorder=8); lab(n,p,t,color="#555",fs=8.5)
ax.plot(-43.70,-20.43,"^",ms=8,color="#9a9a9a",zorder=7); lab("Gerdau: Miguel Burnier\n476 milhões de t, a 1,3 km",(-43.70,-20.43),(-43.93,-20.60),color="#777",fs=7.8,lw=0.6)
blob(-43.63,-20.42,0.11,0.085,TP,0.25); ax.plot(-43.63,-20.42,"*",ms=36,color="#1f6fb2",mec="white",mew=1.2,zorder=9)
foto(fN,-43.52,-20.79,zoom=0.26); lab2("NIKOLAS FERREIRA","TOPÁZIO IMPERIAL, a lavra do áudio\nferro, manganês e topázio. Embargada",(-43.63,-20.42),(-43.41,-20.79),NN,TP,fs=11.5,lw=1.4,target=(-43.52,-20.75))
for lo,la in [(-43.715,-20.394),(-43.52,-20.445)]: ax.plot(lo,la,"s",ms=14,color="#b8261a",mec="white",mew=0.8,zorder=8)
blob(-43.715,-20.394,0.09,0.065,V,0.22); blob(-43.52,-20.445,0.09,0.065,V,0.22)
foto(fV,-44.47,-20.70); lab2("DANIEL VORCARO","3D MINERALS: Vorcaro emprestou R$ 152,9 milhões\ne ficou com metade das cotas em garantia\nferro, a 4,5 km da Topázio",(-43.715,-20.394),(-44.36,-20.70),NV,V,fs=10,target=(-44.47,-20.66))
foto(fV,-43.27,-20.56); lab2("DANIEL VORCARO","3D MINERALS: Vorcaro emprestou R$ 152,9 milhões\ne ficou com metade das cotas em garantia\nferro, a 7 km da Topázio",(-43.52,-20.445),(-43.16,-20.56),NV,V,fs=10,target=(-43.27,-20.52))
blob(-43.90,-19.98,0.10,0.075,V,0.2); ax.plot(-43.90,-19.98,"D",ms=18,color="#b8261a",mec="white",mew=1.2,zorder=9)
foto(fV,-43.69,-19.50); lab2("DANIEL VORCARO","TAMISA: controlada por fundo do Master (93%)\nSerra do Curral, ao lado das minas de Lages\n(Fleurs e Gute) e da Empabra (Kallas)",(-43.90,-19.98),(-43.58,-19.50),NV,V,fs=10,target=(-43.69,-19.54))
blob(-44.12,-20.05,0.10,0.075,V,0.2); ax.plot(-44.12,-20.05,"D",ms=18,color="#b8261a",mec="white",mew=1.2,zorder=9)
foto(fV,-44.48,-19.86); lab2("DANIEL VORCARO","ITAMINAS: Vorcaro comprou metade\nem 2024, com AVG e Ageo",(-44.12,-20.05),(-44.38,-19.86),NV,V,fs=10,target=(-44.48,-19.90))
blob(-43.585,-20.375,0.09,0.065,ORG,0.25); ax.plot(-43.595,-20.38,"P",ms=13,color=ORG,mec="white",mew=1,zorder=9); ax.plot(-43.5827,-20.3729,"P",ms=13,color=ORG,mec="white",mew=1,zorder=9)
lab("PATRIMÔNIO MINERAÇÃO e HG MINERAÇÃO\nmineradoras do grupo de João Alberto Lages\n(Operação Rejeito), Serra do Botafogo, a 5 e 7 km\nlicença comprada com R$ 500 mil de propina\nem fevereiro de 2025, segundo a PF",(-43.585,-20.375),(-43.32,-20.10),color=ORG,fs=10.5,bold=True,lw=1.4)
blob(-43.6899,-20.4662,0.09,0.065,KAL,0.25); ax.plot(-43.6899,-20.4662,"h",ms=14,color=KAL,mec="white",mew=1,zorder=9)
foto(fV,-44.47,-20.34,zoom=0.17); lab2("LUCAS KALLAS, sócio de VORCARO","EMPABRA, de Kallas (sócio de Vorcaro na Biomm)\nbauxita, a 8 km da Topázio",(-43.6899,-20.4662),(-44.38,-20.34),NV,KAL,fs=10,target=(-44.47,-20.31))
ax.plot([],[],"s",color=V,ms=9,label="3D Minerals: financiada pelo Master"); ax.plot([],[],"D",color=V,ms=9,label="Controladas ou compradas por Vorcaro"); ax.plot([],[],"P",color=ORG,ms=10,label="Grupo de Lages (Operação Rejeito)"); ax.plot([],[],"h",color=KAL,ms=10,label="Empabra (Kallas)"); ax.plot([],[],"*",ms=16,color=TP,label="Lavra da Topázio (Nikolas e Faria)")
ax.set_xlim(xmin,xmax); ax.set_ylim(ymin,ymax); ax.set_aspect(1/0.94); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_edgecolor("#b0b0b0")
ax.legend(loc="upper right",bbox_to_anchor=(0.995,0.80),fontsize=8.5,frameon=True,facecolor="#faf6f0",edgecolor="#b0b0b0")
ax.plot([-43.10,-43.10+20/104],[-20.40,-20.40],color="#222",lw=3); ax.text(-43.10+10/104,-20.385,"20 km",ha="center",fontsize=8)
ins=fig.add_axes([0.035,0.68,0.19,0.24]); ins.set_facecolor("#faf6f0"); draw(ins,mg,"#f3ece1","#6b4226",1.0,1)
ins.add_patch(Rectangle((xmin,ymin),xmax-xmin,ymax-ymin,fill=False,edgecolor=TP,lw=2)); ins.plot(-43.63,-20.42,"*",ms=9,color=TP); ins.plot(-43.94,-19.92,"o",ms=3,color="#222"); ins.text(-43.7,-19.55,"BH",fontsize=7)
ins.set_xlim(-51.2,-39.7); ins.set_ylim(-23,-14.1); ins.set_aspect(1/0.94); ins.axis("off"); ins.set_title("Minas Gerais",fontsize=8,color="#3b2213")
fig.suptitle("A lavra do áudio de Nikolas e quem estava ao redor dela em 2025: o dinheiro de Vorcaro, o grupo de Lages e o sócio de Vorcaro",fontsize=13,color="#3b2213",x=0.02,ha="left",y=0.965)
fig.text(0.015,0.030,"Fontes: IBGE, ANM/SIGMINE (05/09/2026), CVM, Folha, AVG, PF via Agência Primaz e O Fator. Patrimônio Mineração em posição aproximada (Serra do Botafogo). Crédito da 3D cedido ao BRB em jul/2025.",fontsize=7,color="#555")
fig.text(0.015,0.012,"Fotos: Vorcaro por Márcio G. Vasconcelos (2024, CC0); Nikolas por Kayo Magalhães/Câmara dos Deputados (2025, CC BY 3.0). Elaboração: O Cafezinho",fontsize=7,color="#555")
fig.text(0.985,0.012,"ocafezinho.com",fontsize=9,color="#6b4226",ha="right",fontweight="bold")
fig.savefig("mapa-quadrilatero-lavra-minas-master.png",facecolor=fig.get_facecolor()); print("ok")
