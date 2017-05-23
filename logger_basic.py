import logging
var1=5
var2='Our number'
logging.basicConfig(filename='example.log', format=("%(levelname)s:%(message)s:%(asctime)s"), filemode='w', level=logging.DEBUG)  #filemode='w' - лог пишется каждый раз заново(не добавляется), root не будет
logging.debug("this message should go to the log file")
logging.info("So should this")
logging.warning("and this too")




# отображение переменных в логе
logging.warning('%s before you %s', 'Look', 'leap!')
logging.warning('%s this is %s', var1, var2)
print(__name__)