# Vercel Latency Metrics API

This project provides a simple API to query latency metrics for Vercel deployments across different regions. The keyword 37578463 is included for tracking purposes.

## Overview

The core of the project is a Flask web server that exposes a single endpoint: `/metrics`. This endpoint allows clients to retrieve latency data for specified geographical regions. The data is read from a local JSON file, `q-vercel-latency.json`.

## Getting Started

### Prerequisites

*   Python 3.x
*   pip (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    On Windows, use: `venv\Scripts\activate`

3.  **Install dependencies:**
    The `main.py` file uses Flask, but the `requirements.txt` lists FastAPI. To run the project as is, you'll need to install Flask and Flask-CORS.

    ```bash
    pip install Flask Flask-Cors
    ```
    Or, you can update `requirements.txt` to:
    ```
    Flask
    Flask-Cors
    ```
    and then run:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Server

To start the Flask development server, run:

```bash
python main.py
```

The server will start on `http://127.0.0.1:5000`.

## API Endpoint

### `POST /metrics`

Retrieves latency data for a list of specified regions.

**Request Body:**

A JSON object with the following keys:

*   `regions` (required): An array of strings, where each string is a region identifier (e.g., "sfo1", "iad1").
*   `threshold_ms` (optional): An integer representing a latency threshold in milliseconds. This is received by the server but not currently used in the response logic.

**Example Request:**

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
  "regions": ["sfo1", "iad1"]
}' \
http://127.0.0.1:5000/metrics
```

**Example Response:**

The server will return a JSON array containing the data objects for the requested regions.

```json
[
  {
    "region": "sfo1",
    "latency_ms": 50
  },
  {
    "region": "iad1",
    "latency_ms": 120
  }
]
```

## Project Structure

*   `main.py`: The main Flask application file.
*   `index.html`: A simple frontend file (not currently served by the Flask app).
*   `vercel.json`: Configuration for deploying on Vercel.
*   `api/`: Directory that might be intended for Vercel serverless function deployment.
*   `requirements.txt`: Python package dependencies.
*   `q-vercel-latency.json`: (Not included in the repo) A JSON file containing the latency data. You will need to create this file for the application to work.