import asyncio
import aiosqlite


async def async_fetch_users(db_name):
    """Fetch all users from the database."""
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()


async def async_fetch_older_users(db_name):
    """Fetch users older than 40 from the database."""
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()


async def fetch_concurrently():
    """Run both queries concurrently."""
    db_name = "User_data.db"
    results = await asyncio.gather(
        async_fetch_users(db_name), async_fetch_older_users(db_name)
    )
    all_users, older_users = results
    print("All Users:", all_users)
    print("Users older than 40:", older_users)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
