# Prompt para o GPT, rodada 3

Continue a apuração da parte 2 da reportagem do Cafezinho sobre Nikolas Ferreira, Daniel Vorcaro e Thiago Rodrigues de Faria. O material das rodadas anteriores está na branch `master`:

https://github.com/migueldorosario1/cafezinho/tree/master/pesquisas/nikolas-vorcaro-faria

Leia nesta ordem: `README.md`, `relatorio-fable-continuidade-2026-09-06.md`, `tese-e-esqueleto-parte-2.md`, seção 10 do `briefing-continuidade-caso-faria-gmais.md`. Os dados brutos estão em `dados/` e os scripts em `scripts/`.

O Fable confirmou em fonte primária: o CNPJ do escritório de Faria (aberto em 19/08/2024, Nova Lima), a entrada de Gilberto Horta como administrador da Gmais em 18/02/2025, os dez títulos da Topázio Imperial na ANM (incluindo uma concessão de lavra de ferro, 291701/1936), a certidão dos 41 recursos distribuídos a Mauro Sousa, e o número do ativo negociado segundo a PF (grupamento 930.096/2000). Não repita isso.

O Fable não conseguiu acessar, por bloqueio de rede: TSE (403), SCM da ANM (503), CMBH e PJe do TRF6. Você parece ter conseguido abrir fontes que ele não abriu. Concentre-se nelas.

## Prioridade 1. Grupamento 930.096/2000
No SCM da ANM (https://sistemas.anm.gov.br/SCM/site/admin/dadosProcesso.aspx) ou no Cadastro Mineiro, obtenha a composição do grupamento mineiro 930.096/2000 da Topázio Imperial. A pergunta decisiva é uma só: o processo 291701/1936 (ferro) faz parte desse grupamento? Registre também titular, fase, substâncias e eventos de 2024 a 2026 (cessões, procurações, pedidos de retomada). Se conseguir, abra também o processo 291701/1936 e liste os eventos após 2007.

## Prioridade 2. Os 41 recursos
Na pesquisa pública do SEI da ANM (https://sei.anm.gov.br/sei/modulos/pesquisa/md_pesq_processo_pesquisar.php), abra pelo menos dez dos 41 números listados na seção 8 do briefing. Para cada um: auto de infração, valor, fundamento, data, procurador da Topázio, e se houve decisão após 26/12/2025. Anote se algum procurador é Faria, Horta, Gmais ou escritório ligado a eles.

## Prioridade 3. TSE
Baixe as bases de 2022 e 2024 e faça o cruzamento descrito na seção 4 do relatório do Fable. Faria só tem CNPJ desde agosto de 2024, então em 2022 procure-o como pessoa física. Registre filtros, versão dos arquivos e resultado, inclusive negativo.

## Prioridade 4. JUCEMG
Obtenha a ficha cadastral completa da Gmais Ambiental (CNPJ 41.332.820/0001-68) com histórico de alterações societárias. Queremos saber se Horta saiu e voltou, e a data exata de cada movimento.

## Prioridade 5. ACP 1000752-23.2023.4.06.3822
No PJe do TRF6, obtenha a decisão de tutela de urgência, a data, o juízo e qualquer petição de 2025 ou 2026 pedindo retomada ou descaracterização.

## Prioridade 6. CMBH
No portal de transparência da Câmara Municipal de Belo Horizonte, date o período de Faria como assessor de Nikolas vereador (2021 a 2022) e o de Horta no gabinete de Uner Augusto (2025), com cargo e remuneração.

## Regras
Para cada achado, registre afirmação exata, URL, data do documento, data de consulta, página ou trecho, e o limite da conclusão. Separe confirmado, atribuído e pendente. Não trate resposta de IA como fonte. Não presuma crime. Não envie pedidos de manifestação, as perguntas já estão prontas na seção 5 do relatório do Fable e o envio é decisão do editor.

Ao terminar, grave um arquivo `relatorio-gpt-rodada-3-<data>.md` na mesma pasta, atualize `fontes-consultadas.md` e informe os commits.
