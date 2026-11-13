# Cobalt Workbench 147

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


A Flutter AI/ML developer tool with a code generator backend.

## Setup

1. Install Python dependencies (if any). The project uses FastAPI.
2. Run the backend: `uvicorn api.main:app --host 0.0.0.0 --port 8000`
3. Open the frontend in a browser: `ui/public/index.html`

## Code Generator

The `/generate` endpoint accepts a POST with JSON `{ "class_name": "MyWidget", "variable_name": "controller" }` and returns generated Dart code.

## License

MIT

Maintainer: Ryan Vo <ryandtvo@gmail.com>
