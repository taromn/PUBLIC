
import logging
import time
import sys

logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

def log_out(number):
  logger.debug(f'log count:{number}')
  logger.info(f'log count:{number}')
  logger.warning(f'log count:{number}')
  logger.error(f'log count:{number}')


if __name__ == "__main__":
  for i in range(100):
    log_out(i)
    time.sleep(1)


# Reference
# https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log-file
# https://docs.python.org/3/howto/logging.html
# https://www.datadoghq.com/blog/python-logging-best-practices/
