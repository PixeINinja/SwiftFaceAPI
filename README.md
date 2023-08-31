---

## SwiftSwap FastAPI Server Documentation

Welcome to the SwiftSwap API. This service allows users to swap faces between images and videos. Here's a quick guide on how to utilize the service.

### Endpoints:

#### 1. Check Server Status:
- **Endpoint**: `/check_status`
- **Method**: `GET`
- **Description**: Checks if the server is up and running.
- **Response**: JSON status of the server.
  ```json
  {
      "status": "running"
  }
  ```

#### 2. Swap Image:
- **Endpoint**: `/swap_image/`
- **Method**: `POST`
- **Description**: Swaps the face from the given image to the target image.
- **Form Data**:
  - `image`: The main image file.
  - `target_image`: The target image where the face will be swapped onto.
- **Response**: JSON with the `task_id`.
  ```json
  {
      "task_id": "your-task-id"
  }
  ```

#### 3. Swap Video:
- **Endpoint**: `/swap_video/`
- **Method**: `POST`
- **Description**: Swaps the face from the given image to faces in the target video.
- **Form Data**:
  - `image`: The main image file.
  - `target_video`: The target video where the face will be swapped onto.
- **Response**: JSON with the `task_id`.
  ```json
  {
      "task_id": "your-task-id"
  }
  ```

#### 4. Check Task Status:
- **Endpoint**: `/check_task_status/{task_id}`
- **Method**: `GET`
- **Description**: Retrieve the status of a specific task using its `task_id`.
- **Response**: JSON with the status of the task and, if completed, a link to the processed file.
  ```json
  {
      "status": "completed",
      "result": "Face swapped and saved as target_image_name.jpg",
      "link": "/static/target_image_name.jpg"
  }
  ```

### How to Use:

1. **Swapping Image**:
    - Make a `POST` request to `/swap_image/` with the required form data (the image, target image, and desired output name).
    - The server will return a `task_id`.
    - Use the given `task_id` to check the status by making a `GET` request to `/check_task_status/{task_id}`. Once the status is `completed`, you'll also receive a link to download the swapped image.

2. **Swapping Video**:
    - Make a `POST` request to `/swap_video/` with the required form data (the image, target video, and desired output name).
    - The server will return a `task_id`.
    - Use the given `task_id` to check the status by making a `GET` request to `/check_task_status/{task_id}`. Once the status is `completed`, you'll also receive a link to download the swapped video.

3. **Download Processed File**:
    - Once a task is completed, you'll get a direct link to the processed file in the task status response. Click on the link or paste it in the browser to download the file.

---

Feel free to post this documentation in your group or wherever required so that users can understand how to interact with the SwiftSwap API.
