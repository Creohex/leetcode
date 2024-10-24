#!python

import os
import click
from pathlib import Path


TEMPLATE = """\

def solve(data):
    ...

if __name__ == "__main__":
    assert solve(...) == ""

"""


@click.command
@click.argument("name", nargs=1)
@click.option(
    "-e",
    "--ext",
    required=False,
    type=str,
    default="py",
    help="file extension",
)
@click.option(
    "-i",
    "--input_file",
    is_flag=True,
    default=False,
    help="also create input file?",
)
def run(name, ext, input_file):
    if not name:
        raise Exception("'name' not provided!")

    target_dir = Path(os.path.abspath(__file__)).parent / "problems"
    extensions: list[str] = [ext] + (["input"] if input_file else [])
    files: list[Path] = [(target_dir / name).with_suffix(f".{ext}") for ext in extensions]

    for f in files:
        if not f.exists():
            f.write_text(TEMPLATE, "utf-8")
        else:
            print(f"'{str(f)}' already exists.")


if __name__ == "__main__":
    run()
