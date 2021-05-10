from fastapi import FastAPI 
from routers import info
app = FastAPI()

@app.get('/', include_in_schema=False)
async def home():
    return {'msg': 'ok'}

app.include_router(info.router)