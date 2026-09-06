# Pesquisa: Nikolas Ferreira, Vorcaro e o contrato minerário de Thiago Rodrigues de Faria

Material de apuração do jornal O Cafezinho (ocafezinho.com), reunido em 05/09/2026. Fase de pesquisa em andamento. Nenhum dado desta pasta foi publicado ainda, exceto o que consta no artigo da parte 1.

## Consolidação atual para Miguel e Claude

Depois das regras editoriais abaixo, comece por [00-CONSOLIDACAO-MESTRA-2026-09-06.md](00-CONSOLIDACAO-MESTRA-2026-09-06.md). Esse documento reúne o núcleo Faria e Nikolas, a vertente minerária de Vorcaro, a cadeia de fundos, os novos documentos do TCU e as pendências, com fontes e limites.

A [checagem final do TCU e da CVM](checagem-final-tcu-cvm-2026-09-06.md) registra o recurso R001, a cautela sobre o prazo de novembro, a discrepância de valores da ata e as limitações da busca inversa. A [matriz de elos e diligências](matriz-consolidada-elos-2026-09-06.json) permite consultar relações, valores, fontes e status sem reconstruir todas as rodadas.

O [prompt para o Claude](prompt-claude-consolidacao-final-2026-09-06.md) orienta uma revisão independente, não a redação ou publicação automática da matéria. A decisão sobre quem escreverá continua com Miguel.

O corte de entrada desta consolidação foi o commit `fe5b0f9b2dbfe9bfddb51fa84d33d2a3cbac7a29`. Os originais e relatórios anteriores foram preservados e prevalecem como fontes sobre qualquer resumo de agente.

A equipe registrou uma LAI à ANM, protocolo `48003.018654/2026-33`, com prazo indicado de 28/09/2026. O recibo autenticado não foi conferido pelo GPT nesta rodada, o Pedido 2 segue redigido e os novos pedidos de manifestação jornalística continuam sem envio confirmado.

A referência de 11/11/2026 para a entrega ao TCU é aritmética e depende da verificação do recurso e de decisões posteriores. Não é garantia de publicação automática dos documentos.

A consolidação não foi copiada automaticamente para o Drive. O link do Drive abaixo continua sendo o backup do pacote pós-Fable daquela rodada, não um espelho atualizado de toda esta pasta.

## Histórico da gravação do pacote pós-Fable

A nova tentativa de gravação do pacote pós-Fable foi aceita. Os seis arquivos que haviam sido entregues localmente agora estão nesta pasta, preservados integralmente, e também foram copiados para o Google Drive.

Leia [00-LEIA-ME-salvamento-2026-09-06.md](00-LEIA-ME-salvamento-2026-09-06.md) para o registro dos commits e do escopo da cópia. As referências a bloqueio no pacote original descrevem a primeira tentativa e não o estado atual.

Depois do briefing e do [relatório do Fable](relatorio-fable-continuidade-2026-09-06.md), leia o [relatório integral pós-Fable](relatorio-gpt-pos-fable-2026-09-06.md) e o [adendo ao briefing](adendo-briefing-pos-fable-2026-09-06.md). Esses documentos acrescentam os achados posteriores, as correções de interpretação e as pendências de acesso, sem substituir o histórico.

Os dados estão em [dados/anm-topazio-pauta-88-2026.json](dados/anm-topazio-pauta-88-2026.json), com verificador em [scripts/conferir_recursos_anm.py](scripts/conferir_recursos_anm.py). A pauta não comprova julgamento, e a ligação entre o ativo do áudio e os títulos minerários continua pendente.

Cópia do pacote completo daquela rodada no Google Drive, com arquivos separados e ZIP original

https://drive.google.com/drive/folders/1ylwR1hoQyKlJQqE_Gt3KPE9vgR6Bk9lQ

## Objetivo

Produzir a parte 2 de uma reportagem sobre o áudio em que o deputado Nikolas Ferreira (PL-MG) pediu ao banqueiro Daniel Vorcaro ajuda para um "ativo minerário" de seu advogado e assessor Thiago Rodrigues de Faria. A parte 2 deve trazer informação inédita, verificada em fonte primária, com direito de resposta aos citados.

## Contexto (parte 1, já publicada)

https://www.ocafezinho.com/2026/09/05/o-escandalo-por-tras-do-audio-de-nikolas-para-vorcaro

## Achado exclusivo ainda não publicado

Pelo Portal da Transparência da Câmara, Faria foi secretário parlamentar no gabinete de Nikolas de 09/03/2023 a 30/03/2026, sem interrupção, inicialmente SP24 e depois SP22, conforme o detalhamento do briefing. Estava na folha quando assinou o contrato com a Gmais Ambiental (jan/2025), quando o áudio foi gravado (30/03/2025) e quando a Operação Rejeito prendeu os gestores da Gmais (17/09/2025).

Saiu 25 dias após a data, registrada na pesquisa anterior, em que a PF entregou à CPMI do INSS a agenda de Vorcaro com o nome do deputado (05/03/2026). A proximidade das datas não comprova o motivo da exoneração.

A pesquisa anterior calculou mais de R$ 700 mil em 37 meses, com as rubricas e ressalvas descritas no briefing. Detalhes em `folha-camara-thiago-rodrigues-de-faria.csv` e `secao-exclusiva-faria-folha-camara.html`.

## Arquivos históricos e fontes

- [briefing-continuidade-caso-faria-gmais.md](briefing-continuidade-caso-faria-gmais.md) — histórico da apuração, base pública anterior, achados documentais, correções, 11 caminhos e lista dos 41 recursos da ANM. Para o estado atual, usar primeiro a consolidação indicada no início deste README.
- [relatorio-gpt-continuidade-2026-09-05.md](relatorio-gpt-continuidade-2026-09-05.md) — conteúdo substantivo da devolutiva do GPT, com fontes, localizadores, limites e pendências para a passagem ao Fable.
- [prompt-fable-continuidade.md](prompt-fable-continuidade.md) — instruções e sequência sugerida da primeira continuidade. Consultar o prompt mais recente para não repetir pendências já resolvidas.
- `folha-camara-thiago-rodrigues-de-faria.csv` — remuneração mês a mês, extraída do portal da Câmara.
- `secao-exclusiva-faria-folha-camara.html` — versão de trabalho do achado anterior, sujeita à revisão e ao contraditório.
- `artigo-parte-1-com-secao-exclusiva.html` — parte 1 completa com a seção exclusiva inserida (versão de trabalho, não publicada).
- `transcricao-orofino-calma-urgente.txt` — transcrição automática (faster-whisper) da fala de Alessandra Orofino no Calma Urgente.
- `audio-orofino-calma-urgente.mp4` — áudio original baixado do X.
- `fontes-consultadas.md` — fontes reunidas na pesquisa inicial, com links e descartes. A classificação deve ser lida à luz das correções no briefing, pois reportagens e agregadores não são fontes primárias.

## Continuidade e passagem ao Fable

O briefing atualizado e o relatório do GPT preservam os achados da ANM, a correção da hipótese jurídica, as pistas de CNPJ e os caminhos ainda não concluídos no Master e no TSE. Os links e localizadores dos documentos externos foram registrados, mas esses documentos não foram anexados como cópias binárias naquela passagem.

O relatório é um registro da rodada anterior, não uma nova verificação independente. Antes de publicar, reabrir as fontes, confirmar o conteúdo efetivamente publicado na parte 1 e manter as ressalvas do briefing.

Nenhum pedido de manifestação foi enviado na rodada do GPT. Os arquivos desta pasta não equivalem a autorização para publicação ou a registro de contato com os citados.

## Regras editoriais do Cafezinho

- Acusações sempre atribuídas a fonte nomeada, nunca afirmadas como fato.
- Não reproduzir trechos de outros veículos, só citar e atribuir.
- Não citar BBC Brasil como fonte.
- Sem ponto e vírgula, dois pontos ou travessão no texto. Parágrafos curtos, no máximo duas frases.
- Antes de publicar dado novo, registrar pedido de manifestação a Nikolas, Faria, Gmais, Topázio Imperial e Estabil.
