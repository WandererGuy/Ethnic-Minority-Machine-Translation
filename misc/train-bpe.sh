#!/bin/bash

# ---------------------------------------------
# Step 1: Source conda.sh to enable 'conda activate'
# ---------------------------------------------
echo "Step 1: Sourcing conda.sh to enable 'conda activate'..."
source /home/manh264/miniconda3/etc/profile.d/conda.sh  # Adjust this path to your conda installation if needed
echo "Successfully sourced conda.sh."

# ---------------------------------------------
# Step 2: Set and activate the second conda environment
# ---------------------------------------------
current_dir=$(pwd)
SECOND_CONDA_ENV_PATH="$(pwd)/env_2"
echo "Step 2: Activating second conda environment: $SECOND_CONDA_ENV_PATH"

conda activate "$SECOND_CONDA_ENV_PATH"
echo "Second conda environment activated."

# ---------------------------------------------
# Step 3: Learn Byte Pair Encoding (BPE) codes
# ---------------------------------------------
echo "Step 3a: Learning BPE codes for source training tokens..."
python OpenNMT-py/tools/learn_bpe.py -i ./data/src-train-token.txt -o ./data/src.code -s 10000
echo "Source BPE codes saved to ./data/src.code."

echo "Step 3b: Learning BPE codes for target training tokens..."
python OpenNMT-py/tools/learn_bpe.py -i ./data/tgt-train-token.txt -o ./data/tgt.code -s 10000
echo "Target BPE codes saved to ./data/tgt.code."

# ---------------------------------------------
# Step 4: Apply the learned BPE codes to the tokenized data
# ---------------------------------------------
echo "Step 4a: Applying BPE to source training tokens..."
python OpenNMT-py/tools/apply_bpe.py -c ./data/src.code -i ./data/src-train-token.txt -o ./data/src-train-bpe.txt
echo "BPE applied to source training tokens. Output saved to ./data/src-train-bpe.txt."

echo "Step 4b: Applying BPE to source validation tokens..."
python OpenNMT-py/tools/apply_bpe.py -c ./data/src.code -i ./data/src-val-token.txt -o ./data/src-val-bpe.txt
echo "BPE applied to source validation tokens. Output saved to ./data/src-val-bpe.txt."

echo "Step 4c: Applying BPE to source test tokens (using target BPE codes)..."
python OpenNMT-py/tools/apply_bpe.py -c ./data/tgt.code -i ./data/src-test-token.txt -o OpenNMT-py/data/src-test-bpe.txt
echo "BPE applied to source test tokens. Output saved to OpenNMT-py/data/src-test-bpe.txt."

echo "Step 4d: Applying BPE to target training tokens..."
python OpenNMT-py/tools/apply_bpe.py -c ./data/tgt.code -i ./data/tgt-train-token.txt -o ./data/tgt-train-bpe.txt
echo "BPE applied to target training tokens. Output saved to ./data/tgt-train-bpe.txt."

echo "Step 4e: Applying BPE to target validation tokens..."
python OpenNMT-py/tools/apply_bpe.py -c ./data/tgt.code -i ./data/tgt-val-token.txt -o ./data/tgt-val-bpe.txt
echo "BPE applied to target validation tokens. Output saved to ./data/tgt-val-bpe.txt."

# ---------------------------------------------
# Step 5: Brief pause before proceeding to vocabulary building
# ---------------------------------------------
echo "Step 5: Pausing for 2 seconds before building the vocabulary..."
sleep 2

# ---------------------------------------------
# Step 6: Build the vocabulary using the configuration file
# ---------------------------------------------
echo "Step 6: Building vocabulary with onmt_build_vocab using 'khmer-viet.yaml' configuration..."
onmt_build_vocab -config khmer-viet.yaml -n_sample 10000
echo "Vocabulary built successfully."

# ---------------------------------------------
# Step 7: Start model training using the configuration file
# ---------------------------------------------
echo "Step 7: Starting training with onmt_train using 'khmer-viet.yaml' configuration..."
onmt_train -config khmer-viet.yaml -verbose
echo "Training initiated."

# End of script
