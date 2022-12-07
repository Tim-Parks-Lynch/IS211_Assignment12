import logging


def create_logger(logger_name, output_file, message):
    # Create custom logger
    logger = logging.getLogger(logger_name)

    # Create handler
    file_handler = logging.FileHandler(output_file)

    # Set level
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(file_handler)
    logger.error(message)
