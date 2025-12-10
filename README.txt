
# FastAPI + SQLite ToDoList API

## Setup Instructions
1. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   #uvicorn main:app --reload
   python main.py
   ```

4. Open Swagger UI:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints
- POST /tasks/ : Create a new task
- GET /tasks/ : Get all tasks
- GET /tasks/{id} : Get task by ID
- PUT /tasks/{id} : Update task
- DELETE /tasks/{id} : Delete task
