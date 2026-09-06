# Onda 4 (Fable). A cadeia de fundos do Master na mineração, lida nas bases da CVM (06/09/2026)

Continuação da linha aberta pelo GPT na onda 3 (identificar quem, no ecossistema de Vorcaro, recebeu a apresentação de Faria). O GPT preparou a busca inversa nas carteiras da CVM mas não conseguiu baixar os arquivos. Esta rodada executou a busca.

## 0. Confirmações e correções

- **Nota de Faria a O Fator (03/09/2026), confirmada na íntegra.** "Na ocasião, representava um direito minerário e, ao saber do interesse do grupo de Daniel Vorcaro no setor, apresentei a oportunidade a ele e a seus advogados." "As tratativas não avançaram e foram posteriormente encerradas." "Tão logo vieram à tona as notícias sobre ele, perdeu-se o interesse." Duas observações. (a) Faria diz que Vorcaro "não era alvo de questionamentos públicos" quando pediu o contato, mas o próprio Nikolas atacou o Master publicamente em abril de 2024, um ano antes. (b) Ao dizer que as tratativas só foram encerradas quando "vieram à tona as notícias", Faria situa a negociação em algum ponto de 2025, depois do áudio. O Fator: https://ofator.com.br/informacao/advogado-diz-que-nikolas-apenas-forneceu-contato-de-vorcaro-mas-nao-participou-de-negociacao-que-acabou-encerrada/
- **Prisões de Vorcaro (correção ao acervo).** Preso em 17/11/2025 em Guarulhos (Dubai), Master liquidado em 18/11, solto em 28/11 pelo TRF-1 com tornozeleira, preso de novo em 04/03/2026 por André Mendonça (3ª fase da Compliance Zero). Segue preso. Fontes: CNN, Migalhas, CartaCapital, Wikipédia (Operação Compliance Zero).

## 1. Método

Bases públicas da CVM (dados.cvm.gov.br), baixadas nesta rodada:
- `cda_fi_202409.zip`, `cda_fi_202503.zip`, `cda_fi_202506.zip` (Composição e Diversificação das Aplicações, todos os fundos, setembro/2024, março/2025 e junho/2025).
- `registro_fundo_classe.zip` (cadastro de fundos e classes, atual).
Busca: em quais carteiras aparecem os CNPJs 10.566.011/0001-97 (Victoria Falls FIP) e 53.263.484/0001-28 (FIP Itaminas), e o que esses fundos declaram ter. Extrações em `dados/cvm-cda-victoria-falls-itaminas-2024-09-a-2025-06.csv` e `dados/cvm-registro-fundos-victoria-falls-itaminas.csv`.

## 2. Resultado: a cadeia do Victoria Falls (confirmado em base oficial)

**Quem é o cotista único do Victoria Falls FIP?** Outro fundo da mesma família: **Victoria Falls Fundo de Investimento Multimercado Investimento no Exterior, CNPJ 15.779.618/0001-79**. Declara cotas do FIP no valor de R$ 73,5 mi (set/2024), R$ 76,5 mi (mar/2025) e R$ 76,9 mi (jun/2025). É praticamente o único ativo do FIM.

**Quem é o cotista do FIM?** Nenhum fundo registrado na CVM declara cotas dele em nenhuma das três competências. Logo, o cotista do FIM é pessoa física, pessoa jurídica não financeira ou veículo estrangeiro. O nome "Investimento no Exterior" e a estrutura FIM sobre FIP são típicas de investidor não residente. A identidade fica fora do alcance das bases públicas da CVM. Caminhos: liquidante do Master (a corretora administrava os dois), Receita (CNPJ do FIM aponta responsável), CPMI.

Dados cadastrais (registro CVM):
| Fundo | CNPJ | Administrador | Gestor | Situação | PL |
|---|---|---|---|---|---|
| Victoria Falls FIP Multiestratégia IE | 10.566.011/0001-97 | Master S/A Corretora | Smart Agro Investimentos | **Cancelado em 30/08/2025** | R$ 76,55 mi (30/04/2025) |
| Victoria Falls FIM IE | 15.779.618/0001-79 | Master S/A Corretora | Smart Agro Investimentos | **Cancelado em 21/08/2025** | R$ 76,88 mi (23/06/2025) |
| Victoria Falls FI Financeiro CI Mult Cred Priv | 13.596.279/0001-60 | BEM DTVM (Bradesco) | Brainvest | Ativo | R$ 23,5 mi (24/04/2025) |

O terceiro fundo, homônimo, é administrado fora do Master e tem carteira pulverizada (títulos públicos, cotas de dezenas de fundos, debêntures). Parece um fundo de gestão de patrimônio da família Wanderley, sem ligação com a cadeia do Master. Registrado para não confundir.

**O que o FIP tinha em 31/03/2025, o mês do áudio** (BLC_8):
| Rubrica | Valor |
|---|---|
| Participacao/TROPICAL | R$ 36.787.000,00 |
| Participacao/PARTICIP TAQUARIL | R$ 33.865.200,01 |
| Participacao/HEALTHY FOR ALL INVE | R$ 3.578.814,19 |
| Participacao/5W PARTICIPACOES LTD | R$ 2.654.910,79 |
| Valores a pagar | R$ 29.022.066,28 |
| Valores a receber | R$ 28.595.458,45 |
Em set/2024 constava ainda "Outros/TAQUARIL" (R$ 165 mil) e a 5W valia R$ 32,6 mil (subiu para R$ 2,65 mi em mar/2025). O campo EMISSOR não traz CNPJ, só o nome abreviado. "Tropical" segue sem identificação. Nenhuma rubrica remete a Topázio, Gmais, Ouro Preto ou 3D Minerals. Ou seja, **até junho de 2025 o FIP não registrou nenhum novo ativo minerário**. Se o "pessoal técnico" avaliou a lavra da Topázio, não foi por este veículo.

## 3. Resultado: a cadeia do FIP Itaminas (confirmado em base oficial)

| Fundo | CNPJ | Registro | Administrador | Gestor | PL |
|---|---|---|---|---|---|
| Itaminas FIP Multiestratégia | 53.263.484/0001-28 | 19/12/2023 | CBSF Trust | CBSF Trust | classe: **R$ -234.140.380,86 em 31/12/2025** |
| **MCL B FIM Crédito Privado** | 57.717.000/0001-24 | **16/10/2024** | **Master S/A Corretora** | CBSF Trust | não informado |
| G5 F Itaminas Minérios FIF Multimercado | 41.574.762/0001-89 | 04/05/2021 | BTG Pactual Serviços | G5 Administradora | não informado |
| WHG PCS II Itaminas FIM CP | 55.582.462/0001-56 | 18/06/2024 | XP Investimentos | Wealth High Governance | não informado |
| WHG Itaminas II FIM CP | 61.767.942/0001-94 | 16/07/2025 | XP Investimentos | Wealth High Governance | não informado |

O que isso mostra:
- O **MCL B**, administrado pela corretora do Master e gerido pela mesma CBSF Trust que administra o FIP Itaminas, foi registrado em **16/10/2024**, três semanas antes da aprovação do Cade (01/11/2024) e do empréstimo à 3D (05/11/2024). É o único fundo da CVM que declara cotas do FIP Itaminas, com valor zero em mar/2025 e jun/2025 (posição registrada sem valor de mercado, comum em FIP fechado ilíquido). Nenhum fundo declara cotas do MCL B, logo seu cotista também é não financeiro.
- A classe do FIP Itaminas fechou 2025 com **patrimônio negativo de R$ 234 milhões**, e o custodiante, CBSF DTVM, está "em liquidação extrajudicial". Isso é compatível com o que a revista The Latin American Lawyer descreveu (debêntures da Itaminas com garantias sobre ações e garantias pessoais) e com um passivo que superou os ativos depois da queda do Master.
- Os fundos G5 (BTG) e WHG (XP) com "Itaminas" no nome são veículos de crédito, provavelmente os detentores das debêntures. Não declaram carteira nas bases abertas (fundos privados).

## 4. O que a rodada fecha e o que deixa aberto

**Fecha.** O cotista do Victoria Falls FIP tem nome: o Victoria Falls FIM IE, também do Master. O FIP não incorporou nenhum ativo novo entre set/2024 e jun/2025. O FIP Itaminas tem um veículo do Master acoplado (MCL B) criado às vésperas da compra, e está com patrimônio negativo de R$ 234 mi.

**Deixa aberto.** Quem está acima do FIM e do MCL B (pessoa física, empresa ou offshore). Quem é "Tropical". Quem eram os "advogados" de Vorcaro a quem Faria diz ter apresentado a lavra. A busca inversa nas bases públicas chegou ao limite: os cotistas finais não são fundos.

## 5. Caminhos
1. **Receita Federal**: CNPJ do Victoria Falls FIM (15.779.618/0001-79) e do MCL B (57.717.000/0001-24). O QSA de fundo traz o administrador, mas a ficha pode indicar o responsável. Tentar via minhareceita.
2. **Liquidante do Master**: relatório da liquidação extrajudicial ao BC lista fundos administrados e cotistas relevantes.
3. **CPMI do INSS**: o celular de Vorcaro tem as conversas com Wanderley, Zettel, AVG (Rodrigo Gontijo, Marcelo Pugedo), Ageo e os advogados da Itaminas (Azevedo Sette). Pedir aos relatores a busca por "Faria", "Topázio", "Ouro Preto", "Rodrigo Silva".
4. **Azevedo Sette**: perguntar formalmente se o escritório recebeu, entre março e dezembro de 2025, apresentação de direito minerário em Ouro Preto por Thiago Rodrigues de Faria, em nome da RDA, da Itaminas ou de Vorcaro.
5. **AVG / Marcelo Pugedo**: a pista do Estado de Minas (áudio de out/2021, R$ 25 mi, grupo Brava) liga a AVG ao núcleo da Gmais três anos antes de a AVG comprar a Itaminas com Vorcaro. Verificar no inquérito quem era a contraparte e qual o ativo.
6. **Cedro / Kallas**: a visita de Teixeira a Kallas (2021-22) com possível oferta de ativo minerário, arquivada em out/2023 (A Investigação). Pedir a peça arquivada.

## 6. Arquivos
- `dados/cvm-cda-victoria-falls-itaminas-2024-09-a-2025-06.csv` (255 linhas, as três competências)
- `dados/cvm-registro-fundos-victoria-falls-itaminas.csv` (8 fundos)
- `dados/cvm-registro-classe-fip-itaminas-victoria-falls.csv`
- `scripts/cvm_busca_inversa_cotistas.py`
