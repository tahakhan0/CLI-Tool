from typer.testing import CliRunner

import main

runner = CliRunner()

app = main.app


def test_call_app_with_an_invalid_command():
    """
    Test for failure: If the app is called without a valid command, it should throw out error.
    """
    result = runner.invoke(app, ["invalid_command"])
    assert result.exit_code != 0


def test_read_with_valid_path():
    """
    Test happy path: Can the app read from a valid path?
    """
    result = runner.invoke(app, ["read", "../babies_names.csv"])
    assert result.exit_code == 0
    assert "I have printed " in result.stdout


def test_read_without_any_path():
    """
    Test for failure: The app should throw out an error if no path is provided.
    """
    result = runner.invoke(app, ["read"])
    assert result.exit_code != 0
    assert "No path provided." in result.stdout


def test_find_command_by_providing_a_valid_csv_path_to_read_from_using_valid_column_names():
    """
    Test for success: Can the app find and print the given fields?
    """
    result = runner.invoke(app, ["find", "../test_babies_names.csv --f year --f rank"])
    assert result.exit_code == 0


def test_find_command_by_providing_a_valid_csv_path_to_read_from_and_write_to_using_valid_column_names():
    """
    Test for success: Can the app find and write to a new csv file using the given fields?
    """
    result = runner.invoke(
        app,
        [
            "find",
            "../test_babies_names.csv ../test_write_babies_names.csv --f year --f rank --write",
        ],
    )
    assert result.exit_code == 0
