import streamlit as st
import streamlit.components.v1 as components

import question_loader
import answer_recorder as recorder
import mailer  # @TODO mailer 업데이트 필요

import os
import re

host = mailer.mailer()  # 메일 전송을 위한 모듈


@st.cache
def load_affirm_mail():  # 확인 메일 내용 로드 함수
    affirm_letter_path = os.path.join(os.path.abspath(
        '.'), 'mail', 'letter_of_affirm', 'index.html')

    with open(affirm_letter_path, 'r', encoding='utf-8') as fp:
        __affirm_body__ = fp.readlines()
        __affirm_body__ = '\n'.join(__affirm_body__)

    return __affirm_body__


# 이메일 검사자 (정규표현식)
email_identifier = re.compile(
    '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


def send_affirm(mail_addr=None):  # 확인 메일 전송 함수
    if mail_addr == None or email_identifier.match(mail_addr) == None:
        raise Exception("메일 주소가 형식에 맞지 않습니다.")

    try:
        host.send_mail_via_html(__html__=load_affirm_mail(
        ), __subject__="[Mr.NL] 응답이 성공적으로 기록되었습니다.", __from__=f"Mr.NL <{host.sender_id}>", __to__=[mail_addr])
    except Exception as error:
        raise error


# page configuration
st.set_page_config(
    page_title='Mr.NL',
    page_icon='https://gitlab.com/hungry-studio/dsu-ai-hackathon-2021/-/raw/main/img/favicon.ico',
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': "https://comfort.channel.io/",
        'Report a bug': 'https://comfort.channel.io/',
        'About': """
            # Mr.NL

            이 페이지는 사용자 데이터 수집을 위해 제작되었으며, 2022년 말까지 유효합니다.

            해당 프로젝트는 ``GNU GPLv3 라이선스``로 보호받고 있습니다.
        """
    }
)

# header
components.html("""
    <center>
        <h1> Mr.NL </h1>
    </center>
""")

with st.container():
    selection = st.selectbox(
        label='어떤 분야의 만족도를 검사하고 싶나요?',
        options=('전공', '삶', '직업')
    )

    # 질문 로드하기
    data = question_loader.load_file()
    found_factor = False

    for i, df in data:
        if i == selection:
            st.dataframe(df)
            found_factor = True
            break

    if not found_factor:
        raise Exception(f"{selection} 질문 목록을 찾지 못했습니다.")
