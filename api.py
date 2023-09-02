from fastapi import FastAPI, UploadFile, HTTPException, Depends, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from typing import Union
import asyncio
import uuid
import os

app = FastAPI()

# Mount the static directory for serving files
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory task database
tasks = {}

@app.get("/check_status")
async def check_status():
    return {"status": "running"}

@app.post("/swap_image")
async def swap_image(image: UploadFile = None, target_image: UploadFile = None, custom_strings: str = "demo"):
    if not image or not target_image:
        raise HTTPException(status_code=400, detail="Both image and target_image are required.")
    
    task_id = str(uuid.uuid4())
    tasks[task_id] = {"status": "processing"}
    
    asyncio.create_task(process_swap_image(task_id, image, target_image, custom_strings))
    
    return {"task_id": task_id}

@app.post("/swap_video")
async def swap_video(image: UploadFile = None, target_video: UploadFile = None, custom_strings: str = "demo"):
    if not image or not target_video:
        raise HTTPException(status_code=400, detail="Both image and target_video are required.")
    
    task_id = str(uuid.uuid4())
    tasks[task_id] = {"status": "processing"}
    
    asyncio.create_task(process_swap_video(task_id, image, target_video, custom_strings))
    
    return {"task_id": task_id}

@app.get("/check_task_status/{task_id}")
async def check_task_status(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found.")
    return tasks[task_id]

async def save_file(file, filename: str):
    with open(os.path.join("static", filename), "wb") as buffer:
        contents = file.read()  # Read the file contents directly from the buffer
        buffer.write(contents)

async def process_swap_image(task_id, image, target_image, custom_strings):
    swapped_img_filename = str(uuid.uuid4()) + '.jpg'

    # This will be replaced later on

    # swapped_image = await some_aiprocess_image(image, target_image, custom_strings) #actual function # return BufferedReader
    swapped_image = open("aidemo/demo.jpg", "rb") # demo
    await asyncio.sleep(10) #Asssume delay for demo

    # END


    await save_file(file=swapped_image, filename=swapped_img_filename)  # Mock saving the processed image
    tasks[task_id]["status"] = "completed"
    tasks[task_id]["result"] = f"Face swapped and saved as {swapped_img_filename}"
    tasks[task_id]["link"] = f"/static/{swapped_img_filename}"

async def process_swap_video(task_id, image, target_video, custom_strings):
    swapped_mp4 = str(uuid.uuid4()) + '.mp4'

    # This will be replaced later on

    # swapped_video = await some_aiprocess_video(image, target_video, custom_strings) #actual function # return BufferedReader
    swapped_video = open("aidemo/demo.mp4", "rb") # demo
    await asyncio.sleep(10) #Asssume delay for demo

    # END

    
    await save_file(file=swapped_video, filename=swapped_mp4)  # Mock saving the processed video
    tasks[task_id]["status"] = "completed"
    tasks[task_id]["result"] = f"Face swapped in video and saved as {swapped_mp4}"
    tasks[task_id]["link"] = f"/static/{swapped_mp4}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)