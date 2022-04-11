import logging



def get_logger(logger,level,message):
    
    if level == "warning":
    
        logger.warning(message)
    elif level == "info":
        logger.info(message)
        
    elif level == "error":
        logger.error(message)
        

    
