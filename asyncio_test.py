import asyncio
import time

async def main():
    print('tim')
    task = asyncio.create_task(fow("randome things text"))
    await task
    print('finished')

async def fow(text):
    print(f'{text}')
    await asyncio.sleep(1)
    print('we wated for one sec of sleep')
    



start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
