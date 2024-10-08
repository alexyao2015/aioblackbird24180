"""Simple example to demonstrate the library."""

import asyncio

from aioblackbird24180 import Blackbird24180


async def main():
    blackbird = Blackbird24180("localhost", 80)
    status = await blackbird.get_matrix()
    print(status.get_output(1))
    for i in range(1, 10):
        await blackbird.set_output(i, 2)
    await asyncio.sleep(1)
    status = await blackbird.get_matrix()
    print(status.matrix_output)
    for i in range(1, 10):
        await blackbird.set_output(i, 1)
    await asyncio.sleep(1)
    status = await blackbird.get_matrix()
    print(status.matrix_output)


asyncio.run(main())
