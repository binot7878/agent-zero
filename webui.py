from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import uvicorn
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <html>
        <body>
            <h1>👁 Agent Zero Control Panel</h1>
            <form action="/upload" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    with open(f"/tmp/{file.filename}", "wb") as f:
        f.write(content)
    return {"filename": file.filename, "status": "uploaded"}

if __name__ == "__main__":
    uvicorn.run("webui:app", host="0.0.0.0", port=int(os.getenv("AGENTZERO_PORT", 3000)))
