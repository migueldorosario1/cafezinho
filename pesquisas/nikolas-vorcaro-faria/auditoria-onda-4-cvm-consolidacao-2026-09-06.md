# Conferência da onda 4 e preparação da consolidação

Revisão GPT de 06/09/2026 para Miguel do Rosário e O Cafezinho. Documento de apuração, não reportagem liberada para publicação.

## Resultado executivo

A onda do Fable acrescentou um elo nominal e quantificado entre o Victoria Falls FIM e o Victoria Falls FIP. Também acrescentou o registro do FIP Itaminas na declaração de carteira do MCL B e um campo cadastral de patrimônio negativo da classe do FIP Itaminas.

Esses avanços identificam veículos e exposições declaradas. Não identificam o beneficiário final, não excluem avaliação de oportunidade sem aquisição e não demonstram ligação desses fundos com a proposta de Faria.

A releitura do CSV revelou outro caminho não destacado pelo Fable. G5 F Itaminas e WHG PCS II Itaminas declaram posições em um mesmo fundo, CNPJ 60.715.887/0001-26, ao contrário da afirmação de que suas carteiras não estavam disponíveis.

Para consolidar, incorporar os elos positivos e retirar as conclusões negativas universais. A tarefa central continua sendo obter a proposta reconhecida por Faria e identificar seus destinatários, o direito minerário e a pessoa jurídica representada.

## Escopo efetivamente verificado

Foram lidos pelo conector GitHub o relatório da onda 4, os dois CSVs cadastrais, o script de busca e trechos do CSV de carteiras que contêm os registros relevantes de setembro de 2024, março de 2025 e junho de 2025. Foram conferidos os seguintes blobs.

- Relatório `onda-4-fable-cvm-cadeia-de-fundos-2026-09-06.md`, blob `4eaefbf0c333772be6c60cde5dc7664ee15384e7`.
- Carteiras `dados/cvm-cda-victoria-falls-itaminas-2024-09-a-2025-06.csv`, blob `5551a86d41fea34e98bf55333ff88173aa47d836`.
- Cadastro de fundos `dados/cvm-registro-fundos-victoria-falls-itaminas.csv`, blob `28250356b9de3b88711e42e7183a4c04ac06404c`.
- Cadastro de classe `dados/cvm-registro-classe-fip-itaminas-victoria-falls.csv`, blob `04f518a803f56daf6d8c4e0d4d9c6ec8994f8094`.
- Script `scripts/cvm_busca_inversa_cotistas.py`, blob `a069da03b76efb36c7b41ddcba3e1f5bbebbcf83`.

Não houve reexecução integral dos ZIPs. A nova tentativa de acesso programático à base de março falhou por resolução DNS, e a tentativa de download pelo recurso de download também falhou.

Foram abertas a documentação oficial da CDA e as páginas dos informes do Victoria Falls FIP e do FIP Itaminas. A identificação do fundo comum a G5 e WHG foi localizada no conteúdo indexado do site de sua administradora, mas a abertura direta desse site devolveu erro.

O comunicado oficial do Banco Central sobre a CBSF foi recuperado em resultado indexado. A abertura direta devolveu uma página dependente de JavaScript, limitação registrada sem apresentar leitura integral do ato de liquidação.

## 1. O elo Victoria Falls FIM e FIP é novo e consistente

No bloco 2 da extração, o declarante Victoria Falls Fundo de Investimento Multimercado Investimento no Exterior, CNPJ 15.779.618/0001-79, identifica como fundo investido o Victoria Falls FIP, CNPJ 10.566.011/0001-97.

| Competência da extração | Posição de cotas do FIP declarada pelo FIM |
|---|---:|
| Setembro de 2024 | R$ 73.489.307,61 |
| Março de 2025 | R$ 76.461.631,34 |
| Junho de 2025 | R$ 76.866.050,63 |

Localizador reproduzível no CSV de carteiras — bloco 2, `cnpj_declarante=15.779.618/0001-79` e `cnpj_cota=10.566.011/0001-97`, nas três competências.

O cadastro extraído identifica Master Corretora como administradora e Smart Agro Investimentos como gestora dos dois fundos. Isso não transforma a administradora em titular das cotas nem prova propriedade pessoal de Daniel Vorcaro.

O informe oficial do FIP recebido em 21/05/2025 registra um cotista na categoria outros fundos, com 100%. Seu seletor de competência não aparece na extração da ferramenta desta revisão, e a rodada ZCode havia preservado a competência janeiro a abril de 2025.

Fonte oficial do informe

https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/InfoTrim/CPublicaInfTrimV2.aspx?PK_PARTIC=94015&TpConsulta=24&TpPartic=73

### Conferência aritmética adicional

Foi reconstruído um saldo líquido do FIP a partir dos investimentos, disponibilidades, valores a receber e a pagar do CSV resumido. O resultado foi confrontado com a posição de cotas declarada pelo FIM.

| Competência | Saldo líquido reconstruído do FIP | Posição declarada pelo FIM | Diferença, FIM menos saldo |
|---|---:|---:|---:|
| Setembro de 2024 | R$ 73.489.307,60 | R$ 73.489.307,61 | R$ 0,01 |
| Março de 2025 | R$ 76.461.631,36 | R$ 76.461.631,34 | R$ -0,02 |
| Junho de 2025 | R$ 76.866.050,66 | R$ 76.866.050,63 | R$ -0,03 |

A proximidade até centavos reforça a consistência do cruzamento. Não substitui as quantidades de cotas, o registro de cotistas nem o campo de patrimônio líquido da base original.

A formulação mais segura é que o FIM declarou essas posições no FIP nas três competências. A identificação é fortemente compatível com o cotista único do informe, mas não prova titularidade durante todos os dias intermediários ou beneficiário final.

## 2. A busca negativa não identifica quem está acima do FIM

A afirmação de que nenhum resultado significa necessariamente pessoa física, empresa não financeira ou offshore no topo não decorre da busca executada. Três competências não abrangem todas as datas, formas de declaração ou limitações de divulgação.

A própria documentação da CVM informa que aplicações sob confidencialidade aparecem agregadas, sem detalhamento, e descreve conjuntos e arquivos distintos. Uma ausência no recorte não equivale a uma certidão negativa universal.

Fonte primária de metodologia, especialmente seção Importante

https://dados.cvm.gov.br/dataset/fi-doc-cda

A expressão Investimento no Exterior no nome de um fundo não identifica a residência de seus cotistas. Não há base nesta pesquisa para qualificar o investidor final como estrangeiro, offshore ou não financeiro.

Formulação para a consolidação — não foi identificado, no recorte consultado, outro fundo que declarasse cotas do Victoria Falls FIM. A cadeia ainda não foi fechada.

A mesma ressalva vale para o MCL B. Também não se deve concluir que um fundo esteja fora de qualquer relação com o Master somente por ter administrador diferente.

## 3. Cancelamentos de agosto são datas novas, não prova de destino dos ativos

O CSV cadastral registra cancelamento do Victoria Falls FIM em 21/08/2025 e do Victoria Falls FIP em 30/08/2025. Esses são dados novos e úteis de cronologia cadastral.

Não converter essas datas automaticamente em datas de venda da Taquaril, liquidação material de cada investimento, pagamento ao cotista ou transferência para um beneficiário específico. Atos de encerramento e instrumentos de transferência continuam necessários.

O homônimo CNPJ 13.596.279/0001-60 aparece com BEM e Brainvest no cadastro, ao contrário dos dois veículos anteriores. Não há prova no material revisto de que pertença à família Wanderley ou de ausência de qualquer vínculo indireto.

## 4. O MCL B acrescenta um registro nominal, com posição de valor zero

A extração de março e junho de 2025 registra MCL B Fundo de Investimento Multimercado Crédito Privado, CNPJ 57.717.000/0001-24, como declarante de uma linha de cotas do FIP Itaminas, CNPJ 53.263.484/0001-28. O campo resumido de valor está em R$ 0,00 nas duas competências.

O cadastro identifica registro em 16/10/2024, administradora Master Corretora e gestora CBSF Trust. Trata-se de uma pessoa jurídica específica a investigar, mas não de prova da finalidade de sua criação.

Localizador no CSV de carteiras — bloco 2, `cnpj_declarante=57.717.000/0001-24` e `cnpj_cota=53.263.484/0001-28`.

O CSV resumido não preservou quantidade de cotas, custo, compras ou vendas. É necessário recuperar a linha original completa antes de afirmar propriedade efetiva, participação integral, montante investido ou explicar o valor zero por iliquidez.

Também há um limite temporal que não deve se perder. O informe do FIP Itaminas recebido em setembro de 2024 já declarava um cotista fundo, enquanto o MCL B só aparece registrado em outubro de 2024.

Logo, esse informe antigo não identifica o MCL B como seu cotista naquele momento. A eventual entrada posterior exige documentação e data próprias.

Fonte primária do informe antigo

https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/InfoTrim/CPublicaInfTrimV2.aspx?PK_PARTIC=239948&TpConsulta=24&TpPartic=73

A data de 01/11/2024 é a do comunicado empresarial da AVG utilizado no acervo. Não transformá-la, sem o despacho original, na data exata da decisão do Cade para calcular uma sequência causal de criação e aquisição.

## 5. Patrimônio negativo do FIP Itaminas é dado novo, com entidade e data precisas

O CSV da classe informa CNPJ 53.263.484/0001-28, ID de classe 28270, patrimônio líquido de R$ -234.140.380,86 e data-base 31/12/2025. Isso é distinto do patrimônio antigo de R$ -695,24 na ficha geral, datado de 31/08/2024.

A formulação permitida nesta revisão é que o campo cadastral extraído registra o valor negativo. Não foi obtida a demonstração financeira correspondente para explicar composição, causas, eventuais reapresentações ou efeitos sobre credores.

Não chamar esse número de dívida da mineradora Itaminas, prejuízo do Banco Master ou prova de financiamento do ativo de Faria. Fundo, investida, banco, custodiante e administradora são entidades diferentes.

O cadastro da classe identifica como custodiante CBSF Distribuidora de Títulos e Valores Mobiliários, CNPJ 34.829.992/0001-86. A administradora CBSF Trust, CNPJ 23.863.529/0001-34, é outra pessoa jurídica.

O Banco Central informa ter decretado a liquidação da CBSF DTVM em 15/01/2026. Não aplicar esse estado cadastral posterior retroativamente a 31/12/2025, nem usar a liquidação do custodiante como prova da causa do patrimônio negativo do fundo.

Fonte primária do BC, recuperada em texto indexado

https://www.bcb.gov.br/detalhenoticia/20998/nota

## 6. O CSV permite avançar onde o relatório disse não haver carteiras

A afirmação de que G5 e WHG não declaravam carteira nas bases abertas é contrariada pela própria extração de junho de 2025. Os dois aparecem como declarantes, e não apenas como fundos investidos por terceiros.

| Declarante | CNPJ do declarante | CNPJ do fundo investido | Valor da posição em junho de 2025 |
|---|---|---|---:|
| G5 F Itaminas Minérios | 41.574.762/0001-89 | 60.715.887/0001-26 | R$ 45.276.038,94 |
| WHG PCS II Itaminas | 55.582.462/0001-56 | 60.715.887/0001-26 | R$ 144.883.324,68 |

As duas posições somam R$ 190.159.363,62. Isso é soma de cotas declaradas, não montante comprovadamente entregue à mineradora ou a Vorcaro.

O conteúdo indexado do site da FIDD identifica o CNPJ de destino como PCS II PPE Feeder Brasil Fundo de Investimento Financeiro, com gestão Prisma Private Equity. A abertura direta do site falhou nesta rodada, de modo que a identificação deve ser confrontada com o cadastro e o regulamento original.

Fonte primária empresarial localizada pela indexação

https://www.fiddgroup.com/fundo-investimentos/

Esse é um ponto documental adicional para investigar o lado do financiamento, considerando a participação da Prisma já atribuída a uma publicação jurídica no relatório da onda 3. A carteira do fundo de destino e a escritura de debêntures ainda são necessárias para conectar as cotas a um crédito específico.

Não chamar esses fundos de detentores diretos das debêntures apenas pelo nome Itaminas. Não lhes atribuir qualquer envolvimento no negócio de Faria.

## 7. A carteira do FIP não exclui uma avaliação do ativo

Nos registros examinados não aparece nova rubrica nominal identificando Topázio, Gmais, 3D ou o ativo de Faria. Isso não prova que o fundo ou sua equipe nunca tenham recebido ou analisado uma proposta.

Avaliação sem compra, proposta recusada e atuação de uma investida não precisam aparecer como aquisição direta de um novo ativo na posição final do fundo. Três fotografias mensais também não demonstram tudo o que ocorreu nos intervalos.

A lista principal de quatro investidas persiste, mas os valores não são iguais nas três competências. A participação em 5W passa de R$ 32.584,39 em setembro de 2024 para R$ 2.654.910,79 em março de 2025, e outras rubricas também variam.

Essa variação não prova, sozinha, aporte novo ou ganho de mercado. O acervo anterior já traz notas sobre integralização na 5W, e a conciliação deve usar atos e contabilidade, sem transformar fotografias em fluxos.

A identificação da Tropical não é mais pendência. Foi feita na rodada ZCode e na auditoria anterior, como Tropical Indústria de Alimentos, marca Tial, e não mineradora.

Referência preservada

[auditoria-zcode-master-2026-09-06.md](auditoria-zcode-master-2026-09-06.md)

## 8. A declaração de Faria continua central, mas não fornece uma data de encerramento

A nota reproduzida por O Fator foi reaberta. Faria reconhece apresentação de oportunidade a Vorcaro e aos advogados dele, afirma que Nikolas somente forneceu o contato e que as tratativas não avançaram e acabaram encerradas.

A manifestação não identifica a data do pedido de contato, quais notícias motivaram a desistência ou a data do encerramento. Não permite situar esse encerramento depois do áudio apenas pela expressão sobre notícias que vieram a público.

A comparação com críticas anteriores de Nikolas pode orientar perguntas, mas não deve ser descrita como contradição temporal já demonstrada sem fechar essas datas e o objeto das declarações. Preservar sempre a versão de ausência de negócio concluído.

Fonte de declaração reproduzida por veículo, não nota original recebida pelo Cafezinho

https://ofator.com.br/informacao/advogado-diz-que-nikolas-apenas-forneceu-contato-de-vorcaro-mas-nao-participou-de-negociacao-que-acabou-encerrada/

## 9. Ajustes de método para o próximo arquivo de dados

O script usa busca literal de CNPJ e separação por ponto e vírgula com `split`, em vez de um leitor CSV que respeite campos entre aspas. Também depende dos nomes atuais de colunas para classificar os papéis.

Isso não demonstra que as correspondências positivas aqui lidas estejam erradas. Impede tratar o resultado negativo como exaustivo sem testar normalização de CNPJ, versões de layout, campos alternativos, fundos e classes, duplicatas e cobertura dos arquivos confidenciais.

Preservar na próxima extração a linha integral, nome do arquivo, número da linha, data-base, CNPJ declarante, CNPJ investido, quantidades, custo, valor final, aquisições e vendas. Gravar URL, data e hash dos ZIPs efetivamente processados.

A extração resumida atual preserva relações úteis, mas perde informações decisivas para interpretar posições zero. As linhas do arquivo PL, por exemplo, aparecem sem o valor do PL nas colunas selecionadas.

## 10. Orientação de consolidação

É possível consolidar a narrativa documental sem esperar o fechamento de todas as ramificações financeiras. Separar o vínculo funcional de Faria, o contrato descrito nas reportagens, a apresentação que ele reconhece e o contexto empresarial e financeiro do grupo de Vorcaro.

Incluir como novidade o Victoria Falls FIM identificado na cadeia, com os valores e datas corretos. Tratar MCL B como registro nominal a completar e o patrimônio negativo do FIP Itaminas como uma apuração contábil separada, não como prova do negócio minerário levado pelo advogado.

O elo que ainda falta é a proposta ou comunicação com destinatários, títulos minerários e pessoa jurídica interessada. A existência de empresas e fundos ligados por participações não resolve quem recebeu ou avaliou o ativo de Faria.

Prioridades de fechamento

1. Obter a proposta de Faria e identificar os advogados, o cliente representado, o título ANM e as datas de apresentação e desistência.
2. Recuperar as linhas completas da CDA para MCL B e o registro de cotistas nas datas relevantes, além dos atos de encerramento dos Victoria Falls.
3. Obter as demonstrações da classe do FIP Itaminas em 31/12/2025 e abrir o fundo comum a G5 e WHG apenas na medida em que ajude a identificar a operação de crédito.

Nenhum pedido de manifestação foi enviado nesta revisão. O relatório do Fable, os CSVs e a reportagem não foram sobrescritos.
