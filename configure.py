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
    'title', type=str,
    help='Galaxy title to utilize'
)

# Get the Arguments
args = prsr.parse_args()


# --- Replace Strings --- #
# Prepare the Title
galTitle  = args.title.strip().upper()
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
        fileText = fileText.replace('[GALAXY_TITLE]', galTitle)
        fileText = fileText.replace('[GALAXY_SHORT_TITLE]', shrtTitle)
        fileText = fileText.replace('[GALAXY_STAR_TITLE]', starTitle)

        # Rewrite the File
        fid.seek(0)
        fid.write(fileText)
        fid.truncate()
