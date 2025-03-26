from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
import logging
from ai_utils import generate_code_from_azure_ai, create_zip_from_code
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.post("/generate-react/")
async def generate_react_code(request: Request):
    try:
        logging.info("Received request to generate React code.")
        
        # Parse JSON body
        json_data = await request.json()
        if "prompt" not in json_data:
            raise HTTPException(status_code=400, detail="Missing 'prompt' in request body")

        logging.info(f"Generating code for prompt: {json_data['prompt']}")
        
        # Generate code using Azure AI Inference API
        project_files = generate_code_from_azure_ai(json_data["prompt"])
        if not project_files:
            raise HTTPException(status_code=500, detail="Failed to generate code.")
        
        # Create ZIP file
        zip_filename = create_zip_from_code(project_files)
        logging.info(f"ZIP file created: {zip_filename}")
        
        # Return ZIP file for download
        return FileResponse(zip_filename, media_type='application/zip', filename='react_project.zip')
    
    except HTTPException as http_err:
        logging.error(f"HTTP Exception: {http_err.detail}")
        raise http_err
    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)  # Log the full traceback
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
