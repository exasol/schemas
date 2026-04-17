import typer

from exasol.schemas import generate_static_page

if __name__ == "__main__":
    typer.run(generate_static_page)
