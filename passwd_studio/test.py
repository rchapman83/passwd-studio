# -*- coding: utf-8 -*-
# Entry point to bring up the web app

# from os import environ
import os, logging, logging.config, timber


# Timber api token and source id
t = os.environ.get('TIMBER_TOKEN')
s = os.environ.get('TIMBER_ID')

log_format = '%(asctime)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=log_format)
timber_handler = timber.TimberHandler(source_id=s, api_key=t, level=logging.INFO, buffer_capacity=20, flush_interval=60, raise_exceptions=True)
logger.addHandler(timber_handler)

def test():
    result = 'Did you get those logs? hope so'
    print('Testing logging handlers')
    logger.info('log level info')
    logger.debug('debug mode')
    logger.error('ERROR...')
    logger.critical('Crit hit')
    return result

if __name__ == '__main__':
    print(test())


 