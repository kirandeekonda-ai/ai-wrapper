# Gemini 2.0 Flash LLM API Wrapper

This project exposes a REST API endpoint to accept a prompt, forwards it to the Gemini 2.0 Flash LLM, and returns the LLM response. Built with FastAPI.

## Features
- `/generate` endpoint: Accepts a prompt and returns the Gemini 2.0 Flash LLM response.

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the server:
   ```sh
   uvicorn main:app --reload
   ```

## API Usage
- **POST** `/generate`
  - Request JSON: `{ "prompt": "your prompt here" }`
  - Response JSON: `{ "response": "llm response here" }`

## Notes
- You must provide your Gemini API key as an environment variable: `GEMINI_API_KEY`.
