"""Simple utility to perform basic operations on a CSV file.

Usage:
    csvpal INFILE OUTFILE [KEEP...] [options]
    csvpal -h | --help
    csvpal --version

Arguments:
    INFILE   The CSV file to read.
    OUTFILE  The CSV file to write.
    KEEP     Column names to keep; if none then all columns will be kept.

Options:
    --keepfile=KEEPFILE     File defining the columns to keep.
    --sort                  Sort the output CSV file by column header.
    -h --help               Show this help message and exit.
    --version               Show version and exit.
"""

##==============================================================#
## COPYRIGHT 2013, REVISED 2014, Jeff Rimko.                    #
##==============================================================#

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import csv

from docopt import docopt

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

__version__ = "csvpal 0.1.0-alpha"

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def make_keep(kfile):
    keep = []
    for line in open(kfile).readlines():
        keep.append(line.strip("\n"))
    return keep

def handle_csv(ipath, opath, sort=False, keep=[]):
    """Handles the CSV logic; reads the input CSV file, performs the requested
    operations, then writes the output CSV file.
    """
    rdr = csv.DictReader(open(ipath, "rb"))
    if [] == keep:
        # If no keep columns are specified, all columns will be kept.
        keep = rdr.fieldnames
    if sort:
        keep = sorted(keep)
    wtr = csv.writer(open(opath, "wb"), keep)
    wtr.writerow(keep)
    for row in rdr:
        wtr.writerow([row[k] for k in keep])

def main():
    """Handles the main application logic."""
    args = docopt(__doc__, version=__version__)
    if args['--keepfile']:
        keep = make_keep(args['--keepfile'])
    else:
        keep = args['KEEP']
    handle_csv(
            args['INFILE'],
            args['OUTFILE'],
            args['--sort'],
            keep)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    main()
