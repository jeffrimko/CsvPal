CsvPal
======
Command-line utility for filtering and sorting CSV files.

## Requirements
This application was written in [Python](http://python.org/). Python 2.6 is recommended although other 2.x versions may work. The [`docopt`](http://docopt.org/) Python library is required.

## Installation
To install CsvPal, just add `csvpal.py` to the PATH (or equivalent configuration).

## Example Usage
The following example shows how to filter out two columns (_foo_ and _bar_) from `infile.csv` to a new file named `outfile.csv`:

    csvpal infile.csv outfile.csv foo bar

Adding the `--sort` option will sort the columns in `outfile.csv`:

    csvpal infile.csv outfile.csv foo bar --sort

A "keep file" can be used to specify which columns will be kept in the output file. Each line of the keep file defines a single column to keep. The following example uses the keep file `keepers.txt`:

    csvpal infile.csv outfile.csv --keepfile keepers.txt
