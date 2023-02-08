from loguru import logger 

logger.add("logger/log.log", format='{time}|||{message}')