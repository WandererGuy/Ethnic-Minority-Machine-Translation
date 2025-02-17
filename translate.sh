#!/bin/bash

echo "Sourcing conda.sh to enable 'conda activate'..."
source /home/manh264/miniconda3/etc/profile.d/conda.sh  # Adjust to your conda installation path
# Set the second conda environment path and activate it
current_dir=$(pwd)
SECOND_CONDA_ENV_PATH="$(pwd)/env_2"
echo "Activating second conda environment: $SECOND_CONDA_ENV_PATH"
conda activate "$SECOND_CONDA_ENV_PATH"

onmt_translate -model models/run2/model_step_120000.pt -src data/fake-src-test-token.txt -output data/pred_no_bpe.txt -verbose -gpu 0 | tee data/translate.log