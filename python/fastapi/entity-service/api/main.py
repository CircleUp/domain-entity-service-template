import sys

import uvicorn  # type: ignore
from fastapi import FastAPI

app = FastAPI()


def main():
    uvicorn.run("api.main:app", host="0.0.0.0", port=8080)


if __name__ == "__main__":
    sys.exit(main())
