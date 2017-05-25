
def fetcher(obj, index):
    return obj[index]

x = 'spam'
try:
    print(fetcher(x, 4))
except IndexError:
    print('got exception')

