from fastapi import FastAPI

from .a_fazer import router

app = FastAPI()


@app.get("/")
def hello_world():
    """
    View raiz retorna {"message": "Hello World"}
    """

    return {"message": "Hello World"}


app.include_router(router, prefix="/a-fazer", tags=["todo"])
