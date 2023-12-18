from parquetpy.subcommands import command_convert, command_inspect
from typer import Typer


app = Typer()

app.add_typer(command_convert, name="convert")
app.add_typer(command_inspect, name="inspect")


if __name__ == "__main__":
    app()
