# CropCompanion Backend Setup

This guide will help you set up the backend for the CropCompanion project.

## Prerequisites

Make sure you have the following installed:
- Python 3.8+
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Gajjela-Koushik-Reddy/CropCompanion.git
    cd CropCompanion/backend
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

2. The server will be running at `http://127.0.0.1:8000`.

## API Endpoints

### Generate Text

- **URL:** `/generate`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "prompt": "Your prompt here",
        "system": "You help farmer achieve their goals of sustainable farming",
        "model": "llama3.2:1b",
        "stream": false
    }
    ```
- **Response:**
    ```json
    {
        "generated_text": "Generated text based on the prompt"
    }
    ```

### Clear Memory Cache Text

- **URL:** `/clear_memory`
- **Method:** `POST`
- **Response:**
    ```json
    {
        "value":"mem cache has been cleared"
    }
    ```

## Error Handling

If there is an error communicating with the external API, the server will respond with a 500 status code and an error message.

## Starting the Ollama Server

To start the Ollama server, follow these steps:

1. Download ollama at `https://ollama.com/`

2. Download the LLM `~ % ollama pull llama3.2:1b`

3. The Ollama server will be running at `http://localhost:11434`.

Make sure the server is running before making any API requests to  python server.
