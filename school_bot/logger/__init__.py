from loguru import logger 

logger.add("log.log", format='{time}|||{message}')