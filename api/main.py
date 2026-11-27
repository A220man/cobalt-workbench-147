from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import re

app = FastAPI()

# Dart identifier pattern: starts with [a-zA-Z_], followed by [a-zA-Z0-9_]*
_DART_IDENTIFIER_RE = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')


def _validate_identifiers(class_name: str, variable_name: str) -> None:
    """Validate that class_name and variable_name are valid Dart identifiers."""
    if not _DART_IDENTIFIER_RE.match(class_name):
        raise HTTPException(
            status_code=422,
            detail=f"Invalid class_name '{class_name}': must be a valid Dart identifier "
                  f"(starting with a letter or underscore, followed by letters, digits, or underscores).",
        )
    if not _DART_IDENTIFIER_RE.match(variable_name):
        raise HTTPException(
            status_code=422,
            detail=f"Invalid variable_name '{variable_name}': must be a valid Dart identifier "
                  f"(starting with a letter or underscore, followed by letters, digits, or underscores).",
        )


@app.get("/")
def root():
    return {"message": "Hello"}


@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    class_name = data.get("class_name", "")
    variable_name = data.get("variable_name", "")

    _validate_identifiers(class_name, variable_name)

    # Generate Dart code
    code = f'''import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class {class_name} extends StatefulWidget {{
  @override
  _${class_name}State createState() => _${class_name}State();
}}

class _${class_name}State extends State<{class_name}> {{
  TextEditingController {variable_name};
  
  @override
  void initState() {{
    super.initState();
    {variable_name} = TextEditingController();
  }}
  
  @override
  void dispose() {{
    {variable_name}.dispose();
    super.dispose();
  }}
  
  @override
  Widget build(BuildContext context) {{
    return TextField({variable_name}: {variable_name});
  }}
}}
'''

    return JSONResponse(content={"generated_code": code})
