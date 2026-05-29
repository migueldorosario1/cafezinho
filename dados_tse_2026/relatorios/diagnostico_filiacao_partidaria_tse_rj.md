# Diagnóstico inicial — filiação partidária no TSE, Brasil e Rio de Janeiro

Este relatório registra o **download e o diagnóstico inicial** das bases de partidos políticos do Portal de Dados Abertos do TSE, com prioridade para a base de **perfil da filiação partidária**. O objetivo operacional foi criar uma base de trabalho para comparar o estado do Rio de Janeiro com o restante do país e, dentro do Rio, comparar municípios e partidos. A base principal analisada foi o arquivo `perfil_filiacao_partidaria.zip`, disponibilizado pelo TSE como recurso de “Perfil Filiação Partidária”.[1]

A base foi baixada diretamente do CDN estatístico do TSE e processada localmente. O arquivo compactado tem **231.694.767 bytes**; dentro dele há o CSV `perfil_filiacao_partidaria.csv`, com **3.524.940.132 bytes** descompactados. O processamento leu **12.617.991 linhas agregadas** e somou **16.129.441 filiados** no Brasil. No Rio de Janeiro, a soma encontrada foi de **1.002.835 filiados**, distribuídos pelos **92 municípios fluminenses** e por **31 partidos**.

> **Ponto crítico para a pauta:** esta base de perfil, no arquivo baixado agora, contém apenas o período `NR_ANO_MES = 202604`. Portanto, ela permite um retrato detalhado da filiação por partido, município, UF, gênero, faixa etária, escolaridade, ocupação, raça/cor e outros recortes, mas **não traz uma série histórica mensal interna**. Para estudar evolução e migração partidária ao longo do tempo, será necessário cruzar esta fotografia com outras bases históricas, versões arquivadas do TSE ou bases eleitorais de candidatos/votação/órgãos partidários.

## Arquivos baixados

|Base|Arquivo local|Tamanho compactado|Conteúdo principal|Uso jornalístico imediato|
|---|---|---:|---|---|
|Perfil da filiação partidária|`downloads/perfil_filiacao_partidaria.zip`|221 MB|Agregados de filiados por partido, UF, município, zona e perfil social|Base central para comparar Brasil, RJ, municípios e partidos|
|Órgãos partidários|`downloads/orgao_partidario.zip`|208 MB|Órgãos partidários, abrangência, vigência e membros dirigentes|Mapear presença organizativa e capilaridade partidária|
|Delegados partidários|`downloads/delegado_partidario.zip`|453 KB|Delegados partidários por partido e unidade eleitoral|Complementar estrutura formal dos partidos|

Os leiautes oficiais dos arquivos de órgãos e delegados informam que os CSVs usam **codificação Latin-1**, campos entre aspas e separados por ponto e vírgula, e marcadores como `#NULO` para informação em branco e `#NE` para informação não registrada no ano correspondente.[2] [3]

## Campos disponíveis na base de perfil de filiação

A base de perfil é especialmente útil porque não traz apenas o total por partido. Ela permite cruzamentos territoriais e sociais. Os campos identificados no CSV são:

`DT_GERACAO`
`HH_GERACAO`
`NR_ANO_MES`
`NR_PARTIDO`
`SG_PARTIDO`
`NM_PARTIDO`
`SG_UF`
`CD_MUNICIPIO`
`NM_MUNICIPIO`
`NR_ZONA`
`CD_GENERO`
`DS_GENERO`
`CD_FAIXA_ETARIA`
`DS_FAIXA_ETARIA`
`CD_ESTADO_CIVIL`
`DS_ESTADO_CIVIL`
`CD_GRAU_INSTRUCAO`
`DS_GRAU_INSTRUCAO`
`CD_OBJETO_OCUPACAO`
`NM_OCUPACAO`
`CD_RACA_COR`
`DS_RACA_COR`
`CD_IDENTIDADE_GENERO`
`DS_IDENTIDADE_GENERO`
`CD_QUILOMBOLA`
`DS_QUILOMBOLA`
`CD_INTERPRETE_LIBRAS`
`DS_INTERPRETE_LIBRAS`
`QT_FILIADO`

## Comparação inicial entre unidades da federação

A tabela abaixo mostra as UFs com maior número de filiados na fotografia de abril de 2026. O Rio de Janeiro aparece como o **quarto maior contingente de filiados do país**, atrás de São Paulo, Minas Gerais e Rio Grande do Sul.

|UF|Filiados|Participação no Brasil|
|---|---|---|
|SP|2.942.833|18,25%|
|MG|1.665.215|10,32%|
|RS|1.296.760|8,04%|
|RJ|1.002.835|6,22%|
|BA|991.512|6,15%|
|PR|962.772|5,97%|
|SC|883.014|5,47%|
|GO|663.479|4,11%|
|PA|633.229|3,93%|
|PE|620.083|3,84%|
|MA|564.772|3,50%|
|CE|531.779|3,30%|

## Maiores partidos no Brasil

|Partido|Filiados|Participação no Brasil|
|---|---|---|
|MDB|2.020.280|12,53%|
|PT|1.668.828|10,35%|
|PP|1.289.140|7,99%|
|PRD|1.284.504|7,96%|
|PSDB|1.264.112|7,84%|
|PDT|1.076.218|6,67%|
|UNIÃO|1.069.086|6,63%|
|PL|947.503|5,87%|
|PODE|798.213|4,95%|
|PSB|640.428|3,97%|
|REPUBLICANOS|565.654|3,51%|
|PSD|465.507|2,89%|

## Maiores partidos no Rio de Janeiro

No Rio, o **PDT** aparece como maior partido em número de filiados, seguido por **MDB** e **PT**. Esse dado é relevante para uma pauta sobre a história política fluminense, pois o PDT mantém no estado uma presença orgânica superior à sua posição nacional.

|Partido|Filiados no RJ|Participação no RJ|
|---|---|---|
|PDT|144.797|14,44%|
|MDB|115.239|11,49%|
|PT|112.720|11,24%|
|PSDB|77.091|7,69%|
|PL|63.156|6,30%|
|PRD|60.756|6,06%|
|PODE|52.606|5,25%|
|PP|51.130|5,10%|
|PSB|38.074|3,80%|
|UNIÃO|37.934|3,78%|
|PCDOB|26.724|2,66%|
|REPUBLICANOS|24.674|2,46%|
|PSOL|24.442|2,44%|
|AVANTE|22.914|2,28%|
|CIDADANIA|20.543|2,05%|

## Municípios fluminenses com mais filiados

A capital concentra o maior número absoluto, mas a comparação municipal posterior deverá relativizar esses números pela população ou pelo eleitorado de cada município. Para isso, em etapa seguinte, será útil cruzar a base de filiação com o eleitorado municipal do TSE ou com estimativas populacionais do IBGE.

|Município|Filiados|Participação no RJ|
|---|---|---|
|RIO DE JANEIRO|303.316|30,25%|
|SÃO GONÇALO|51.469|5,13%|
|NOVA IGUAÇU|41.416|4,13%|
|DUQUE DE CAXIAS|41.080|4,10%|
|CAMPOS DOS GOYTACAZES|28.461|2,84%|
|NITERÓI|27.818|2,77%|
|SÃO JOÃO DE MERITI|23.933|2,39%|
|BELFORD ROXO|22.730|2,27%|
|VOLTA REDONDA|22.664|2,26%|
|MARICÁ|19.431|1,94%|
|PETRÓPOLIS|18.768|1,87%|
|MACAÉ|16.485|1,64%|
|CABO FRIO|15.860|1,58%|
|NOVA FRIBURGO|14.383|1,43%|
|MAGÉ|13.503|1,35%|

## Perfil dos filiados no Rio de Janeiro

A fotografia do Rio mostra uma filiação fortemente concentrada nas faixas de meia-idade e idosos. O maior grupo está em **45 a 59 anos**, seguido por **60 a 69 anos**. Esse padrão sugere uma baixa renovação geracional da filiação formal, hipótese que pode render uma linha analítica importante para o artigo.

### Gênero

|Gênero|Filiados no RJ|Participação no RJ|
|---|---|---|
|MASCULINO|504.382|50,30%|
|FEMININO|497.005|49,56%|
|NÃO INFORMADO|1.293|0,13%|
|#NULO|155|0,02%|

### Faixa etária

|Faixa etária|Filiados no RJ|Participação no RJ|
|---|---|---|
|45 a 59 anos|319.680|31,88%|
|60 a 69 anos|264.808|26,41%|
|70 a 79 anos|149.686|14,93%|
|35 a 44 anos|142.285|14,19%|
|Superior a 79 anos|74.791|7,46%|
|25 a 34 anos|45.591|4,55%|
|21 a 24 anos|4.691|0,47%|
|18 a 20 anos|1.058|0,11%|
|#NULO|155|0,02%|
|17 anos|61|0,01%|
|16 anos|20|0,00%|
|Inválida|9|0,00%|

### Escolaridade

|Escolaridade|Filiados no RJ|Participação no RJ|
|---|---|---|
|ENSINO FUNDAMENTAL INCOMPLETO|274.512|27,37%|
|ENSINO MÉDIO COMPLETO|230.923|23,03%|
|ENSINO MÉDIO INCOMPLETO|139.411|13,90%|
|SUPERIOR COMPLETO|112.174|11,19%|
|ENSINO FUNDAMENTAL COMPLETO|110.485|11,02%|
|LÊ E ESCREVE|76.649|7,64%|
|SUPERIOR INCOMPLETO|46.538|4,64%|
|ANALFABETO|10.387|1,04%|
|NÃO INFORMADO|1.601|0,16%|
|#NULO|155|0,02%|

## Produtos gerados para a próxima etapa

Além deste relatório, foram gerados CSVs agregados menores para economizar processamento nas próximas análises. Os principais são `brasil_total_por_uf.csv`, `brasil_total_por_partido.csv`, `brasil_total_por_uf_partido.csv`, `rj_total_por_municipio.csv`, `rj_total_por_partido.csv`, `rj_total_por_municipio_partido.csv`, `rj_total_por_faixa_etaria.csv`, `rj_total_por_genero.csv`, `rj_total_por_instrucao.csv`, `rj_total_por_partido_faixa_etaria.csv`, `rj_total_por_partido_genero.csv` e `rj_total_por_partido_instrucao.csv`.

Para uma segunda etapa barata, recomenda-se trabalhar primeiro com esses CSVs agregados, sem reler o CSV bruto de 3,5 GB. Isso permite montar rapidamente rankings por partido, município e perfil social. A releitura da base bruta só será necessária se quisermos criar cruzamentos ainda mais finos, por exemplo partido × município × faixa etária × gênero × instrução.

## Próximos caminhos possíveis

|Caminho|Objetivo|Custo estimado em pontos|Observação|
|---|---|---:|---|
|Análise barata com agregados já gerados|Comparar partidos no RJ, municípios e perfil básico|40–80|Não relê a base bruta; usa CSVs pequenos|
|Cruzamento mais fino no RJ|Partido × município × idade × gênero × escolaridade|100–180|Pode exigir nova leitura parcial da base bruta|
|Série histórica/migração partidária|Buscar bases antigas, snapshots ou dados de filiação nominal/histórica|200–500|Depende de localizar arquivos históricos confiáveis|
|Artigo jornalístico inicial|Texto analítico sobre RJ, partidos e perfil da filiação|80–160|Só deve começar com comando explícito do editor|

## Referências

[1]: https://cdn.tse.jus.br/estatistica/sead/odsele/filiacao_partidaria/perfil_filiacao_partidaria.zip "TSE — Perfil Filiação Partidária"
[2]: https://cdn.tse.jus.br/estatistica/sead/odsele/orgao_partidario/orgao_partidario.zip "TSE — Órgãos Partidários"
[3]: https://cdn.tse.jus.br/estatistica/sead/odsele/delegado_partidario/delegado_partidario.zip "TSE — Delegados Partidários"
[4]: https://dadosabertos.tse.jus.br/dataset/delegados-partidarios "Portal de Dados Abertos do TSE — Partidos"
