from functools import wraps
import logging
import time

# Configuração do sistema de Logs para gravar em arquivo
logging.basicConfig(
    filename='execucao_atividades.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
)


def medir_tempo(func):
  """Decorator que mede o tempo de execução de uma função,

  imprime no console e grava em log (Atividade 4).
  """

  @wraps(func)
  def wrapper(*args, **kwargs):
    inicio = time.perf_counter()
    resultado = func(*args, **kwargs)
    fim = time.perf_counter()
    duracao = fim - inicio

    mensagem = (
        f"⏱ Função '{func.__name__}' executada em {duracao:.6f} segundos."
    )
    print(mensagem)
    logging.info(mensagem)

    return resultado

  return wrapper