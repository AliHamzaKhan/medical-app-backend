import uvicorn
from fastapi import FastAPI
import typer
from app.api.v1.api import api_router
from app.core.config import settings
from app.db import init_db

app = FastAPI()

cli = typer.Typer()

app.include_router(api_router, prefix=settings.API_V1_STR)


@cli.command()
def db_init():
    """
    Initialize the database.
    """
    init_db.init_db()
    print("Database initialized")


@cli.command()
def run():
    """
    Run the application.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    cli()
