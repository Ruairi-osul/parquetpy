import pyarrow.dataset as ds
from typer import Argument, Option, Typer
from typing_extensions import Annotated
from typing import Optional
import typer

command_inspect = Typer()


@command_inspect.command()
def head(
    input: Annotated[str, Argument(help="Input Parquet file")],
    n: Annotated[
        Optional[int],
        Option(
            "-n",
            "--num_rows",
            help="Number of rows to display",
            show_default=False,
            rich_help_panel="Select Methods",
        ),
    ] = None,
    frac: Annotated[
        Optional[float],
        Option(
            "-f",
            "--frac",
            help="Fraction of rows to display",
            show_default=False,
            rich_help_panel="Select Methods",
        ),
    ] = None,
):
    """Display first rows of a Parquet file."""

    dataset = ds.dataset(input)

    match n, frac:
        case None, None:
            n_rows = 5
        case None, frac:
            n_rows = int(dataset.num_rows * frac)
        case n, None:
            n_rows = n
        case n, frac:
            raise typer.Abort(
                "Cannot specify both --n and --frac. Please specify only one."
            )

    rows = dataset.head(n_rows).to_pandas()
    print(rows)


@command_inspect.command()
def tail(
    input: Annotated[str, Argument(help="Input Parquet file")],
    n: Annotated[
        Optional[int],
        Option(
            "-n",
            "--num-rows",
            help="Number of rows to display",
            show_default=False,
            rich_help_panel="Select Methods",
        ),
    ] = None,
    frac: Annotated[
        Optional[float],
        Option(
            "-f",
            "--frac",
            help="Fraction of rows to display",
            show_default=False,
            rich_help_panel="Select Methods",
        ),
    ] = None,
):
    """Display first rows of a Parquet file."""

    dataset = ds.dataset(input)

    match n, frac:
        case None, None:
            n_rows = 5
        case None, frac:
            n_rows = int(dataset.num_rows * frac)
        case n, None:
            n_rows = n
        case n, frac:
            raise typer.Abort(
                "Cannot specify both --n and --frac. Please specify only one."
            )

    rows = dataset.head(n_rows).to_pandas()
    print(rows)
