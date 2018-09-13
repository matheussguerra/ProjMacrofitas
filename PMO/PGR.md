# Plano de Gerenciamento de Requisitos

### Controle de Versões

| Versão |    Data    |            Autores            |   Notas da Revisão    |
| :----: | :--------: | :---------------------------: | :-------------------: |
| 0.0.1  | 13/09/2018 | Lucas Guedes, Matheus Guerra, Rafael Alessandro, Vítor Yudi | Criação do PGR |

## Sumário

1. [Utilização do Repositório](#desc)
2. [Atualização de Requisitos](#req)
3. [Declaração de Escopo](#escopo)
4. [Estrutura Analítica do Projeto (EAP)](#eap)

<div id='desc' />

## Utilização do Repositório

O repositório será utilizado para implementar funcionalidades e requisitos do projeto. O controle de requisitos faltantes e já implementados serão feitos através de "issues".

A equipe de desenvolvimento utilizará a ferramenta Trello para controlar as "issues" do repositório, permitindo criação, definição de impoortância, deadline da "issue", entre outros.

<div id='req' />

## Atualização de Requisitos



<div id='escopo' />
 
## Declaração de Escopo

1. O sistema deve validar o nome das espécies da lista de entrada (1900 espécies) com base nas informações disponibilizadas em online databases (Flora do Brasil e PlantList), fornecendo o nome atualmente aceito e autor, bem como a lista de sinonímias para cada nome válido ou aceito;
2. Para cada espécie válida o sistema deve buscar e extrair das online databases os seguintes informações: ordem, classe, família, tribo, forma de vida, substrato, origem, endemismo e distribuição geográfica.
3. O sistema deve buscar os dados de ocorrência de cada espécie (para o nome aceito e suas sinonímias) nas plataformas Specieslink e GBIF;
4. O sistema deve executar um processo de triagem dos dados de ocorrências disponibilizados pelo GBIF e Specieslink de modo a corrigir nomes duplicados, erros de digitação, coordenadas ausentes, registros de grupos não plantas (ex. peixes, insetos, répteis, etc), entre outras inconsistências. 
5. O sistema deverá fornecer gráficos/tabelas/mapas com as principais tendências dos dados entre as 14 grandes bacias Sul-Americanas e do continente como um todo, como por exemplo, número de espécies de macrófitas por bacia, família mais especiosa, família mais amplamente distribuída, etc. 

<div id='eap' />

## Estrutura Analítica do Projeto (EAP)


