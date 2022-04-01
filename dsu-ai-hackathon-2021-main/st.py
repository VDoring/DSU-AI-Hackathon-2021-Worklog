# import streamlit as st
# import pickle
# import os

# st.title("안녕하세요! Mr.NL입니다.")

# st.markdown("저희는 서술형 문항을 통해 전공 적합성을 예측하는 프로그램을 만들려고 합니다.")
# st.markdown("다만, 이 사이트를 구현하기까지 데이터가 너무 부족해서 여러분의 도움이 필요합니다😢")
# st.markdown("아래 질문에 답변하고, 가나 초콜릿을 받아가세요! (총 3분에게 보내드립니다!)")

# satisfaction = st.slider("자신이 생각하는 전공 만족도를 0~100 사이의 값으로 응답해주세요")

# # 질문 로드
# question = None
# with open("question_list.txt", "r") as fp:
#     data = fp.readlines()

#     token = len(os.listdir(os.path.join('answers'))) if os.path.exists(
#         os.path.join('answers')) else 0

#     question = data[token % len(data)].rstrip('\n')

# st.markdown(f"Q.{question}")

# answer = st.text_area(
#     "답변", key="msg", help="최대한 길게, 정확하게 응답해주세요")

# email = st.text_input("Q.기프티콘을 위해 연락처를 입력해주세요", help="이메일을 입력해주시면 됩니다!")

# submit = st.button("제출")

# if answer == '':
#     st.write("답변을 작성해주세요.")
# elif email == '':
#     st.write("연락처를 작성해주세요.")
# elif submit:
#     st.markdown("설문조사에 참여해주셔서 감사합니다🎉🎉")

#     path = os.path.join("answers")

#     if not os.path.exists(path):
#         os.mkdir(path)

#     token = len(os.listdir(path))

#     with open(os.path.join(path, f"{token}.pickle"), "wb") as fp:
#         pickle.dump({
#             "answer": answer,
#             "satisfaction": satisfaction,
#             "question_tag": token,
#             "email": email
#         }, fp)

#     # with open(os.path.join(path, f"{token}.pickle"), "rb") as fp:
#     #     st.write(pickle.load(fp))

import pickle

data = {
    'addr': 'notice@hungrystudio.ml',
    'pw': '@fornlp21'
}

# with open('usr.pickle', 'wb') as fp:
#     pickle.dump(data, fp)

with open('usr.pickle', 'rb') as fp:
    print(pickle.load(fp))
