import sys

import uvicorn  # type: ignore
from fastapi import FastAPI
from fastapi.routing import APIRoute, APIRouter
from starlette.middleware.cors import CORSMiddleware

from api.application.health import health_handler

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

get_service_health_route = APIRoute(
    path="/healthz",
    endpoint=health_handler.get_service_health,
    methods=["GET"],
    name="Get Service Health",
)
health_router = APIRouter(routes=[get_service_health_route])
app.include_router(health_router)


def main():  # pylint: disable=missing-function-docstring
    uvicorn.run("api.main:app", host="0.0.0.0", port=8080)


if __name__ == "__main__":
    sys.exit(main())
