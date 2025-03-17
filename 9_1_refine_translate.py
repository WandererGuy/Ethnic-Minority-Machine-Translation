# from nltk.tokenize.treebank import TreebankWordDetokenizer
# detokenizer = TreebankWordDetokenizer()
# from nltk import word_tokenize

# output = []
# with open('data/fake-pred-no-bpe.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip()
#         line = line.replace(" ", "")
#         line = line.replace("▁", " ")
#         output.append(detokenizer.detokenize(word_tokenize(line)))

# with open('data/fake-pred-no-bpe-detokenize.txt', 'w') as f:
#     for line in output:
#         f.write(line)
#         f.write("\n")
import subprocess
model_path = "target.model"
input = 'data/fake-pred-no-bpe.txt'
output = 'data/fake-pred-no-bpe-detokenize.txt'
command = f"spm_decode --model={model_path} --input_format=piece < {input} > {output}"
print (command)
# Running the subprocess with the provided command
subprocess.run(command, shell=True, check=True)