import asyncio
import time

async def main():
    print('tim')
    task = asyncio.create_task(fow("randome things text"))
    # If we would remove the await task ,It would run immediately but we will not get line 14. 
    await task
    print('finished')

async def fow(text):
    print(f'{text}')
    await asyncio.sleep(2)
    print('we wated for one sec of sleep')
    



start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
