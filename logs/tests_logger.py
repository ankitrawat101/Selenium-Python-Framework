import logging

logger = logging.getLogger("Tests logs")
handler = logging.FileHandler("tests_logs.log")
log_formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
handler.setFormatter(log_formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


