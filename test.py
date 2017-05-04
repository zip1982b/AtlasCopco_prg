import asyncio



async def time_consuming_computation(x):
    print('Computing {0} ** 2...'.format(x))
    await asyncio.sleep(20)
    return x ** 2



async def process_data(x):
    result = await time_consuming_computation(x)
    print('{0} ** 2 = {1}'.format(x, result))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process_data(238))
    loop.close()









    