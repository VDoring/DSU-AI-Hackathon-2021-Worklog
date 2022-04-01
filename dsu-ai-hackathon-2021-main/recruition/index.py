import streamlit.components.v1 as components
import streamlit as st

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


if __name__ == '__main__':
    # header:
    st.markdown("""
            # Mr.NL

            Mr.NL은 AI가 제공하는 서술형 질문을 통해 사용자의 성격, 심리 상태, 직업/전공/삶에 대한 만족도, 직업 적성을 추정하는 프로젝트입니다.

            2021 동서인 AI 해커톤을 통해 시작된 프로젝트이며 현재는 사용자의 답변으로부터 삶/전공에 대한 만족도 구하기를 목표로 프로젝트를 진행 중입니다.

            프로젝트에 참여하고자 하시는 분은 아래 QR 코드를 클릭하거나 촬영하여 프로젝트 페이지로 넘어가주세요 :smile:
        """)

    components.html('', height=20)  # 20px

    # section:
    cols = st.columns(3)
    with cols[1]:
        components.html("""
            <center>
                <a href="http://fornlp.ml" target="_blank">
                    <img src="https://i.imgur.com/0aNs21f_d.webp?maxwidth=760&fidelity=grand" width="128px" />
                </a><br>
                <span>
                    프로젝트 참가 QR 이미지
                </span>
            </center>
        """, height=172)
