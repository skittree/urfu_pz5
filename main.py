from fastapi import FastAPI
from routers import emotions

app = FastAPI()
app.include_router(emotions.router)

@app.get('/', summary='Root')
def root():
    return {'message': 'Hello World'}