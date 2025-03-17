#!/bin/bash
perl OpenNMT-py/tools/multi-bleu-detok.perl ./data/fake-tgt-test.txt < ./data/fake-pred-no-bpe-detokenize.txt
