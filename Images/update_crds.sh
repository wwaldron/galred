#!/usr/bin/bash
# Updates my local CRDS repo for the current image set
# Must be run in conda stenv

# Update the References
# This assumes that the CRDS_SERVER_URL & CRDS_PATH environment variables have been set
crds bestrefs --files mastDownload/HST/*/*fl?.fits --sync-references=1 --update-bestrefs
