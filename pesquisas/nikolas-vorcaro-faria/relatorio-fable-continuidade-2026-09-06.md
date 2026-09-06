# Relatório de continuidade, rodada Fable (06/09/2026)

Apuração para a parte 2 da reportagem do Cafezinho. Esta rodada verificou as pistas do GPT em fonte primária e abriu frentes novas. Nenhum pedido de manifestação foi enviado. Nenhum dado abaixo foi publicado.

Convenção. **Confirmado** significa lido em documento ou base oficial nesta rodada, com localizador. **Atribuído** significa afirmado por veículo ou pela PF conforme citado por veículo. **Pendente** significa hipótese ou pista sem fechamento documental.

## 1. Avanços novos (confirmados em fonte primária)

### 1.1. O escritório de Faria foi aberto em agosto de 2024, em Nova Lima, com ele na folha da Câmara

Base de dados abertos do CNPJ da Receita Federal (espelho minhareceita.org, consulta em 06/09/2026). Cópia em `dados/receita-cnpj-quatro-empresas-2026-09-06.json`.

- Thiago Rodrigues Sociedade Individual de Advocacia, CNPJ 56.902.629/0001-81
- Início de atividade 19/08/2024. Titular Thiago Rodrigues de Faria. Capital social R$ 100.000. Simples Nacional.
- Sede na Rua Mamoré, 35, Alphaville Lagoa dos Ingleses, Nova Lima (MG).

Novidade em relação ao acervo. O GPT tinha o CNPJ como pista de agregador. Agora está confirmado na base da Receita, com titular nominal. Isso resolve a homonímia com o CNPJ paulista.

Cronologia que o dado permite montar, toda em fonte primária ou em documento da PF citado por veículo:

| Data | Fato | Fonte |
|---|---|---|
| 09/03/2023 | Faria entra na folha da Câmara como SP24 no gabinete de Nikolas | Portal da Câmara (CSV no acervo) |
| abr/2024 | Faria e Gilberto Horta criam grupo de WhatsApp "Projeto Ferro" | inquérito da PF, citado por A Investigação (atribuído) |
| 19/08/2024 | Faria abre a sociedade unipessoal de advocacia em Nova Lima | Receita (confirmado) |
| jan/2025 | Escritório assina contrato de intermediação com a Gmais | inquérito da PF, citado por Estado de Minas e A Investigação (atribuído) |
| 18/02/2025 | Gilberto Horta entra como administrador formal da Gmais | Receita (confirmado, ver 1.2) |
| 30/03/2025 | Áudio de Nikolas a Vorcaro | ICL (atribuído, áudio público) |
| 17/09/2025 | Operação Rejeito prende Teixeira e Horta | público |
| 26/12/2025 | ANM distribui 41 recursos da Topázio a Mauro Sousa | Certidão SG-ANM 53/2025 (confirmado, ver 1.4) |
| 30/03/2026 | Faria sai da folha da Câmara | Portal da Câmara (CSV no acervo) |
| 26/06/2026 | PF indicia Mauro Sousa (Operação Parcours) | Poder360, Observatório da Mineração, A Investigação (atribuído) |

Limite. A abertura do escritório com o titular na folha não prova infração. O Estatuto da Advocacia admite sociedade unipessoal de advogado servidor sem dedicação exclusiva (ver relatório do GPT, seção 1). O que a data mostra é que a pessoa jurídica beneficiária do contrato foi criada quatro meses depois do grupo "Projeto Ferro" e cinco meses antes do contrato, e que a sede fica em Nova Lima, município da Serra do Curral onde a PF apurou a extração ilegal.

### 1.2. Gilberto Horta virou administrador formal da Gmais em 18/02/2025

Base da Receita, quadro societário atual da Gmais Ambiental Ltda., CNPJ 41.332.820/0001-68:

- Daniella Santos Wandeck, sócia, entrada 24/03/2021
- Luiz Fernando Vilela Leite, sócio, entrada 24/03/2021
- Gilberto Henrique Horta de Carvalho, administrador, entrada **18/02/2025**

Sede na Av. Barbacena, 1018, sala 103, Santo Agostinho, Belo Horizonte. Capital social R$ 10.000. Abertura 24/03/2021.

Novidade. O acervo dizia que Horta "integrou o quadro societário e depois saiu, substituído por Leite" (A Investigação). A base atual da Receita mostra Horta como administrador com entrada em fevereiro de 2025, ou seja, um mês depois do contrato com o escritório de Faria e seis semanas antes do áudio. Nesse mesmo mês Horta começou como assessor do vereador Uner Augusto (PL-BH), segundo Metrópoles e A Investigação (fev a set/2025).

Limite. A base da Receita mostra o quadro vigente, não o histórico completo. É possível que Horta tenha saído e voltado. Para fechar, pedir a ficha cadastral completa na JUCEMG (Gmais é sociedade empresária, registrada na Junta).

### 1.3. A Topázio Imperial tem uma concessão de lavra de FERRO em Ouro Preto

Dados abertos SIGMINE da ANM, shapefile de Minas Gerais gerado em 05/09/2026, filtrado por titular. Cópia em `dados/topazio_imperial_titulos_anm_sigmine_2026-09-05.csv`. Script em `scripts/extrair_titulos_anm_sigmine.py`.

A Topázio Imperial Mineração Comércio e Indústria Ltda é titular de 10 processos em Minas:

| Processo | Substância | Fase | Área (ha) | Último evento |
|---|---|---|---|---|
| **291701/1936** | **FERRO** | Concessão de lavra | 78,78 | Documento diverso protocolado em 09/04/2007 |
| 800645/1971 | Topázio | Concessão de lavra | 349,10 | Cumprimento de exigência em 04/05/2009 |
| 827501/1972 | Topázio | Concessão de lavra | 62,78 | Cumprimento de exigência em 26/10/2020 |
| 804805/1976 | Topázio | Concessão de lavra | 44,37 | Documento diverso em 09/04/2007 |
| 800214/1978 | Topázio | Concessão de lavra | 163,48 | Suspensão de análise, conflito com projeto energético, 08/07/2013 |
| 830687/1980 | Gema | Concessão de lavra | 22,77 | Documento diverso em 09/04/2007 |
| 830689/1980 | Topázio | Concessão de lavra | 4,29 | Documento diverso em 09/04/2007 |
| 830060/1986 | Gema | Concessão de lavra | 49,98 | Recurso protocolado em 25/04/2022 |
| 832783/1989 | Topázio imperial | Autorização de pesquisa | 14,32 | Prorrogação de prazo em 09/10/2017 |
| 832784/1989 | Gema | Autorização de pesquisa | 24,84 | Documento diverso em 19/10/2004 |

Os centroides dos títulos de Ouro Preto ficam entre 20,41° S e 20,43° S, 43,61° O e 43,65° O, região do distrito de Rodrigo Silva e da Fazenda Capão do Lana, endereço cadastral da empresa na Receita. O título 830060/1986 fica em outra região (19,64° S, 43,11° O).

Por que importa. O grupo de WhatsApp em que Faria e Horta discutiam a transação, segundo o inquérito da PF citado por A Investigação, chamava-se "Projeto Ferro". Até agora a cobertura tratou o ativo como uma lavra de topázio. A existência de uma concessão de lavra de minério de ferro de 78,78 ha em nome da Topázio Imperial, parada desde 2007, abre a hipótese de que o negócio de US$ 30 a 45 milhões envolvesse ferro, e não topázio.

Limite. É hipótese. O nome do grupo pode se referir a outra coisa. O processo 291701/1936 não aparece no documento da PF que o Estado de Minas citou. Para fechar, ler o inquérito ou obter a composição do grupamento (ver 1.5).

### 1.4. Os 41 recursos da Topázio na ANM foram distribuídos ao presidente da agência, indiciado seis meses depois

Certidão SG-ANM 53/2025, processo 48051.000269/2025-83, distribuição em 26/12/2025, 15h, três páginas, lida integralmente nesta rodada. Cópia em `dados/anm-certidao-sg-53-2025-topazio-41-recursos.pdf`.

- As 41 primeiras linhas do bloco 1 são recursos contra imposição de multa da Topázio Imperial, numerados de 2021 (40) e 2022 (1).
- Relator de todos: **Mauro Sousa**, diretor-geral da ANM.
- Responsável pela distribuição: Caio Vasconcelos de Azevedo.

Contexto atribuído (não é da certidão). Em 26/06/2026 a PF concluiu os relatórios finais das operações Rejeito e Parcours e indiciou Mauro Henrique Moreira Sousa por advocacia administrativa e associação criminosa, por manter "canal pessoal e privilegiado" com regulados, no caso da Empabra na Serra do Curral (Poder360, 27/06/2026; Observatório da Mineração, 07 e 09/07/2026). Ele permanece no cargo. A ANM disse que ele atuou "exclusivamente como representante institucional".

O que isso permite dizer. Que 41 recursos de multa da empresa cuja lavra o grupo da Gmais queria destravar foram parar, por distribuição, nas mãos do dirigente da ANM que a PF indiciou por proximidade com mineradores investigados na mesma rede de operações. Nada indica decisão favorável, nem que Sousa tenha agido nesses recursos. Não há na certidão qualquer menção a Faria, Nikolas, Gmais ou Master.

Pendente. Consultar no SEI da ANM (pesquisa pública) cada um dos 41 processos para saber objeto, valor, se houve decisão após 26/12/2025 e quem são os procuradores. O SCM da ANM estava fora do ar (HTTP 503) em 06/09/2026.

### 1.5. O ativo negociado pelo grupo é o grupamento mineiro 930.096/2000

Reportagem de Mateus Parreiras, Estado de Minas, 18/09/2025, reproduzindo diálogos e trechos do relatório da PF (atribuído):

- A PF registra que "o empreendimento da TOPÁZIO MINERAÇÃO encontra-se suspenso em razão do ajuizamento pelo MPF da Ação Civil Pública 1000752-23.2023.4.06.3822, com concessão de tutela de urgência pelo Judiciário".
- Em 23/02/2023 Horta e João Alberto Paixão Lages trocaram prints "relacionados ao processo minerário ANM 930.096/2000 da Topázio Imperial".
- Em 14/03/2023 a última versão virou "Contrato Particular de Arrendamento e Outros Pactos", com Gmais e HCRN como arrendatárias da Topázio, e participação da Gmais em 8%.
- Em 20/07/2023 Horta, ao lado de Rodrigo Teixeira, pergunta a Lages se vão "ver a barragem".
- A barragem Água Fria tem 2 milhões de m³ de rejeitos e nível de emergência 1.

Interpretação técnica. Números da ANM com prefixo 930 são grupamentos mineiros, que reúnem várias concessões contíguas sob um mesmo plano de lavra. O SIGMINE não lista grupamentos como polígonos, só as concessões que os compõem. Por isso 930.096/2000 não aparece no shapefile. Fica a pergunta que decide a hipótese do item 1.3: a concessão de ferro 291701/1936 faz parte do grupamento 930.096/2000? Só o SCM da ANM ou o próprio processo respondem.

Isso também confirma, por citação da PF, que a paralisação da Topázio decorre de tutela de urgência na ACP, o que o GPT ainda não tinha (ele tinha só a portaria do MPF).

### 1.6. Estabil e Topázio, quadro societário confirmado na Receita

- Estabil Escritório Contábil Ltda, CNPJ 11.030.358/0001-83, aberta em 07/08/2009, Rua dos Timbiras, 1840, 4º andar, Lourdes, Belo Horizonte. Sócio-administrador Roberto Carlos de Souza Gomes. Nenhuma ligação com Teixeira, Horta ou Lages foi encontrada em fonte pública. Fica como terceiro beneficiário do contrato (25% da comissão), sem outro vínculo apurado.
- Topázio Imperial Mineração Comércio e Indústria Ltda, CNPJ 16.857.294/0001-02, aberta em 01/11/1971, sede na Fazenda Capão do Lana, Mina Capão do Lana, Rodrigo Silva, Ouro Preto. Sócios Edmar Evanir da Silva, Fernando Celso Gonçalves e Zélia Machado Fonseca Colombarolli (entrada 22/12/1997). Administrador Guilherme Capanema Gonçalves (desde 26/12/2019). O nome Colombarolli coincide com o de Wagner Colombarolli, citado em 2021 por site de gemas como dirigente da empresa. Coincidência de sobrenome, sem prova de parentesco.

### 1.7. A parte 1 publicada foi conferida

Página lida em 06/09/2026. A versão publicada tem seis subtítulos (O que Nikolas pediu a Vorcaro, O contrato de 25% do lucro, A barragem que trava o negócio, Operação Rejeito, Os voos pagos pelo banqueiro, As defesas). Não contém a seção sobre a folha da Câmara, nem Estabil, nem "Projeto Ferro", nem Mauro Sousa, nem a palavra "lindão". Tudo o que está neste relatório e na seção exclusiva do acervo continua inédito no Cafezinho.

## 2. O que foi verificado do GPT e bateu

- Certidão SG-ANM 53/2025: existe, tem 3 páginas, 41 recursos da Topázio, relator Mauro Sousa. Confere.
- CNPJs candidatos do escritório, da Estabil e da Topázio: confirmados na base da Receita, com quadros societários.
- ACP 1000752-23.2023.4.06.3822: a PF, citada pelo Estado de Minas, confirma a tutela de urgência. O juízo (Ponte Nova) continua sem confirmação direta.

## 3. Hipóteses refutadas ou enfraquecidas

- "Faria era ex-assessor quando fez o negócio". Refutada pelo CSV da folha (já no acervo) e agora pela data de abertura do escritório, dentro do período de exercício.
- "A Topázio é só uma mineradora de topázio". Enfraquecida. Ela detém concessão de lavra de ferro.
- "Horta saiu da Gmais e foi substituído por Leite". Enfraquecida. A base atual da Receita o mostra como administrador desde 18/02/2025.
- "Julio Cesar Rodrigues Lage e Silva pode ser parente de João Alberto Lages". Sem qualquer base. O GPT já apontou que ele é advogado (OAB/MG 169.239). Descartar.

## 4. Bloqueios desta rodada

- **TSE**: os servidores cdn.tse.jus.br e divulgacandcontas.tse.jus.br devolvem 403 (Akamai) para este ambiente. O cruzamento eleitoral de 2022 e 2024 precisa ser feito de uma máquina local. Roteiro: baixar `prestacao_de_contas_eleitorais_candidatos_2022.zip` e `_2024.zip`, abrir `despesas_contratadas_candidatos_<ano>_MG.csv` e `receitas_candidatos_<ano>_MG.csv`, filtrar por SQ_CANDIDATO 130001611005 (Nikolas 2022, a confirmar) e 130002172747 (Pablo 2024, a confirmar), e procurar nos fornecedores e doadores os CPFs e CNPJs de Faria (pessoa física, o CNPJ só existe desde ago/2024), Gmais, Estabil, Topázio, Horta, Teixeira, Wandeck, Lages e Baya Andrade.
- **ANM SCM**: fora do ar (503). Necessário para o grupamento 930.096/2000 e para os 41 recursos.
- **CMBH**: portal de transparência da Câmara Municipal de BH não respondeu em tempo hábil. Serve para datar o período de Faria como assessor de Nikolas vereador (2021-2022) e o de Horta com Uner Augusto (2025).
- **PJe TRF6**: não tentado nesta rodada. A consulta pública exige navegador com JavaScript.

## 5. Perguntas de manifestação (não enviadas)

Para o gabinete de Nikolas Ferreira (dep.nikolasferreira@camara.leg.br) e para Thiago Rodrigues de Faria:

1. O deputado sabia, em 30/03/2025, que o escritório de Faria tinha contrato de intermediação com a Gmais Ambiental assinado em janeiro?
2. O "ativo minerário" citado no áudio era o grupamento 930.096/2000 da Topázio Imperial? Envolvia a concessão de lavra de ferro 291701/1936?
3. Faria trabalhava presencialmente em Brasília? Qual era a jornada e o local de exercício registrados na Câmara?
4. O deputado autorizou, por escrito, o exercício de atividade privada de intermediação comercial por um secretário parlamentar?
5. Por que Faria foi exonerado em 30/03/2026?
6. Faria recebeu algum valor da Gmais, da Estabil, da Topázio ou de pessoas ligadas a elas?
7. O grupo "Projeto Ferro", criado em abril de 2024, tratava de qual área?

Para a Gmais Ambiental e para Gilberto Horta (via defesa):

8. Qual foi a data e o motivo da entrada de Horta como administrador em 18/02/2025?
9. O contrato de janeiro de 2025 com o escritório de Faria previa intermediação junto a quem? Banco Master foi procurado?

Para a Topázio Imperial (Fazenda Capão do Lana, Rodrigo Silva):

10. A empresa outorgou procuração à Gmais? Quando? Foi revogada?
11. O grupamento 930.096/2000 inclui o processo 291701/1936 (ferro)?
12. Qual é a situação atual da barragem Água Fria e do projeto de descaracterização?

Para a Estabil:

13. A empresa confirma o contrato e a comissão de 25%? Qual serviço prestaria?

Para a ANM (Lei de Acesso à Informação):

14. Composição do grupamento mineiro 930.096/2000 e situação de cada processo.
15. Situação dos 41 recursos da Topázio distribuídos em 26/12/2025: houve decisão? Quem assinou?

Para a Câmara dos Deputados (LAI, Diretoria de Recursos Humanos):

16. Local de exercício, jornada, folhas de frequência e eventuais afastamentos de Thiago Rodrigues de Faria entre 09/03/2023 e 30/03/2026.
17. Há registro de autorização para atividade externa ou consulta à Corregedoria?

## 6. Arquivos gravados nesta rodada

- `relatorio-fable-continuidade-2026-09-06.md` (este)
- `dados/receita-cnpj-quatro-empresas-2026-09-06.json`
- `dados/topazio_imperial_titulos_anm_sigmine_2026-09-05.csv`
- `dados/anm-certidao-sg-53-2025-topazio-41-recursos.pdf`
- `scripts/extrair_titulos_anm_sigmine.py`
- `scripts/folha_camara_secretario.py`
- `briefing-continuidade-caso-faria-gmais.md` (seção 10 acrescentada)
- `fontes-consultadas.md` (seção da rodada 2 acrescentada)
