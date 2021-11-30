import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get("/")
def index():
    return "Hello World"


if __name__ == '__main__':
    uvicorn.run(app)
