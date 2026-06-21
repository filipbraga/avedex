# AveDex

Catálogo interativo de aves desenvolvido na disciplina **Boas Práticas de Programação** (IFMG - Campus Ouro Preto).

## Funcionalidades atuais

- Menu principal com opções de interação
- Mensagem de boas-vindas personalizada
- Listagem de aves cadastradas
- Consulta de detalhes de uma ave pelo código
- Informações sobre o projeto
- Tratamento de opções inválidas
- Encerramento seguro do programa

## Estrutura do código

- **Lista de dicionários**: cada ave é representada por um dicionário com as mesmas chaves (`codigo`, `nome_popular`, `nome_cientifico`, `habitat`, `alimentacao`, `curiosidade`).
- **Funções**: cada responsabilidade está separada em funções (`listar_aves`, `buscar_ave_por_codigo`, `exibir_detalhes`, etc.).
- **Parâmetros**: funções recebem os dados necessários por parâmetro, evitando dependência de variáveis globais.
- **Commits**: evolução registrada passo a passo no GitHub.

## Como executar

```bash
python avedex.py
