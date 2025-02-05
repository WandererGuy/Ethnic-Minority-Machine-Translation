from khmernltk import word_tokenize


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
    res = word_tokenize(line, return_tokens=True)
    new_res = []
    for token in res:
        if token.strip() == '': continue
        new_token = token.replace(' ', '_')
        new_res.append(new_token)
    new_res = " ".join(new_res)
    return new_res


src_train = open('./data/src-train.txt', mode='r', encoding='utf8')
src_val = open('./data/src-val.txt', mode='r', encoding='utf8')
src_test = open('./data/src-test.txt', mode='r', encoding='utf8')

src_train_token = open('./data/src-train-token.txt', mode='w+', encoding='utf8')
src_val_token = open('./data/src-val-token.txt', mode='w+', encoding='utf8')
src_test_token = open('./data/src-test-token.txt', mode='w+', encoding='utf8')


n = 0
for line in src_train:
    src_train_token.write(tokenize_line(line) + "\n")
    n+=1
print('Số lượng câu trong tập huấn luyện nguồn là ', n)

n = 0
for line in src_val:
    src_val_token.write(tokenize_line(line) + "\n")
    n+=1
print('Số lượng câu trong tập thẩm định nguồn là ', n)

n = 0
for line in src_test:
    src_test_token.write(tokenize_line(line) + "\n")
    n+=1
print('Số lượng câu trong tập kiểm tra nguồn là ', n)

print("Tokenize sucess")