import asyncio

from minter import minter


async def main() -> None:
    await minter()


if __name__ == "__main__":
    asyncio.run(main=main())
