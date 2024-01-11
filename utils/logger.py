# Imports the Google Cloud client library
def get_logger ():
    from google.cloud import logging

    # Instantiates a client
    logging_client = logging.Client()

    # The name of the log to write to
    log_name = "workbench-log"
    # Selects the log to write to
    logger = logging_client.logger(log_name)
    return logger