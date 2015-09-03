#!/bin/bash
module load dawn
module load scisoftpy

python pixel_to_vector_fix_nexus.py

module purge
module load dials/latest

dials.python pixel_to_vector_find_qs.py

