## Build CLI tool using Typer

## Introduction
This mini project to introduce the ease of creating cli tools using [Typer](https://typer.tiangolo.com/).
The core features used in this repo are:
1. Reading a csv file.
2. Write a csv file.
3. Using typer's built in arguments and options.

## Credits
1. Typer [documentation](https://typer.tiangolo.com/)
2. Babies Names csv file used in this project was provided by National Records of Scotland [here](https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/vital-events/names/babies-first-names/babies-first-names-summary-records-comma-separated-value-csv-format)

## Link to the blog

[Writing CLI tools using Typer](https://blogsbytaha.gtsb.io/cli-tool/)

## Install

```python
$ git clone 
$ cd cli_tutorial
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

The app contains two commands, read, and find. 

### Read
The read command simply verifies the path given and reads out the output.
```python
cd src

>> python main.py read --help

Usage: main.py read [OPTIONS] [PATH]

Arguments:
  [PATH]

Options:
  --help  Show this message and exit.
```

Command
```python
$ cd src
>> python main.py read ../babies_names.csv
```

### Find
The find command can read/write a csv file using a given list of column names. If column names
are not provided, it prompts the user for input.
```python
$ cd src
>> python main.py find --help

Usage: main.py find [OPTIONS] [PATH] [WRITE_PATH]

Arguments:
  [PATH]
  [WRITE_PATH]

Options:
  --f TEXT
  --write   [default: False]
  --help    Show this message and exit.
```  

Commands
```python
# Here we are providing a csv file and the column names the we want it to print it out for us.
# year and rank are column names from the given csv file.
>> python main.py find ../babies_names.csv --f year --f rank
```

```python
# Here we are providing a csv file without explicitly mentioning the column names that we want
# to read from. So the app should prompt the user for that.
>> python main.py find ../babies_names.csv 

<< You have not passed any fields.
<< Please select fields from the following fields: ['year', 'sex', 'FirstForename', 
                'number', 'rank', 'position'].: year sex rank
```

```python
# Here we are providing the app a csv file to read from and a path to write to. Also it 
# includes the column names (year and gender) and a write boolean flag that tells 
# the app that we want to write the output of the column names into that file.
>> python main.py find ../babies_names.csv  ../xyz.csv --f year --f gender --w
```

```python
# Here we are providing the app with a csv file and path to write to. But we have not given it
# a list of column names. So the app should prompt the user for it.
>> python main.py find ../babies_names.csv  --w ../write_output_to_this_file.csv
```

## Testing

Tests are located in the src/test_main.py file.

To run tests

```python
>> pytest
```
