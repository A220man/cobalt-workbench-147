from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    class_name = data.get("class_name", "")
    variable_name = data.get("variable_name", "")
    
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
