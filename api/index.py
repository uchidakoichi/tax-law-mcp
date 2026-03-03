from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from tax-law-mcp on Vercel!"}

@app.post("/mcp")
async def mcp_handler():
    # ここに tax-law-mcp のロジックを組み込んでいく
    return JSONResponse(content={"type": "mcp_response", "content": {"message": "MCP response from Vercel"}})
