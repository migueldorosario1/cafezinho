# Continuidade após a rodada do Claude/Fable

Rodada de 06/09/2026, preparada para Miguel do Rosário e O Cafezinho. Documento de apuração, não reportagem liberada para publicação.

## Estado da entrega

Foram lidos o README, o relatório do Fable, o índice de fontes e as extrações cadastrais e minerárias da pasta `pesquisas/nikolas-vorcaro-faria`, na branch `master` de `migueldorosario1/cafezinho`. A referência de partida conferida foi o commit `b065f010fbdd4ad4125e9f38d4eacabe08106cb5`.

A tentativa de criar no GitHub o JSON desta rodada foi bloqueada pela ferramenta, que informou não conseguir determinar o status de segurança da solicitação. Nenhum commit desta rodada foi confirmado, e o material está sendo entregue em arquivos locais para preservação.

Os arquivos anteriores do repositório não foram substituídos. Este relatório é um adendo de continuidade, com correções de interpretação que devem acompanhar a leitura do briefing e do relatório do Fable.

Nenhum pedido de manifestação foi enviado. Não há prova nova de operação concluída, comissão recebida ou identidade entre o ativo do áudio e os títulos da Topázio apresentados nos documentos ambientais.

## 1. Novidade documental na ANM

### Os 41 recursos aparecem em uma pauta com 90 processos

A pauta oficial da 88ª Reunião Ordinária Pública da diretoria da ANM, marcada para 19/08/2026, reúne 90 processos da Topázio no item 1.1.1. O assunto é recurso contra multa aplicada em fiscalização de barragem, no bloco de Mauro Henrique Moreira Sousa, identificado ali como diretor-geral. [S01]

Os identificadores foram transcritos das páginas 1 e 2 e comparados por igualdade exata com os 41 do briefing anterior. Todos os 41 estão presentes, e há 49 identificadores adicionais, sem duplicatas na transcrição.

A lista completa, o conjunto anterior e a diferença estão em `dados/anm-topazio-pauta-88-2026.json`. O verificador em `scripts/conferir_recursos_anm.py` permite refazer a comparação localmente.

O ganho é identificar uma movimentação posterior à distribuição de dezembro de 2025 e especificar a natureza das multas. Não são necessariamente 49 novas infrações, e não se pode atribuir todas à Água Fria sem examinar os autos.

Pauta não demonstra julgamento, voto, resultado ou favorecimento. A contagem de processos também não informa o valor total das multas.

### Onde buscar o resultado

A pauta tem documento SEI 20613489, código CRC B5F5CD69, e integra o processo 48051.009607/2026-23. A ata da 88ª reunião não foi localizada na coleção consultada, cuja listagem mais recente era a da 87ª. [S01, S03]

A gravação foi localizada por busca, mas não foi assistida ou transcrita nesta rodada. A notícia oficial da reunião indica a Secretaria-Geral como contato para sua organização. [S04, S05]

A diligência objetiva é pedir a ata, o voto, eventuais pedidos de vista ou retirada, os resultados individuais e as inscrições para sustentação oral relativas ao item 1.1.1. Não presumir que a inclusão na pauta foi seguida de deliberação.

Contato institucional registrado no documento e na notícia oficial, `secretaria.geral@anm.gov.br`. Nenhum envio foi realizado.

## 2. A publicação de um embargo liga o número 930.096/2000 à Água Fria

No fac-símile do Diário Oficial da União de 10/04/2026, Seção 1, página 59, o Despacho Relação 12/2026 determina embargo da barragem Água Fria da Topázio Imperial. O texto identifica o processo 930.096/2000, o Auto de Embargo 13/2026/ANM/GERG e o PAS 48054.930202/2025-45. [S06]

A publicação permite ligar diretamente esses identificadores à empresa e à barragem, sem depender da reportagem que citou o inquérito da PF. Ela não identifica o ativo oferecido ao Master, a composição do grupamento ou o alcance de uma decisão judicial anterior.

O documento foi lido visualmente na quarta página do PDF, que reproduz a página impressa 59. A cópia está hospedada na ABRAPCH, não no domínio da Imprensa Nacional.

Para autenticação, o rodapé traz o código 05152026041000059. A reprodução precisa ser confrontada com a página oficial ou com o ato no processo antes de fechar a publicação.

Não foi obtido o auto integral nem eventual ato posterior de levantamento do embargo. A data do Diário não autoriza retroagir a situação a março de 2025 ou afirmar, sem os autos, que todo o empreendimento estava proibido de operar.

## 3. O que a rodada do Fable acrescentou e o que precisa de ressalva

### Cadastro das pessoas jurídicas

O arquivo `dados/receita-cnpj-quatro-empresas-2026-09-06.json` declara como origem os dados abertos do CNPJ via espelho minhareceita.org. É uma extração útil, mas não equivale a uma certidão emitida diretamente pela Receita ou pela OAB nesta apuração.

Os dados do escritório de Faria reforçam a desambiguação do CNPJ, mas a identificação da pessoa jurídica contratante ainda exige o confronto com o contrato integral. A mesma ressalva vale para afirmar que a Estabil encontrada é a beneficiária daquele acordo.

Para evitar mudança indevida no grau de certeza, utilizar a formulação consulta ao espelho de dados cadastrais, indicando sua origem. Não utilizar Receita confirmou o contrato ou certidão primária obtida quando isso não aconteceu.

### Horta como administrador não resolve o histórico societário

Na extração do Fable, Horta aparece com qualificação de administrador e campo de entrada em 18/02/2025. Essa fotografia não demonstra quando deixou ou voltou à condição de sócio, nem permite reconstruir todas as alterações da Gmais.

Ser administrador e ser sócio são qualificações diferentes no próprio arquivo. O próximo documento é a sequência de atos da JUCEMG, não outra reprodução do mesmo cadastro vigente.

### Último evento em 2007 não prova lavra parada desde 2007

O CSV do Fable registra, no processo 291701/1936, um documento diverso protocolado em 09/04/2007 no campo de último evento. Esse campo não comprova ausência de produção desde aquela data.

A expressão parada desde 2007 deve ser retirada até a obtenção de documentos de operação, suspensão ou produção. A classificação FERRO no CSV é uma pista distinta e não depende daquela inferência.

Também não foi demonstrado que toda a cobertura anterior tratava o ativo apenas como topázio. Não transformar uma busca incompleta em afirmação sobre todos os veículos.

### Parentesco não comprovado não significa parentesco refutado

O acervo não oferece comprovação da hipótese de parentesco entre Lage e Silva e Lages. A classificação correta é hipótese sem base documental descartada da pauta, não fato positivamente refutado.

## 4. Uma pista histórica adicional sobre ferro

O boletim da FIPE de outubro de 2021 inclui a Topázio Imperial com um grupamento na tabela de principais titulares de grupamentos mineiros de ferro em Minas Gerais. A tabela está na página impressa 52, terceira página do PDF, e declara adaptação do Diagnóstico do Setor Mineral de Minas Gerais de 2020 e do SIGMINE. [S07]

Esse registro histórico reforça a utilidade de investigar ferro, mas é uma compilação secundária para os dados cadastrais. Não identifica a composição do processo 930.096/2000 nem prova que a concessão 291701/1936 o integra.

O endereço do diagnóstico original foi localizado em referências bibliográficas, mas o PDF não foi recuperado dos endereços testados. A referência e os dois caminhos tentados estão registrados em S08.

## 5. Resultado dos testes de acesso

### Cadastro Mineiro e SEI da ANM

O formulário do Cadastro Mineiro abriu nesta rodada, inclusive os campos de titular e processo. A consulta exige preenchimento e código de verificação, e não foi concluída pela ferramenta de leitura. [S09]

O módulo de pesquisa pública do SEI também abriu, mas a interação necessária não foi concluída. Portanto, não é correto registrar a ANM inteira como indisponível nem afirmar que os autos foram consultados. [S10]

### TSE

As páginas dos conjuntos de dados foram localizadas, mas os arquivos eleitorais não foram baixados e processados. No teste do ZIP de 2024, a ferramenta informou tipo application/zip não suportado, diferente do bloqueio 403 relatado pelo Fable. [S11, S12]

O acesso de rede pelo ambiente local também falhou, por resolução de nomes, o que não prova indisponibilidade do TSE. Não há resultado novo sobre pagamentos, doações ou ausência deles.

### Câmara Municipal de Belo Horizonte

A relação nominal e páginas gerais de pessoal abriram, assim como o caminho para a aplicação de remuneração. A aplicação individual exige interação e verificação no navegador, e as folhas históricas não foram extraídas. [S13, S14]

Uma lista nominal atual não basta para excluir vínculo passado. Permanecem pendentes os atos de nomeação e exoneração e os demonstrativos mensais de Faria em 2021–2022 e Horta em 2025.

### Justiça Federal e TCE-MG

Os portais de consulta da Justiça Federal foram testados, mas não foi obtida a íntegra da ACP 1000752-23.2023.4.06.3822. Parte das rotas devolveu erro ou exigiu seleção e interação que não se completaram. [S15]

A peça do TCE-MG 4195237 continuou inacessível no teste, com erro 502. Trechos indexados sobre negociação ou suspensão processual não foram promovidos a fatos novos. [S16]

### Limites das cópias

Os PDFs citados foram lidos pela ferramenta web e as páginas relevantes foram conferidas visualmente. Os binários originais desses documentos não foram anexados ao pacote desta rodada.

O JSON da pauta é uma transcrição, não uma cópia integral da ANM. O script verifica consistência e comparação dos identificadores, não autenticidade dos documentos nem resultados processuais.

## 6. Como Miguel pode ajudar a destravar

### Prioridade imediata no TSE

Baixar no próprio navegador os arquivos oficiais `prestacao_de_contas_eleitorais_candidatos_2022.zip` e `prestacao_de_contas_eleitorais_candidatos_2024.zip`, pelos conjuntos S11 e S12. Enviar os arquivos aqui, mantendo nomes e origem.

Se o pacote completo for grande demais, extrair apenas os CSVs de Minas Gerais referentes a receitas, despesas contratadas e despesas pagas. Incluir o cadastro de candidatos usado para identificar Nikolas Ferreira em 2022 e Pablo Almeida em 2024.

Não converter primeiro em Excel nem enviar apenas capturas de tela. Preservar CPFs e CNPJs nos arquivos de trabalho para cruzamento, sem publicá-los indiscriminadamente no repositório público.

Os SQ_CANDIDATO 130001611005 e 130002172747 registrados pelo trabalho anterior continuam sendo identificadores a conferir no cadastro oficial. Se houver pagamentos por órgão partidário, ampliar depois a consulta às prestações dos órgãos correspondentes.

### Prioridade documental na ANM

Na consulta pública S09 e no SEI S10, recuperar primeiro o processo 930.096/2000, com composição do grupamento, substâncias, títulos integrantes e histórico. Recuperar também o 291.701/1936, com os atos de concessão, eventual incorporação ao grupamento e mudanças pertinentes.

Para o embargo, buscar o PAS 48054.930202/2025-45 e o Auto 13/2026/ANM/GERG, com fundamentação e atos posteriores. Para os recursos, buscar o processo da reunião 48051.009607/2026-23 e o resultado do item 1.1.1 da 88ª reunião.

Exportar os documentos públicos em PDF, com identificação, data e assinatura, em vez de apenas a tela inicial da pesquisa. Se o sistema negar o documento, guardar a informação sobre a restrição para formular pedido de acesso ao órgão.

### Prioridade na Justiça Federal e na CMBH

Na ACP 1000752-23.2023.4.06.3822, obter a inicial, a tutela de urgência, as decisões posteriores e os requerimentos de 2025–2026. O objetivo é delimitar o que foi proibido, em que datas e sob quais condições, sem confundir suspensão do processo com autorização para minerar.

Na CMBH, exportar as consultas históricas de Faria em 2021–2022 e de Gilberto Henrique Horta de Carvalho entre fevereiro e setembro de 2025. Procurar também os atos de nomeação e exoneração publicados no diário oficial.

A ajuda necessária são os arquivos obtidos por acesso legítimo, não credenciais, cookies, códigos de autenticação ou conteúdo protegido por segredo de justiça.

## 7. Perguntas adicionais para manifestação, ainda não enviadas

À ANM, pedir os resultados dos 90 recursos, os valores discutidos, os fundamentos, os votos e a identificação das barragens envolvidas. Pedir também a composição formal do grupamento e o auto integral do embargo publicado em abril.

À Topázio, perguntar quais títulos e substâncias integravam o negócio discutido com a Gmais, qual a situação dos recursos e o que foi exigido no embargo. Não apresentar como provada a participação de Nikolas, Faria ou Master nos procedimentos administrativos.

A Faria, Nikolas e representantes do Master, pedir documentos que identifiquem o ativo apresentado, os títulos ANM, as contrapartes e os profissionais que o avaliaram. A relação entre o ativo do áudio e o grupamento continua sendo o elo documental que falta.

À Gmais, pedir os atos históricos que expliquem a posição de Horta e a identificação completa das partes dos contratos. À Estabil, pedir a confirmação documental de sua participação e da natureza do serviço, sem presumir recebimento de comissão.

## 8. Fontes e localizadores

### S01 — Pauta da 88ª reunião da ANM

Fonte primária obtida no portal oficial, páginas 1 e 2, e metadados na página 6. Data do documento 14/08/2026, reunião prevista para 19/08/2026, consulta em 06/09/2026.

https://www.gov.br/anm/pt-br/composicao/diretoria-colegiada/reunioes-da-diretoria-colegiada/pautas-da-rop/pauta-da-88a-rop.pdf

### S02 — Certidão usada na comparação

Fonte primária já conhecida no acervo, Certidão SG-ANM 53/2025, distribuição de 26/12/2025. A base de 41 identificadores foi preservada para comparação, não reapresentada como descoberta.

https://www.gov.br/anm/pt-br/acesso-a-informacao/processos/distribuicao-de-processos-aos-diretores/documentos/2025/2025-12-26-certidao-sg-anm200b-no-53.pdf

### S03 — Coleção de atas

Página oficial consultada em 06/09/2026. Não localizar a ata da 88ª nessa listagem não prova que inexista em outro lugar ou que a reunião não tenha ocorrido.

https://www.gov.br/anm/pt-br/composicao/diretoria-colegiada/reunioes-da-diretoria-colegiada/atas-da-rop/atas-reunioes-ordinarias

### S04 — Notícia oficial da reunião

https://www.gov.br/anm/pt-br/assuntos/noticias/88a-reuniao-ordinaria-publica-da-diretoria-colegiada

### S05 — Gravação localizada, não assistida

https://www.youtube.com/watch?v=hTNOHwVJjN0

### S06 — Publicação do embargo

Ato primário em fac-símile do DOU, hospedado por terceiro. Página impressa 59, quarta página deste PDF, com conferência visual e autenticação oficial ainda pendente.

https://abrapch.org.br/wp-content/uploads/2026/04/DOU-Secao-1-n-68-10-04-26.pdf

Caminho de conferência da Imprensa Nacional, não recuperado pela ferramenta nesta rodada.

https://pesquisa.in.gov.br/imprensa/jsp/visualiza/index.jsp?data=10/04/2026&jornal=515&pagina=59

### S07 — Compilação da FIPE

Boletim de outubro de 2021, artigo Economia Mineira e os Enclaves Econômicos, tabela 1, página impressa 52. Fonte secundária dos dados cadastrais, com conferência visual da tabela.

https://downloads.fipe.org.br/publicacoes/bif/bif493-50-57.pdf

### S08 — Diagnóstico original ainda não recuperado

Endereços localizados ou testados para o Diagnóstico do Setor Mineral de Minas Gerais, de 2020. Não citar o conteúdo como lido nesta rodada.

https://www.desenvolvimento.mg.gov.br/assets/projetos/1081/130fd1adf19cc74be83c7c6c829c53b9.pdf

https://www.agenciaminas.mg.gov.br/ckeditor_assets/attachments/11205/130fd1adf19cc74be83c7c6c829c53b9.pdf

### S09 — Cadastro Mineiro

https://sistemas.anm.gov.br/SCM/site/admin/pesquisarProcessos.aspx

### S10 — Pesquisa pública SEI

https://sei.anm.gov.br/sei/modulos/pesquisa/md_pesq_processo_pesquisar.php?acao_externa=protocolo_pesquisar&acao_origem_externa=protocolo_pesquisar&id_orgao_acesso_externo=0

### S11 — Contas eleitorais de 2022

https://dadosabertos.tse.jus.br/dataset/dadosabertos-tse-jus-br-dataset-prestacao-de-contas-eleitorais-2022

https://cdn.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_de_contas_eleitorais_candidatos_2022.zip

### S12 — Contas eleitorais de 2024

https://dadosabertos.tse.jus.br/dataset/prestacao-de-contas-eleitorais-2024

https://cdn.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_de_contas_eleitorais_candidatos_2024.zip

### S13 — Relação nominal da CMBH

https://www.cmbh.mg.gov.br/transparencia/pessoal/relacao-nominal

### S14 — Aplicação de remuneração da CMBH

https://cmbhweb.cmbh.mg.gov.br/transparencia/pessoal/consulta-a-remuneracao

https://cmbhweb.cmbh.mg.gov.br/extras/remuneracao/index.php

### S15 — Justiça Federal

https://sistemas.trf6.jus.br/consultaProcessual/

https://portal.trf6.jus.br/consulta-processual/

### S16 — Peça do TCE-MG não recuperada

https://tcnotas.tce.mg.gov.br/tcjuris/Nota/BuscarArquivo/4195237

## 9. Conclusão operacional

As novidades mais firmes são a pauta com 90 recursos de fiscalização de barragem e a publicação de embargo que liga Água Fria ao processo 930.096/2000. A pauta deve ser seguida pelo resultado, e a publicação do embargo pelo auto integral e sua situação posterior.

A hipótese de ferro ganhou uma referência histórica, mas a composição do grupamento e o ativo apresentado ao Master continuam sem fechamento. Os arquivos do TSE e os documentos processuais exportados pelo navegador são a ajuda mais direta que Miguel pode fornecer para a próxima rodada.
