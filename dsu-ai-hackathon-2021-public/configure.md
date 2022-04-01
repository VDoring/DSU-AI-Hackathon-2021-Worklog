# 기초 세팅 사용법

해당 레파지토리 내용을 사용하기 위해서는 아래에 명시된 모든 패키지를 설치해야 합니다.

우선 ``venv`` 설정부터 해야하는데, ``venv``의 사용법은 [여기](https://hleecaster.com/python-venv/)에 명시하도록 하겠습니다.



``venv`` 설정을 성공적으로 마치셨다면, ``venv`` 환경을 활성화 한 다음, 아래의 명령어를 통해 필요한 패키지를 모두 설치해주세요.

/* 명령어 채우기 */



위의 패키지 중, ``nltk``와 ``konlpy``의 경우 추가적인 설정이 필요합니다.

설정법은 아래에 명시하겠습니다. ([이 문서](https://wikidocs.net/22488)를 참조했습니다)

### NLTK 설정

``nltk``의 경우, 최종 설치가 ``python``을 통해 마무리 됩니다.

자세한 설정은 번호 순서대로, 아래에 명시하겠습니다.

1. 우선, ``venv`` 환경에서 아래의 코드를 실행해주세요.

   ```python
   import nltk
   nltk.download()
   ```

2. 위의 코드를 실행하는 경우, ``nltk``에서 제공하는 설치 위젯이 나옵니다.

   해당 위젯을 통해 설치를 마쳐주시면 됩니다.

### KoNLPy 설정

``KoNLPy``는 ``Java``와 ``JPype``의 추가 설치를 필요로 합니다.





## 사용법

다음과 같습니다.

1. 우선, ``clone`` 또는 다운로드를 통해 레파지토리에 있는 폴더와 똑같은 폴더를 구성해주세요.
2. 명령프롬프트 환경에서, 해당 폴더에 접근하여 ``.\Scripts\activate.bat`` 명령을 실행하면, ``venv`` 가상 환경으로 접근할 수 있습니다.

위의 방법으로 접근하고나면, 평소 파이썬 프로그래밍을 하듯 프로그램을 사용하시면 됩니다.



## 그 외의 참조 명령어

### 파이썬 실행

파이썬 실행은 환경에 따라 3가지가 존재합니다.

```shell
py <파일명>
```

```shell
python <파일명>
```

```python
python3 <파일명>
```

위의 3가지 중 사용 가능한 것을 사용하시면 됩니다.

### 경로 이동

아시는 분들은 아시겠지만, 경로에는 ``절대경로(absoloute path)``와 ``상대경로 (relative path)``가 존재합니다.

``절대경로``는 말 그대로 절대적인 시점에서의 위치를 의미하며, ``상대경로``는 현재 위치를 기준으로 특정 폴더, 특정 파일의 위치를 말합니다.



예를 들어, 현재 위치가 ``C:\A``이고, ``C:\A\B``로 이동하고 싶다면 2가지 방법을 쓸 수 있습니다.

1. ``절대경로 사용``: ``cd C:\A\B``
2. ``상대경로 사용``: ``cd .\A`` 또는 ``cd A``

윈도우를 기준으로 ``.\``는 "현재경로"를 의미합니다.




