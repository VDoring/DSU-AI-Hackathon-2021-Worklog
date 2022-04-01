# pickle 파일 로드

import pickle

file_name = 'result.pickle'

with open(file_name, 'rb') as fp:
    data = pickle.load(fp)

# print(data)
for v in data:
    print(v)
