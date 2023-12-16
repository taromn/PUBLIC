
import logging
import time

logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.WARN)

def log_out(number):
  logging.debug(f'DEBUG log count:{number}')
  logging.info(f'INFO log count:{number}')
  logging.warning(f'WARN log count:{number}')
  logging.error(f'ERROR log count:{number}')


if __name__ == "__main__":
  for i in range(100):
    log_out(i)
    time.sleep(1)
