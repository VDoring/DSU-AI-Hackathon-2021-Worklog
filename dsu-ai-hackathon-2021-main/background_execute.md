# [Ubuntu] Background 프로세스 실행

## 일회성 백그라운드 실행

```shell
<명령> &
```

예시:

```shell
streamlit hello &
```

## 반영구성 백그라운드 실행

```shell
nohup <명령>
```

예시:

```shell
nohup streamlit hello
```

### 백그라운드로부터 출력 받아오기

```shell
nohup <명령> > <파일명>
```

### 백그라운드로부터 출력 받지않기

```shell
nohup <명령> > /dev/null
```



## 참조

- https://dptablo.tistory.com/236