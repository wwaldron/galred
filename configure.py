#!/usr/bin/env python
"""This is the configuration file to be used when this template is used to
process a repository.

Examples
--------

`$ ./configure "ESO 137-001"`

"""

# Python Imports
from glob import iglob
from argparse import ArgumentParser


# --- Argument Parsing --- #
# Create the Parser
prsr = ArgumentParser(
    description=__doc__
)

# Add Arguments
prsr.add_argument(
    'gal_title', type=str,
    help='Galaxy title to utilize'
)
prsr.add_argument(
    '-a', '--author', type=str, default="",
    help='The name of the preparer'
)
prsr.add_argument(
    '-i', '--institution', metavar='INST', type=str, default="",
    help="The name of the preparer's institution"
)

# Get the Arguments
args = prsr.parse_args()


# --- Replace Strings --- #
# Prepare the Title
galTitle  = args.gal_title.strip().upper()
galTitle  = ' '.join(galTitle.split())
shrtTitle = ''.join(galTitle.split())
starTitle = '*'.join(galTitle.split()) + '*'

# Loop through Notebooks
for fn in iglob('**/*.ipynb', recursive=True):

    # Open File for Writing
    with open(fn, 'r+') as fid:

        # Get Lines
        fileText = fid.read()

        # Replace Text
        fileText = fileText.replace('[GALAXY]', galTitle)
        fileText = fileText.replace('[GALAXY_SHORT]', shrtTitle)
        fileText = fileText.replace('[GALAXY_WILDCARD]', starTitle)
        fileText = fileText.replace('[AUTHOR]', args.author)
        fileText = fileText.replace('[INSTITUTION]', args.institution)

        # Rewrite the File
        fid.seek(0)
        fid.write(fileText)
        fid.truncate()
