from pathlib import Path
from typing import List, Optional

import typer

import helpers

# Initialize the app
app = typer.Typer()


@app.command()
def find(
    path: Path = typer.Argument(None),
    fields: Optional[List[str]] = typer.Option(None, "--f"),
    write_path: Path = typer.Option(None, "--w"),
):
    if path.is_file():
        if len(fields) == 0:

            # Raise a message.
            typer.secho(
                "You have not passed any fields.", fg=typer.colors.BRIGHT_YELLOW
            )

            # Get the column names.
            column_names = helpers.get_column_names(file=path)

            # Ask the user for selecting fields from the options.
            selection = typer.prompt(
                f"Please select fields from the following fields: {column_names}."
            )

            # Match the selected fields with the column names,
            fields = helpers.match_selected_fields_with_column_names(
                column_names=column_names, selection=selection
            )

        if write_path is not None:
            if write_path.exists():
                typer.secho(
                    f"Writing output to the file {write_path}.",
                    fg=typer.colors.BRIGHT_BLUE,
                )
            else:
                typer.secho(
                    f"I could not find a path to the file: {write_path}. Therefore, I am creating one for you.",
                    fg=typer.colors.BRIGHT_RED,
                )

            # Write to the given/created file path.
            helpers.read_or_write(
                file=path,
                fields=list(fields),
                write_to_file=True,
                write_to_path=write_path,
            )
        else:
            typer.secho(
                f"You haven't given me a write path. So I'm just going to print it out for you.",
                fg=typer.colors.BRIGHT_BLUE,
            )

            # Read the file with the given fields.
            helpers.read_or_write(file=path, fields=list(fields))
    else:
        typer.Abort("Invalid input.")


@app.command()
def read(path: Path = typer.Argument(None)):
    if path is None:
        typer.secho(f"No path provided.", fg=typer.colors.BRIGHT_RED)
        raise typer.Abort()
    elif path.is_dir():
        typer.secho(f"Cannot read from a directory.", fg=typer.colors.BRIGHT_YELLOW)
    elif path.is_file():
        typer.secho(f"Reading from path: {path}", fg=typer.colors.MAGENTA)
        helpers.read_or_write(file=path)
    elif not path.exists():
        typer.secho(f"Given path: `{path}` does not exist.", fg=typer.colors.BRIGHT_RED)
        typer.Abort()


if __name__ == "__main__":
    app()
