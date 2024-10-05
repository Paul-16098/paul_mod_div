import asyncio
import httpx
from src.core import GameSourceCode


async def main():
    async with httpx.AsyncClient() as client:
        game = GameSourceCode(client)
        await game.get_latest_commit()  # Judging whether download or not
        await game.download()
    game.extract()

if __name__ == '__main__':
    asyncio.run(main())