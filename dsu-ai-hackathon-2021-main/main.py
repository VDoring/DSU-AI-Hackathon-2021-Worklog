import streamlit as st
from konlpy.tag import Okt
from hanspell import spell_checker
import streamlit.components.v1 as components
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

    token.add(v1)
    token.add(v2)

    vec1, vec2 = token.one_hot_encoding(
        token.cache, v1), token.one_hot_encoding(token.cache, v2)

    # st.write(vec1, vec2)

    l1, l2 = len(v1), len(v2)
    l = min(l1, l2)  # @TODO: 단어 개수별 문제 발생

    vec1, vec2 = vec1[0:l], vec2[0:l]

    # st.write(vec1, vec2)

    return cos_similiarity(vec1, vec2)


# for v in questions[1]:
#     print(v)

# print(get_similarity(questions[1][2].nouns, questions[1][1].nouns))


st.header("Welcome to Mr.ML")
st.markdown('#### 전공 만족도 검사 사이트, Mr.NL에 오신것을 환영합니다.')
st.markdown(
    'Mr.NL은 간편한 전공 만족도 검사를 위하여 만들어졌으며, 자신의 지금 전공이 자기한테 얼마나 맞는가를 알아볼 수 있도록 설계된 AI입니다.')
st.markdown('정보를 정확히 입력해주세요. 정보에 따라 검사 결과가 달라집니다.')

# status = st.radio('성별을 선택하세요.', ('남', '여'))
# age = st.text_input("나이를 입력해주세요", help="나이를 숫자로 입력하시면 됩니다.")
# level = st.slider('나이를 선택하세요.', 1,100)


question_list = []
with open("question_list.txt", "r") as fp:
    string = fp.readlines()
    for v in string:
        question_list.append(v.rstrip('\n'))

st.markdown('---')
# st.markdown('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 여기서부터 문제입니다. ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ--ㅡ')

textareas = []
for i, v in enumerate(question_list):
    textareas.append(st.text_area(f"Q.{v}"))

# # 첫번째 문항
# q1 = st.text_area('1번 문항의 답변을 서술하시오.')
# level2 = st.slider('1번 문항에 대한 현재 당신의 만족도는 어떻습니까?(%)', 0, 100)
# st.markdown('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# # 두번째 문항
# st.markdown('2. ')
# q2 = st.text_area('2번 문항의 답변을 서술하시오.')
# level3 = st.slider('2번 문항에 대한 현재 당신의 만족도는 어떻습니까?(%)', 0, 100)
# st.markdown('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# # 세번째 문항
# st.markdown('3. ')
# q3 = st.text_area('3번 문항의 답변을 서술하시오.')
# level4 = st.slider('3번 문항에 대한 현재 당신의 만족도는 어떻습니까?(%)', 0, 100)

if st.button('확인'):
    okt = Okt()

    our_nouns = []
    for i, v in enumerate(textareas):
        our_nouns.append(piece({
            "question_tag": i,
            "answer": v,
            "email": "",
            "satisfaction": 0
        }))

    st.write("유사도 측정을 시작합니다.")

    # 문제별 유사도
    for i, v in enumerate(textareas):
        result_params = []
        for j, vv in enumerate(questions[i]):  # 문제별, 개체별 유사도 측정하기

            result_params.append(get_similarity(
                vv.nouns, our_nouns[i].nouns))

        # st.write(result_params)

        result = str(round(sum(result_params) /
                     len(result_params) * 10000)/100)
        st.write(f"{i + 1}번 문항 계산 완료")

    st.write(f"예상 적합성: {result}%")
