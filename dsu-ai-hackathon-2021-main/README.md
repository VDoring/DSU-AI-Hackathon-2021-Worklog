# NL-Devs on DSU AI Hackathon 2021

2021년도 동서인 AI 해커톤 경진대회에 참가할 때 사용한 아이더어를 정리한 문서입니다.

---

- 팀 이름: <b>NL-Devs</b>
- 아이디어 이름: 자연어 처리를 통한 전공/삶 만족도 예측 프로그램
- 컨셉: Holland 직업 적성 검사와 같은 타 직업 적성 검사 프로그램의 많은 문항 수로 인한 긴 소요 시간과 집중력 저하를 자연어 처리를 통해 감소 시키는 프로그램.
- 방식: 질문 유형에 따라 저장된 각 데이터로부터 유사도 정보와 만족도 정보를 구해, 최종적으로는 검사자 표본이 얼마나 긍정적인 군집과 가까운지 나타낸다. (별점 0점 ~ 5점 중)
- 컨셉과 구현 방식의 맥락이 다른 이유: 현재 상황에서는 직업 적성 검사 프로그램을 위한 알고리즘을 구현할 수 없기 때문

## 참고자료

- [레퍼지토리 사용법](./configure.md)

- [streamlit 사용법](./streamlit.md)



## 오류 로그

1. ```shell
   AttributeError: module 'tweepy' has no attribute 'StreamListener'
   ```

   - 설명: tweepy 버전을 ``4.3.0``에서 ``3.10.0으로 바꾸어 해결하였습니다.

     ```shell
     pip install tweepy=3.10.0
     ```

   - 참조

     - Inflearn Forum: https://www.inflearn.com/questions/324338

   
2. ```shell
   java.nio.file.InvalidPathException: Illegal char <*> at index 55: C:\Programming\Anaconda3\Lib\site-packages\konlpy\java\*'
   ```
   - Java의 환경변수를 다시 설정한다. 자세한 사항은 아래 사이트 참조.
   - C:\ProgramData\Anaconda3\Lib\site-packages\konlpy 에서 jvm.py 파일로 들어가서 *를 제거한다.

   -  참조
      -  https://byeon-sg.tistory.com/entry/%EC%9E%90%EC%97%B0%EC%96%B4-%EC%B2%98%EB%A6%AC-konlpy-%EC%84%A4%EC%B9%98-%EC%98%A4%EB%A5%98-okt%EC%97%90%EB%9F%AC-already-loaded-in-another-classloader-SystemErro-1
