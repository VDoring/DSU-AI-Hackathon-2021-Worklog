from konlpy.tag import Okt
from hanspell import spell_checker
import numpy as np
import pickle

# 데이터 조각 클래스 (pickle 기반)


class piece:
    def __init__(self, dictionary=None):
        if dictionary == None:
            raise Exception("파라미터가 지정되지 않았습니다.")

        self.okt = Okt()

        self.data = dictionary

        self.data['answer'] = spell_checker.check(self.data['answer']).checked

    def __str__(self):
        return f"answer: {self.answer}\nemail: {self.email}\nsatisfaction: {self.satisfaction}%\n{self.question_tag}\n"

    @property
    def nouns(self):
        return self.okt.nouns(self.answer)

    @property
    def email(self):
        return self.data['email']

    @property
    def satisfaction(self):
        return self.data['satisfaction']

    @property
    def answer(self):
        return self.data['answer']

    @property
    def question_tag(self):
        return self.data['question_tag']


class data_handler:
    def __init__(self, path=None):
        if path == None:
            raise Exception("파라미터가 정상적으로 입력되지 않앗습니다.")

        with open(path, 'rb') as fp:
            cache = pickle.load(fp)

        self.cookies = []
        for v in cache:
            self.cookies.append(piece(v))

    def __str__(self):
        return '\n'.join(list(map(str, self.cookies)))

    @property
    def values(self):
        return self.cookies


class token_handler:
    def __init__(self):
        self.cache = {}
        self.cache_number = 0

    def add(self, words=None):
        if not words == None:  # words 입력
            for v in words:
                if not v in self.cache:
                    self.cache[v] = self.cache_number
                    self.cache_number = self.cache_number + 1

    def tokenize(self, splited_list=None):
        if splited_list == None:
            raise Exception("유효한 입력값이 존재하지 않습니다.")

        return_values = []
        for v in splited_list:
            if not v in self.cache:
                return_values.append(0)
            else:
                return_values.append(self.cache.index(v))

        return return_values

    def one_hot_encoding(self, token_dict=None, splited_list=None):
        if token_dict == None:
            raise Exception("토큰 딕셔너리 입력 없음.")

        if splited_list == None:
            raise Exception("유효한 입력값이 존재하지 않습니다.")

        return_values = []
        for v in splited_list:
            if not v in token_dict:
                return_values.append(0)
            else:
                return_values.append(int(token_dict[v]))

        return return_values


# 파일 불러오기
data = data_handler('result.pickle')

# 질문 종류 분류
questions = {}
for v in data.cookies:
    if not v.question_tag in questions:
        questions[v.question_tag] = []

    questions[v.question_tag].append(v)


def cos_similiarity(v1, v2):
    dot_product = np.dot(v1, v2)
    l2_norm = (np.sqrt(sum(np.square(v1)))*np.sqrt(sum(np.square(v2))))
    similarity = dot_product/l2_norm

    return similarity


def get_similarity(v1, v2):
    token = token_handler()

    print(v1, v2)

    token.add(v1)
    token.add(v2)

    vec1, vec2 = token.one_hot_encoding(
        token.cache, v1), token.one_hot_encoding(token.cache, v2)

    l1, l2 = len(v1), len(v2)
    l = min(l1, l2)

    print(vec1, vec2)

    vec1, vec2 = vec1[0:l], vec2[0:l]

    return cos_similiarity(vec1, vec2)


for v in questions[1]:
    print(v)

print(get_similarity(questions[1][2].nouns, questions[1][1].nouns))
