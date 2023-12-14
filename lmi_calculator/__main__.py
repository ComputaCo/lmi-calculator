import typer

from .calculator import Calculator

app = typer.Typer('Calculator for language models')

calculator = Calculator()

@app.command()
def serve(port: int = typer.Option(..., help="The port to serve on")):
    calculator.serve(port)

@app.command()
def cli():
    calculator.cli()

if __name__ == "__main__":
    app()
