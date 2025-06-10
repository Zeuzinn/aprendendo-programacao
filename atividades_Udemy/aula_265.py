import asyncio

async def task():
    print('Task started')
    await asyncio.sleep(1)
    print('Task finished')

async def main():
    await asyncio.gather(task(), task())

asyncio.run(main())
