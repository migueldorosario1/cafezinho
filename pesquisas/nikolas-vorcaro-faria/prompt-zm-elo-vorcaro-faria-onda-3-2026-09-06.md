# Próxima diligência ZM para o elo Faria e Vorcaro

ZM, trabalhe em `migueldorosario1/cafezinho`, branch `master`, somente na pasta `pesquisas/nikolas-vorcaro-faria/`. Leia o README, a auditoria anterior e `elo-vorcaro-faria-mineracao-onda-3-2026-09-06.md`, que discrimina os links e as limitações desta rodada.

O objetivo é identificar quem recebeu a proposta de Faria e qual pessoa jurídica avaliava o ativo. Não ampliar um mapa de associações sem fechar documentos, datas e papéis.

## 1. Destinatários da proposta

Localize a nota de Faria reproduzida por O Fator em 03/09/2026 e preserve uma captura identificada. Ele reconheceu apresentação a Vorcaro e aos advogados dele e afirmou que as tratativas terminaram sem avançar.

Busque nos documentos públicos a proposta, correspondência ou procuração que identifique esses advogados, o cliente representado, a data e o título minerário. Não escolha os defensores criminais atuais como destinatários presumidos de uma negociação de 2025.

Há comunicado próprio do Azevedo Sette de 14/11/2024 sobre assessoria na aquisição da Itaminas, e uma publicação do escritório descreve os acionistas assessorados como Ageo e AVG. Esse é um interlocutor possível, não prova de que recebeu a proposta de Faria.

The Latin American Lawyer descreveu em 10/06/2025 a assessoria do BMA à Prisma no financiamento da Itaminas. A escritura de debêntures e as garantias são documentos a recuperar, sem confundir assessor do financiador com advogado de Vorcaro.

Não envie perguntas em nome de Miguel sem autorização específica. Prepare perguntas objetivas e registre eventuais negativas ou elementos que refutem a hipótese.

## 2. Novo alvo documental na CVM

Recupere as demonstrações e os informes do Itaminas FIP Multiestratégia, CNPJ 53.263.484/0001-28, administradora CBSF Trust, CNPJ 23.863.529/0001-34. Os localizadores de participante são 239948, tipo 73, e 257992, tipo 68, listados com URLs no relatório.

O informe que o GPT conseguiu abrir foi enviado em setembro de 2024 e tem um cotista do tipo outros fundos. Não transportar esse registro para março de 2025, nem afirmar o beneficiário final a partir da categoria do cotista.

Obtenha a competência, as notas, os percentuais e as pessoas jurídicas acima e abaixo do fundo em 2024–2025. Confira a escritura do financiamento da Itaminas e os atos da RDA, sem atribuir a Faria participação nessa operação sem documento.

## 3. Busca inversa de cotistas

Baixe do diretório oficial https://dados.cvm.gov.br/dados/FI/DOC/CDA/DADOS/ os arquivos de dezembro de 2024, fevereiro, março, abril, julho e agosto de 2025. Analise o bloco 2, cotas de fundos, procurando como INVESTIDOS os CNPJs do Victoria Falls e do FIP Itaminas.

O script `scripts/rastrear_cotistas_victoria_falls_cda.py` já está salvo. Ele foi testado somente com dados sintéticos, e o GPT não conseguiu baixar as bases reais por falha DNS do ambiente.

Exemplos de execução, a partir da pasta da pesquisa e com os ZIPs públicos baixados em `bases/`.

```bash
python scripts/rastrear_cotistas_victoria_falls_cda.py bases/*.zip --cnpj 10566011000197 --saida resultado_cotistas_victoria_falls.json
python scripts/rastrear_cotistas_victoria_falls_cda.py bases/*.zip --cnpj 53263484000128 --saida resultado_cotistas_itaminas.json
```

Confira o dicionário vigente, os cabeçalhos e a codificação. Se necessário, use `--encoding latin-1`, mas registre a opção e não ignore erros de leitura.

Os campos de CNPJ do declarante e do ativo são diferentes. Preserve linha, membro do ZIP, competência e SHA-256, e verifique manualmente qualquer correspondência antes de seguir a cadeia para o fundo superior.

Uma consulta sem correspondências não prova ausência de cotista. Verifique cobertura, dados confidenciais, retificações e mudanças de fundo para classe, sem contornar restrições.

## 4. Contratos anteriores AVG e Cedro

Os últimos parágrafos da reportagem do Estado de Minas de 18/09/2025 mencionam tratativas Brava–AVG e uma negociação frustrada com a Cedro. Busque os documentos públicos correspondentes, sem assumir que o objeto era a Topázio.

A Investigação descreve uma visita de Teixeira à Cedro e um procedimento preliminar arquivado em outubro de 2023. Preserve as versões divergentes e o arquivamento, e confira a data no original porque a matéria usa dias diferentes.

Cruze os títulos e as pessoas jurídicas dos contratos com os processos 930.096/2000 e 291.701/1936. A participação posterior de um grupo em operação com Vorcaro não o coloca automaticamente em todas as tratativas anteriores.

## 5. Preservação e entrega

Salve documentos e extrações em uma nova subpasta identificada, sem substituir originais anteriores. Registre URL, data de obtenção com fuso, competência, página, SHA-256 e se o arquivo é original, impressão ou transcrição.

Não é necessário pedir novamente o DOU de abril de 2026 já preservado na rodada ZM anterior. As prioridades são os destinatários da proposta, o FIP Itaminas, os cotistas superiores e os contratos mencionados.

Não publique credenciais ou dados pessoais desnecessários e não tente acesso a peças sigilosas sem autorização legítima. Ao encerrar, informe quais conexões foram comprovadas, quais foram refutadas e os commits efetivamente gravados.
