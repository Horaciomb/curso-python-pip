import store
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}
def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()