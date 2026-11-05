from datetime import datetime
from decorator_tempo import medir_tempo
import pandas as pd
from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    text,
)

# Conexão com o banco de dados 
engine = create_engine(
    'postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2',
    echo=False,
)
metadata = MetaData()

usuarios = Table(
    'usuarios',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False, index=True),
    Column('cpf', String(14), nullable=False),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column(
        'updated_on',
        DateTime(),
        default=datetime.now,
        onupdate=datetime.now,
    ),
)


# ==========================================
# ATIVIDADE 1: Função de Anonimização
# ==========================================
def LGPD(row):
  # Compatível com pandas Series ou SQLAlchemy Row
  if hasattr(row, 'to_dict'):
    row_dict = row.to_dict()
  else:
    row_dict = dict(row._mapping)

  # 1. Nome: Mantém a primeira letra e troca o restante por '*'
  nome_original = str(row_dict['nome'])
  partes_nome = nome_original.split(' ')
  nome_anonimizado = []
  for parte in partes_nome:
    if len(parte) > 0:
      primeira = parte[0]
      resto = '*' * (len(parte) - 1)
      nome_anonimizado.append(primeira + resto)
  row_dict['nome'] = ' '.join(nome_anonimizado)

  # 2. CPF: Substitui os últimos caracteres por '*' (ex: 237.*** ***-**)
  cpf_original = str(row_dict['cpf'])
  row_dict['cpf'] = (
      cpf_original[:4] + '*** ***-**'
      if len(cpf_original) >= 14
      else '***.***.***-**'
  )

  # 3. E-mail: Substitui os caracteres antes do '@' por '*'
  email_original = str(row_dict['email'])
  if '@' in email_original:
    usuario_email, dominio = email_original.split('@', 1)
    row_dict['email'] = (
        usuario_email[0] + '*' * (len(usuario_email) - 1) + '@' + dominio
    )

  # 4. Telefone: Apresenta somente o final (ex: 6810)
  tel_original = str(row_dict['telefone'])
  digitos_tel = ''.join(filter(str.isdigit, tel_original))
  row_dict['telefone'] = (
      digitos_tel[-4:] if len(digitos_tel) >= 4 else tel_original
  )

  return row_dict


# ==========================================
# ATIVIDADE 2: Geração de arquivos por Ano
# ==========================================
@medir_tempo
def processar_atividade_2(df):
  # Converte a coluna para datetime caso venha como texto/objeto
  df['data_nascimento'] = pd.to_datetime(df['data_nascimento'])
  anos = df['data_nascimento'].dt.year.unique()

  for ano in anos:
    df_ano = df[df['data_nascimento'].dt.year == ano]
    dados_anonimizados = [LGPD(row) for _, row in df_ano.iterrows()]
    df_exportar = pd.DataFrame(dados_anonimizados)

    nome_arquivo = f'{int(ano)}.xlsx'
    df_exportar.to_excel(nome_arquivo, index=False)
    print(f'Arquivo gerado: {nome_arquivo}')


# ==========================================
# ATIVIDADE 3: Arquivo consolidado (Sem Anonimização)[cite: 4]
# ==========================================
@medir_tempo
def processar_atividade_3(df):
  df_todos = df[['nome', 'cpf']].copy()
  df_todos.to_excel('todos.xlsx', index=False)
  print('Arquivo consolidado gerado: todos.xlsx')


# ==========================================
# Execução Principal
# ==========================================
if __name__ == '__main__':
  with engine.connect() as conn:
    query = text('SELECT * FROM usuarios;')
    df_usuarios = pd.read_sql(query, conn)

  print('--- Executando Atividade 2 (Por Ano com Anonimização) ---')
  processar_atividade_2(df_usuarios)

  print('\n--- Executando Atividade 3 (Consolidado Nome e CPF) ---')
  processar_atividade_3(df_usuarios)