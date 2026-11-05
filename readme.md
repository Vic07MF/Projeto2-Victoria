# Mini Projeto 2: Lei Geral de Proteção de Dados (LGPD)

Repositório desenvolvido para a atividade acadêmica da Fatec Rio Claro, focado na aplicação prática de regras de anonimização de dados, manipulação de banco de dados e medição de desempenho em Python em conformidade com a Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018).

---

## 🛠️ Tecnologias e Dependências

O projeto utiliza as seguintes bibliotecas Python:
* **SQLAlchemy** (ORM e conexão com o banco de dados PostgreSQL)
* **Pandas** (Manipulação e exportação de dados)
* **Psycopg2-binary** (Driver de conexão PostgreSQL)
* **Openpyxl** (Manipulação de arquivos Excel `.xlsx`)

Para instalar todas as dependências necessárias, execute:
```bash
pip install -r requirements.txt
```

---

## 📂 Estrutura do Projeto

* `LGPD.py`: Script principal que realiza a conexão com o banco de dados, executa as regras de anonimização (Atividade 1), gera os arquivos por ano de nascimento (Atividade 2) e o relatório consolidado de nomes e CPFs (Atividade 3).
* `decorator_tempo.py`: Módulo contendo o decorador customizado responsável por mensurar o tempo de execução e registrar logs de performance (Atividade 4).
* `requirements.txt`: Lista de dependências e bibliotecas do projeto.
* `Atividade_LGPD.pdf`: Documento original com as diretrizes e regras do mini projeto.

---

## 🚀 Como Executar

1. Certifique-se de que possui as dependências instaladas:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script principal no terminal:
   ```bash
   py LGPD.py
   ```

---

## 📋 Descrição das Atividades

1. **Atividade 1 (Anonimização):** Ajuste da função `LGPD(row)` para mascarar os campos sensíveis:
   * **Nome:** Mantém apenas a primeira letra de cada parte do nome e substitui o restante por asteriscos (`*`).
   * **CPF:** Preserva os primeiros dígitos e mascara os demais (`237.*** ***-**`).
   * **E-mail:** Oculta os caracteres antes do símbolo `@` (`n*********@example.com`).
   * **Telefone:** Exibe apenas os últimos dígitos correspondentes ao final do número.
2. **Atividade 2 (Arquivos por Ano):** Filtra e agrupa os registros por ano de nascimento, aplicando a anonimização e gerando dinamicamente planilhas individuais (ex: `1990.xlsx`, `1991.xlsx`).
3. **Atividade 3 (Relatório Consolidado):** Gera um arquivo consolidado (`todos.xlsx`) contendo todos os registros da base, restrito estritamente às colunas **nome** e **CPF**, **sem anonimização**.
4. **Atividade 4 (Métricas e Logs):** Utilização de um decorador isolado (`decorator_tempo.py`) para capturar o tempo de execução das rotinas e registrar as informações em um arquivo de log persistente (`execucao_atividades.log`).
