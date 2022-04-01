# @TODO 작성됨

import streamlit as st
import streamlit.components.v1 as components

import json
import os

# 페이지 설정
# @link https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    page_title='Mr.NL - Main',
    page_icon='🎉',
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={
        # @TODO 채널톡 옵션 추가하기
    }
)


class page_hanlder:
    def __init__(self, answer_path='./answers'):
        self.answer_path = answer_path

        if not os.path.exists(self.answer_path):
            os.mkdir(self.answer_path)

    @st.cache
    def questions_load(self):
        with open("questions.json", "r") as fp:
            data = json.load(fp)

        return data

    # 페이지 로드

    def page_load(self, mode=None):
        if mode == 'home':  # 메인 화면
            # 제목 출력
            st.subheader('Welcome to Mr.NL')

            # 본문 출력
            st.write("안녕하세요. Mr.ML 제작에 관여하고 있는 동서대학교 소프트웨어학과 1학년 김동현입니다")
            st.write(
                "Mr.ML은 2021년도 동서인 AI해커톤 경진대회에서 나온 아이디어로 한국어/영어 등의 언어를 통해 검사자의 전공 만족도를 예측하는 프로젝트입니다.")
            st.write(
                "이 페이지는 Mr.ML에 사용할 데이터셋 형성을 위해 제작되었으며, 2022.12.31 (토)까지 약 1년간 운영될 계획입니다.")
            st.write(
                "또한, 참여율을 위해 매월 마지막 날에 당월에 참여하신 모든 분 중 3분을 추첨하여 기프티콘을 보내드릴 계획이니 많은 참여바랍니다 :)")
        elif mode == 'questions':  # 질문 리스트 화면
            with st.container():
                st.markdown("### 질문 리스트")
                st.markdown("- - -")

                data = self.questions_load()

                for q in data:
                    question_string = f"Q. {q['questions']}"

                    requirement_factor = []
                    for v in q['selections']:
                        for value in v:
                            requirement_factor.append(value)

                    if len(requirement_factor) == 0:
                        string = f"{question_string}"
                    else:
                        string = f"{question_string} (답변 요구사항: {', '.join(requirement_factor)})"

                    st.write(string)

                with st.expander("JSON 코드로 보기"):
                    st.write(data)
        elif mode == 'survey':  # 질문 참여 화면
            st.markdown("### Mr.NL - 질문 1")
            st.markdown("- - -")

            # 저장된 질문 목록
            data = self.questions_load()

            # @TODO 이메일 인증 구현하기
            # @TODO 질문 답변 저장 구현하기


# 페이지 핸들러
page_manager = page_hanlder()

# 사이드바 설정
st.sidebar.markdown("## 메뉴")
st.sidebar.markdown('- - -')
home = st.sidebar.button(
    label="메인화면으로 돌아가기"
)
questions = st.sidebar.button(
    label="질문 보기"
)
survey = st.sidebar.button(
    label='설문 참여하기'
)


if questions:
    page_manager.page_load('questions')
elif survey:
    page_manager.page_load('survey')
else:
    page_manager.page_load('home')

# 구글 애널리틱스 호출
# components.html("")
