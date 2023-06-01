import os
import glob

# Get all .py files in the seed folder
seed_files = glob.glob(os.path.join('seed', '*.py'))

# Iterate over the seed files and execute them
for seed_file in seed_files:
    # Execute each seed file
    exec(open(seed_file).read())

