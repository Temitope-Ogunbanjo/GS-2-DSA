# Módulo de Gerenciamento de Registros

Sistema em Python para gerenciar registros utilizando estrutura de Lista Encadeada e persistência em JSON.

## Integrantes
* **Temitope Kuku da Silva Ogunbanjo** — RM: 573772
* **Gustavo de Souza Abreu** — RM: 574080
* **Gabriel Oliveira Gusmãos Florencio dos Santos** — RM: 573747

## O que foi feito
* **Estrutura de Dados Customizada (`Node`):** Criação de nós encadeados para armazenar os registros em memória (`Id`, `Titulo`, `Categoria`, `Descricao`, `PublicoAlvo`, `Canal` e `LocalAtendimento`).
* **Operações CRUD via Menu Interativo:** Implementação de cadastro, listagem, exibição detalhada, atualização e exclusão de registros diretamente pelo terminal.
* **Busca e Ordenação:** Implementação de busca linear (`Pesquisar`) por ID ou atributos e ordenação por inserção (`Ordenar`) em ordem numérica ou alfabética.
* **Persistência em JSON:** Carregamento inicial via `appsettings.json` e serialização automática da estrutura encadeada para `Tree.json` e `Id.json`.
