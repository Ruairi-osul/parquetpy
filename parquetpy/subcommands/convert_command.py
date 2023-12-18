from typing_extensions import Annotated
from typer import Argument, Option, Typer
from enum import Enum
import pyarrow.csv as pv
import pyarrow.parquet as pq

command_convert = Typer()


class CompressionType(str, Enum):
    snappy = "snappy"
    gzip = "gzip"
    brotli = "brotli"
    lz4 = "lz4"
    zstd = "zstd"
    none = "none"


@command_convert.command()
def from_csv(
    input: Annotated[str, Argument(help="Input CSV file")],
    output: Annotated[str, Argument(help="Output Parquet file")],
    compression_type: Annotated[
        CompressionType,
        Option(help="Compression type", show_default=False),
    ] = CompressionType.snappy,
):
    """Convert a CSV file to Parquet."""
    table = pv.read_csv(input)
    pq.write_table(table, output, compression=compression_type.value)


if __name__ == "__main__":
    command_convert()
