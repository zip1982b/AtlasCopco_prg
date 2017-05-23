import logging

#create logger
testLogger = logging.getLogger("simple_example")
print(testLogger.name) #class logging.Logger
testLogger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
testLogger.addHandler(ch)

# 'application' code
testLogger.debug('debug message')
testLogger.info('info message')
testLogger.warn('warn message')
testLogger.error('error message')
testLogger.critical('critical message')


