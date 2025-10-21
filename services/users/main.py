from fastapi import FastAPI

from common.utils import hello

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Users service says: {hello()}"}


def main() -> None:
    import uvicorn

    uvicorn.run("services.users.main:app", host="0.0.0.0", port=8002)
