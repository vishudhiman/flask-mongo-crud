# Flask MongoDB CRUD Application

A simple CRUD application(Todo List) built with Flask and MongoDB.

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/vishudhiman/flask-mongo-crud.git
   cd flask-mongo-crud
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```sh
   cp .env.example .env  # Update MongoDB URI if needed
   ```

5. **Run the application:**
   ```sh
   python run.py
   ```

## Usage

- Visit `http://127.0.0.1:5000/` to use the CRUD interface.

## Project Structure

- `app/` - Application code (includes configs, database setup, models, and routes)
- `.env` - Environment variables
- `.env.example` - Sample environment file
- `requirements.txt` - Dependencies list
- `run.py` - Application entry point

## License

Licensed under the MIT License.

