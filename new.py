#!python

import os
import click
from pathlib import Path


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
def run(name, ext):
    if not name:
        raise Exception("'name' not provided!")

    target_dir = Path(os.path.abspath(__file__)).parent / "problems"
    extensions: list[str] = ["input", ext]
    files: list[Path] = [(target_dir / name).with_suffix(f".{ext}") for ext in extensions]

    if any(f.exists() for f in files):
        raise Exception("File(s) already exist:\n" + "\n".join(map(str, files)))

    [f.write_text("", "utf-8") for f in files]


if __name__ == "__main__":
    run()
