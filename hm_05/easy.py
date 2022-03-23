import aiohttp
import asyncio
import os
import aiofiles

async def downloadPicture(url) -> bytes:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def writeToFile(el):
    pic = await downloadPicture(el[0])
    if not os.path.exists(el[2]):
        os.makedirs(el[2])
    # lock when writing to file ?
    f = await aiofiles.open(el[2] + "/picture" + str(el[1]) + ".png", 'wb')
    await f.write(pic)
    await f.close()


async def run():
    count = input()
    dirr = input()
    url = 'https://picsum.photos/200/300'
    urls = [[url, i, dirr] for i in range(int(count))]
    await asyncio.wait(map(writeToFile, urls))


if __name__ == '__main__':
    asyncio.run(run())

