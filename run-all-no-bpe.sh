#!/bin/bash

echo "Sourcing conda.sh to enable 'conda activate'..."
source /home/manh264/miniconda3/etc/profile.d/conda.sh  # Adjust to your conda installation path

# Set the first conda environment path and activate it
current_dir=$(pwd)
FIRST_CONDA_ENV_PATH="$(pwd)/env_1"
echo "Activating first conda environment: $FIRST_CONDA_ENV_PATH"
conda activate "$FIRST_CONDA_ENV_PATH"

# Run your Python scripts with delays
echo "Running check_prepare.py..."
python check_prepare.py

echo "Sleeping for 2 seconds..."
sleep 2

echo "Running split.py..."
python split.py

echo "Sleeping for 4 seconds..."
sleep 4

echo "Running tokenize_source.py..."
python tokenize_source.py

echo "Sleeping for 4 seconds..."
sleep 4

echo "Running tokenize_target.py..."
python tokenize_target.py

echo "Sleeping for 4 seconds..."
sleep 4



echo "Running config.py..."
python config.py

echo "Sleeping for 4 seconds..."
sleep 4

echo "Starting train.sh..."
bash train.sh
