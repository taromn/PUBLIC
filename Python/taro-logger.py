
import logging
import time
import sys
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

format_a = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

# stdout
handler_std = logging.StreamHandler(sys.stdout)
handler_std.setLevel(logging.DEBUG)
handler_std.setFormatter(format_a)
logger.addHandler(handler_std)

# file out, rotation
handler_rot = RotatingFileHandler(
  'output.log',
  maxBytes=10*1024,
  backupCount=2,
  encoding='utf-8'
)
handler_rot.setFormatter(format_a)
logger.addHandler(handler_rot)

logger.setLevel(logging.DEBUG)

def log_out(number):
  logger.debug(f'log count:{number}')
  logger.info(f'log count:{number}')
  logger.warning(f'log count:{number}')
  logger.error(f'log count:{number}')


if __name__ == "__main__":
  i = 0
  while True:
    log_out(i)
    time.sleep(1)
    i = i + 1


# Reference
# https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log-file
# https://docs.python.org/3/howto/logging.html
# https://www.datadoghq.com/blog/python-logging-best-practices/
