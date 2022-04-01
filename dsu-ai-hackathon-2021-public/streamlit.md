# streamlit 모듈 사용법

[서우영님의 블로그 포스트](https://wonyoungseo.medium.com/kr-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9B%B9%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EB%A7%9B%EB%B3%B4%EA%B8%B0-feat-streamlit-846937a7438d)의 내용을 정리한 문서입니다.



### streamlit 설치

```shell
pip install streamlit
```

### streamlit 실행

```shell
streamlit run {your app}.py
```

### streamlit 데모 실행

```shell
streamlit hello
```

### streamlit 모듈 호출

```python
import streamlit as st
```



## 텍스트 출력 

### 기본적인 방법

<img src="https://miro.medium.com/max/875/0*5xe0qwO3YPKJpz6S.png" />

```python
# Title
st.title("Streamlit Tutorial")

# Header/Sub header
st.header("This is header")
st.subheader("This is subheader")

# Text
st.text("This is Text")
```

### Markdown을 사용하는 방법

<img src="https://miro.medium.com/max/875/0*G41m1afvTyzMFf1o.png" />

```python
# Using markdown syntax
st.markdown("# This is a Markdown title")
st.markdown("## This is a Markdown header")
st.markdown("### This is a Markdown subheader")
st.markdown("- item 1\n"
            "   - item 1.1\n"
            "   - item 1.2\n"
            "- item 2\n"
            "- item 3")
st.markdown("1. item 1\n"
            "   1. item 1.1\n"
            "   2. item 1.2\n"
            "2. item 2\n"
            "3. item 3")
```

### Latex를 사용하는 방법

<img src="https://miro.medium.com/max/875/0*KKtzMwnmYPUeRyiL.png" />

```python
## Latex
st.latex(r”Y = \alpha + \beta X_i”)
## Latex-inline
st.markdown(r”회귀분석에서 잔차식은 다음과 같습니다 $e_i = y_i — \hat{y}_i$”)
```

### 예외 문구 출력 방법

<img src="https://miro.medium.com/max/875/0*8ZLY0SuR8v3DTOn8.png" />

```python
## Error/message text
st.success(“Successful”)
st.info(“Information!”)
st.warning(“This is a warning”)
st.error(“This is an error!”)
st.exception(“NameError(‘Error name is not defined’)”)
```

### 데이터 테이블 출력하는 방법

<img src="https://miro.medium.com/max/875/0*mrHuJD_mrjj6zofm.png" />

```python
## Load data
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris['target']
iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))

## Return table/dataframe
# table
st.table(iris_df.head())

# dataframe
st.dataframe(iris_df)
st.write(iris_df)
```

- ``st.table``: 입력된 테이블 전체를 리턴함.
- ``st.dataframe``: 10개의 행을 기준으로 데이터를 관찰하거나, 각 열마다 정렬할 수도 있음.
- ``st.write``: ``st.dataframe``과 같은 결과를 리턴. (``st.write`` == ``st.dataframe``)

### 미디어 출력하는 방법 (이미지, 오디오, 영상)

<img src="https://miro.medium.com/max/875/0*-NZDTOG-AooBQHiO.png" />

```python
##Show image
from PIL import Image
img = Image.open("files/example_cat.jpeg")
st.image(img, width=400, caption="Image example: Cat")
## Show videos
vid_file = open("files/example_vid_cat.mp4", "rb").read()
st.video(vid_file, start_time=2)
## Play audio file.
audio_file = open("files/loop_w_bass.mp3", "rb").read()
st.audio(audio_file, format='audio/mp3', start_time=10)
```

- ``st.image``: 파이썬 이미지 라이브러리와 함께 사용할 수 있음
- ``st.video``: 파일의 포맷을 별도로 지정할 수 있으며, 기본값은 ``video/mp4``. ``start_time`` 파라미터를 통해 영상 시작 지점을 설정할 수 있음.
- ``st.audio``: 파일 포맷을 별도로 지정할 수 있으며, 기본값은 ``audio/wav``. 마찬가지로 ``start_time`` 파라미터를 통해 시작 지점을 설정할 수 있음.

## 위젯 설정

### 체크박스 - ``st.checkbox``

<img src="https://miro.medium.com/max/875/0*2Rbps0YEef5oYhda.png" />

```python
## Checkbox
if st.checkbox(“Show/Hide”):
 st.write(“체크박스가 선택되었습니다.”)
```

### 라디오 버튼 - ``st.radio``

<img src="https://miro.medium.com/max/3000/0*riiKMIBOrdDIUrtp.png" />

```python
## Radio button
status = st.radio("Select status.", ("Active", "Inactive"))
if status == "Active":
    st.success("활성화 되었습니다.")
else:
    st.warning("비활성화 되었습니다.")
```

### 드랍다운 메뉴 - ``st.selectbox``

<img src="https://miro.medium.com/max/875/0*PcLbUHy1Atn34QIl.png" />

<img src="https://miro.medium.com/max/875/0*k3zZRaJ4n5j6udMr.png" />

```python
## Select Box
occupation = st.selectbox("직군을 선택하세요.",
 ["Backend Developer",
 "Frontend Developer",
 "ML Engineer",
 "Data Engineer",
 "Database Administrator",
 "Data Scientist",
 "Data Analyst",
 "Security Engineer"])
st.write("당신의 직군은 ", occupation, " 입니다.")
```

### 드랍다운 메뉴 : 다중선택 - ``st.multiselect``

<img src="https://miro.medium.com/max/875/0*cA2v9GWr6YcESmsz.png" />

<img src="https://miro.medium.com/max/875/0*JLQykUP5EriFwBjt.png" />

```python
## MultiSelect
location = st.multiselect("선호하는 유투브 채널을 선택하세요.",
                          ("운동", "IT기기", "브이로그",
                           "먹방", "반려동물", "맛집 리뷰"))
st.write(len(location), "가지를 선택했습니다.")
```

### 슬라이더 메뉴 - ``st.slider``

<img src="https://miro.medium.com/max/875/0*MrC9l23H-becHbdX.png" />

```python
## Slider
level = st.slider("레벨을 선택하세요.", 1, 5)
```

### 버튼 - ``st.button``

<img src="https://miro.medium.com/max/875/0*7NvefEc3Gbutnzdn.png" />

```python
## Buttons
if st.button("About"):
 st.text("Streamlit을 이용한 튜토리얼입니다.")
```

### 텍스트 입력 - ``text_input``, ``text_area``

- ``type="password"``와 같이 파라미터를 추가해, ``HTML``에서 사용하는 것과 같이 사용할 수 있음.

<img src="https://miro.medium.com/max/875/0*ciqusZqaLHhaniBi.png" />

```python
# Text Input
first_name = st.text_input("Enter Your First Name", "Type Here ...")
if st.button("Submit", key='first_name'):
    result = first_name.title()
    st.success(result)


# Text Area
message = st.text_area("메세지를 입력하세요.", "Type Here ...")
if st.button("Submit", key='message'):
    result = message.titl
```

### 날짜/시간 입력 - ``st.date_input``

<img src="https://miro.medium.com/max/875/0*BQEuQL9BoIZs5Ook.png" />

<img src="https://miro.medium.com/max/875/0*dij1OgOwAWCE00vj.png" />

```python
## Date Input
import datetime
today = st.date_input("날짜를 선택하세요.", datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요.", datetime.time())
```

### 로딩 화면 - ``with st.spinner(msg): <something>``

```python
import time

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
```

위와 같이 사용해 로딩화면을 연출할 수 있음.

### (코드 | JSON) 출력 - ``with st.echo``, ``st.json``

<img src="https://miro.medium.com/max/875/0*xYAguSfkavqgMWTX.png" />

```python
## Display Raw Code — one line
st.subheader(“Display one-line code”)
st.code(“import numpy as np”)

# Display Raw Code — snippet
st.subheader(“Display code snippet”)
with st.echo(): # "with st.echo" 아래의 내용을 모두 코드 블럭으로 출력
 import pandas as pd
 df = pd.DataFrame()

## Display JSON
st.subheader(“Display JSON”)
st.json({‘name’ : ‘민수’, ‘gender’:’male’, ‘Age’: 29})
```

### 사이드바 메뉴 - ``st.sidebar `` :warning:

> ``st.echo``, ``st.spinner``, ``st.write``와 함께 사용 불가

streamlit은 대부분의 위젯을 지원해, 사이드바를 사용할 수 있음.

<u>예제는 아래에 첨부됨</u>

### 레이아웃 분리  - ``st.betacolumns`` (w. 사이드바 메뉴 - ``st.sidebar``)

<img src="https://www.dropbox.com/s/0h1gncfdjer8rzo/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-02-07%20%EC%98%A4%EC%A0%84%202.30.31.png?raw=1" />

```python
# 사이드바 메뉴 추가
add_selectbox = st.sidebar.selectbox("왼쪽 사이드바 Select Box", ("A", "B", "C"))

# 레이아웃을 3개로 분리
col1, col2, col3 = st.beta_columns(3)

with col1: # 고양이 사진
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

with col2: # 
   st.header("Button")
   if st.button("Button!!"):
       st.write("Yes")

with col3:
	st.header("Chart Data")
	chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
	st.bar_chart(chart_data)
```

### 차트 그리기 :exclamation:

streamlit은 기본적으로 자체 내장된 시각화 패키지에 더해 ``matplotlib``, ``plot.ly``, ``altair``, ``vega_lite``, ``bokeh``, ``deck_gl``, ``pydeck``, ``graph_vir`` 등 다양한 시각화 패키지를 지원한다.

대부분의 경우 ``pandas``의 ``dataframe``만 넣으면 동작한다.

<img src="https://miro.medium.com/max/875/0*zIviKf5oPr4ORIba.png" />

## 그 외

[이 포스트](https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/)의 마지막 부분에 streamlit에서 사용할 수 있는 <u>컴포넌트</u>와 <u>Heroku를 사용해 배포하는 방법</u>이 기재되어 있습니다.