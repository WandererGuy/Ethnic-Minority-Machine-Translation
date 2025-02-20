import nltk
def tokenize_line(line):
    '''
    args: line (raw text)
    return: new_res (tokenized text)
    progress:
    - tokenize/subword into a list of tokens/subwords
    - make sure each token separate by space (openNMT input standard)
    - and token contains space in between , replace space with _
    '''
    line = line.strip()
    res = nltk.word_tokenize(line)
    new_res = []
    for token in res:
        if token.strip() == '': continue
        new_token = token.replace(' ', '_')
        new_res.append(new_token)
    new_res = " ".join(new_res)
    return new_res

tgt_train = open('./data/tgt-train.txt', mode='r', encoding='utf8')
tgt_val = open('./data/tgt-val.txt', mode='r', encoding='utf8')
tgt_test = open('./data/tgt-test.txt', mode='r', encoding='utf8')

tgt_train_token = open('./data/tgt-train-token.txt', mode='w+', encoding='utf8')
tgt_val_token = open('./data/tgt-val-token.txt', mode='w+', encoding='utf8')
tgt_test_token = open('./data/tgt-test-token.txt', mode='w+', encoding='utf8')

n = 0;
for line in tgt_train:
    tgt_train_token.write(tokenize_line(line) + "\n")
    n+=1
print('Số lượng câu trong tập huấn luyện đích là ', n)
n = 0
for line in tgt_val:
    tgt_val_token.write(tokenize_line(line) + "\n")
    n+=1
print('Số lượng câu trong tập thẩm định đích là ', n)
n = 0
for line in tgt_test:
    tgt_test_token.write(tokenize_line(line) + "\n")
    n+=1
print('Số lượng câu trong tập kiểm tra đích là ', n)
print("Tokenize sucess")