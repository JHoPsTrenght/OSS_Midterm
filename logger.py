import logging

Suc_logger = logging.getLogger("succeed")
Suc_logger.setLevel(logging.DEBUG) # 모든 레벨의 로그를 Handler들에게 전달해야 합니다.
Err_logger = logging.getLogger("error")
formatter = logging.Formatter('[%(asctime)s] %(message)s', '%Y-%m-%d %H:%M:%S')

# DEBUG 레벨 이상의 로그를 `debug.log`에 출력하는 Handler
file_debug_handler = logging.FileHandler('debug.log')
file_debug_handler.setLevel(logging.DEBUG)
file_debug_handler.setFormatter(formatter)
Suc_logger.addHandler(file_debug_handler)

# ERROR 레벨 이상의 로그를 `error.log`에 출력하는 Handler
file_error_handler = logging.FileHandler('error.log')
file_error_handler.setLevel(logging.ERROR)
file_error_handler.setFormatter(formatter)
Err_logger.addHandler(file_error_handler)

def error(str):
    Err_logger.error(str)

def succeed(str):
    Suc_logger.debug(str)