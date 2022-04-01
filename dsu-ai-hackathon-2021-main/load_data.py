import pickle
import os

path = './answers'

# {path}에 위치한 폴더 내부의 모든 파일 목록 호출
params = os.listdir(path)

data = []  # 모든 데이터를 저장할 리스트 생성

# 각각의 데이터를 모두 불러옴
for param in params:
    with open(os.path.join(path, param), 'rb') as fp:
        data.append(pickle.load(fp))

# print(data)  # 가져온 데이터 출력
print(data[0]['answer'])
