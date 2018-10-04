# Plano de Gerenciamento de Requisitos

### Controle de Versões

| Versão |    Data    |            Autores            |   Notas da Revisão    |
| :----: | :--------: | :---------------------------: | :-------------------: |
| 0.0.1  | 13/09/2018 | Lucas Guedes, Matheus Guerra, Rafael Alessandro, Vítor Yudi | Criação do PGR |
| 0.1.0  |27/09/2018  | Lucas, Rafael                                      | Correção do EAP|
| 0.1.1  |28/09/2018  | Matheus                                      | Seqência de tarefas|

## Sumário

1. [Utilização do Repositório](#desc)
2. [Atualização de Requisitos](#req)
3. [Declaração de Escopo](#escopo)
4. [Estrutura Analítica do Projeto (EAP)](#eap)
5. [Sequenciamento de Tarefas](#seq)

<div id='desc' />

## Utilização do Repositório
<div id='desc' />
O repositório será utilizado para implementar funcionalidades e requisitos do projeto. O controle de requisitos faltantes e já implementados serão feitos através de "issues".

A equipe de desenvolvimento utilizará a ferramenta Trello para controlar as "issues" do repositório, permitindo criação, definição de impoortância, deadline da "issue", entre outros.



## Atualização de Requisitos
<div id='req' />
Durante o projeto novos requisitos podem ser adicionados com a devida aprovação dos Stakeholders e do gerrente de projeto.


 
## Declaração de Escopo
<div id='escopo' />

1. O sistema deve validar o nome das espécies da lista de entrada (1900 espécies) com base nas informações disponibilizadas em online databases (Flora do Brasil e PlantList), fornecendo o nome atualmente aceito e autor, bem como a lista de sinonímias para cada nome válido ou aceito;
2. Para cada espécie válida o sistema deve buscar e extrair das online databases os seguintes informações: ordem, classe, família, tribo, forma de vida, substrato, origem, endemismo e distribuição geográfica.
3. O sistema deve buscar os dados de ocorrência de cada espécie (para o nome aceito e suas sinonímias) nas plataformas Specieslink e GBIF;
4. O sistema deve executar um processo de triagem dos dados de ocorrências disponibilizados pelo GBIF e Specieslink de modo a corrigir nomes duplicados, erros de digitação, coordenadas ausentes, registros de grupos não plantas (ex. peixes, insetos, répteis, etc), entre outras inconsistências. 
5. O sistema deverá fornecer gráficos/tabelas/mapas com as principais tendências dos dados entre as 14 grandes bacias Sul-Americanas e do continente como um todo, como por exemplo, número de espécies de macrófitas por bacia, família mais especiosa, família mais amplamente distribuída, etc. 


## Estrutura Analítica do Projeto (EAP)
<div id='eap' />

1. Entrega
   * PMO
      * TAP
      * PGR
2. Entrega
   * Validação de Espécies
      * Pré processamento de dados da base cedida
      * Verificação da lista de nomes de espécies e autores
      * Extração de dados das online databases (Flora do Brasil e PlantList)
      * Estruturação dos dados das online databases
      * Verificar/modificar nomes na base cedida com os nomes dos dados estruturados
   * Elaborar testes unitários
   * Aplicar testes unitários
3. Entrega
   * Busca de Ocorrências de espécies
      * Extração de dados das online databases (GBIF e Specieslink)
   * Triagem dos dados
      * Correção de nomes inválidos
      * Correção de incoerências
   * Elaborar testes unitários
   * Aplicar testes unitários
4. Entrega
   * Saidas
      * Gráficos
      * Mapas
      * Tabela
   * Elaborar testes unitários
   * Aplicar testes unitários
   * Termo de Finalização de projeto
   
   
## Sequenciamento de Tarefas
<div id='seq' />

<p>O sequenciamento de tarefas é apresentado atráves do gerenciador de projetos Waffle. O projeto pode ser acessado através do link: https://waffle.io/GuerraUTFPR/ProjEng2 </p>.
