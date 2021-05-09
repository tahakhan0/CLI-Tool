import csv
import os
from pathlib import Path
from typing import List

import typer


def get_column_names(file: Path):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        return list(next(reader))


def read_or_write(
    file: Path,
    fields: List[str] = [],
    write_to_file: bool = False,
    write_to_path: Path = None,
):
    with open(file) as csv_file:
        if len(fields) != 0:
            reader = csv.DictReader(csv_file)
            if write_to_file:
                with open(write_to_path, "a", newline="") as write_csv_file:
                    writer = csv.DictWriter(write_csv_file, fieldnames=fields)
                    writer.writeheader()
                    for index, row in enumerate(reader):
                        values = dict(
                            (k, v) for k, v in row.items() if k in set(fields)
                        )
                        writer.writerow(values)
                    typer.secho(
                        f"I have written {index} records for you. You can find the csv located in "
                        f"{os.path.abspath(write_to_path)}.",
                        fg=typer.colors.GREEN,
                    )
            else:
                for index, row in enumerate(reader):
                    values = [row[field].strip() for field in fields]
                    typer.secho(str(values), fg=typer.colors.MAGENTA)
        else:
            reader = csv.reader(csv_file)

            for index, row in enumerate(reader):
                output = [data.strip() for data in row]
                typer.secho(str(output), fg=typer.colors.MAGENTA)

            typer.secho(
                f"I have printed {index} items for you.", fg=typer.colors.BRIGHT_CYAN
            )


def match_selected_fields_with_column_names(column_names: List[str], selection) -> list:
    if not isinstance(selection, list):
        selection = list(selection.split(" "))

    return list(set(selection).intersection(set(column_names)))
