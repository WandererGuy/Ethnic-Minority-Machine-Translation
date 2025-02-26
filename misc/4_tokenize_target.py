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
# import tiktoken
# encoding = tiktoken.encoding_for_model("gpt-4o-mini")

# fail_token = 0
# success_token = 0 
# find_missing_token_hopefully = 0
# REPLACE_TOKEN = "X"
# def find_missing_token(line, previous_token):
#     """
#     weakness: other similar previous token found other place can make this function mislead missing token
#     """

#     global find_missing_token_hopefully
#     if previous_token == "": return REPLACE_TOKEN
#     # Finding the start index of the substring
#     if previous_token in line:
#         start_index = line.find(previous_token)
#         missing_token_start_index = start_index + len(previous_token)
#         find_missing_token_hopefully += 1
#         return line[missing_token_start_index]
#     else:
#         return REPLACE_TOKEN
# def tokenize_line(line):
#     global fail_token
#     global success_token
#     n = encoding.encode(line)
#     # h = encoding.decode(n)
#     # print (h)
#     k = [encoding.decode_single_token_bytes(token) for token in n]
#     tokenized_sentence_ls = []
#     new_token = ""
#     for token in k:
#         try:
#             new_token = token.decode(encoding="utf-8").strip()
#             success_token += 1
#         except:
#             fail_token += 1
#             previous_token = new_token
#             new_token = find_missing_token(line, previous_token)

#         tokenized_sentence_ls.append(new_token)
#     tokenized_sentence = " ".join(tokenized_sentence_ls)
#     return tokenized_sentence

tgt_train = open('./data/tgt-train.txt', mode='r', encoding='utf8')
tgt_val = open('./data/tgt-val.txt', mode='r', encoding='utf8')
tgt_test = open('./data/tgt-test.txt', mode='r', encoding='utf8')

tgt_train_token = open('./data/tgt-train-token.txt', mode='w+', encoding='utf8')
tgt_val_token = open('./data/tgt-val-token.txt', mode='w+', encoding='utf8')
tgt_test_token = open('./data/tgt-test-token.txt', mode='w+', encoding='utf8')

n = 0
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
print ("*************************************")
print ("success tokens ", success_token)
print ("fail tokens ", fail_token)
print ("find_missing_token_hopefully ", find_missing_token_hopefully)