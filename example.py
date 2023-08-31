import aiohttp
import asyncio

SERVER_URL = "http://127.0.0.1:8001"
MAX_WAIT_TIME = 120  # in seconds
POLL_INTERVAL = 1  # in seconds

async def check_server_status():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{SERVER_URL}/check_status") as response:
            return await response.json()

async def swap_image(image_path, target_image_path, custom_strings):
    data = aiohttp.FormData()
    data.add_field('image', open(image_path, 'rb'))
    data.add_field('target_image', open(target_image_path, 'rb'))
    data.add_field('custom_strings', custom_strings)

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{SERVER_URL}/swap_image", data=data) as response:
            return await response.json()

async def swap_video(image_path, target_image_path, custom_strings):
    data = aiohttp.FormData()
    data.add_field('image', open(image_path, 'rb'))
    data.add_field('target_video', open(target_image_path, 'rb'))
    data.add_field('custom_strings', custom_strings)

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{SERVER_URL}/swap_video", data=data) as response:
            return await response.json()

async def check_task_status(task_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{SERVER_URL}/check_task_status/{task_id}") as response:
            return await response.json()

async def main():
    # Checking server status
    status = await check_server_status()
    print("Server Status:", status)

    # Swapping image
    #result = await swap_video('path_to_image.jpg', 'path_to_video.mp4', 'demo_string')
    result = await swap_image('path_to_image.jpg', 'path_to_target_image.jpg', 'demo_string')
    task_id = result.get("task_id")
    print("Task ID", task_id)

    # Polling for task status
    elapsed_time = 0
    while elapsed_time < MAX_WAIT_TIME:
        task_status = await check_task_status(task_id)
        if task_status.get("status") == "completed":
            print("Task Completed!", task_status)
            break

        print("Task Pending", task_status)
        await asyncio.sleep(POLL_INTERVAL)
        elapsed_time += POLL_INTERVAL

    if elapsed_time >= MAX_WAIT_TIME:
        print("Maximum wait time reached. Task might not be completed yet.")

if __name__ == "__main__":
    asyncio.run(main())
