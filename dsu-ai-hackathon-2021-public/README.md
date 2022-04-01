# DSU-AI-Hackathon-2021
2021년도 동서인 AI 해커톤 경진대회



## 참고자료

- [레퍼지토리 사용법](./configure.md)

- [streamlit 사용법](./streamlit.md)



## 오류 로그

1. ```shell
   AttributeError: module 'tweepy' has no attribute 'StreamListener'
   ```

   - 상태: 해결

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

      https://byeon-sg.tistory.com/entry/%EC%9E%90%EC%97%B0%EC%96%B4-%EC%B2%98%EB%A6%AC-konlpy-%EC%84%A4%EC%B9%98-%EC%98%A4%EB%A5%98-okt%EC%97%90%EB%9F%AC-already-loaded-in-another-classloader-SystemErro-1
