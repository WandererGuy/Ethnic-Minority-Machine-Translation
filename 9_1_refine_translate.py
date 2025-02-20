from nltk.tokenize.treebank import TreebankWordDetokenizer
detokenizer = TreebankWordDetokenizer()
from nltk import word_tokenize

output = []
with open('data/fake-pred-no-bpe.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        output.append(detokenizer.detokenize(word_tokenize(line)))

with open('data/fake-pred-no-bpe-detokenize.txt', 'w') as f:
    for line in output:
        f.write(line)
        f.write("\n")