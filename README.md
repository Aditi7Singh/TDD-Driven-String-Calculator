# String Calculator TDD Kata

This project is a solution to the Incubyte TDD assessment. It is a String Calculator with a Python/Flask backend and a React frontend.

## Prerequisites

- Python 3.x
- Node.js and npm

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd string-calculator
    ```

2.  **Backend Setup:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Frontend Setup:**
    ```bash
    cd frontend
    npm install
    ```

## Running the Application

1.  **Start the backend server:**
    From the `string-calculator` directory:
    ```bash
    source venv/bin/activate
    python app.py
    ```
    The backend server will start on `http://127.0.0.1:5000`.

2.  **Start the frontend development server:**
    In a new terminal, from the `string-calculator/frontend` directory:
    ```bash
    npm start
    ```
    The application will open in your browser at `http://localhost:3000`.

## Running Tests

To run the Python tests for the string calculator:
```bash
cd string-calculator
source venv/bin/activate
pytest

