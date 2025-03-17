#!/bin/bash
onmt_translate -model models/khmer-spm/model_step_130000.pt -src data/fake-src-test-token.txt -output data/fake-pred-no-bpe.txt -verbose -gpu 0 
echo "From input file data/fake-src-test-token.txt"
echo "Translation complete. Output saved to data/fake-pred-no-bpe.txt"
echo "ground truth file : data/fake-tgt-test-token.txt"