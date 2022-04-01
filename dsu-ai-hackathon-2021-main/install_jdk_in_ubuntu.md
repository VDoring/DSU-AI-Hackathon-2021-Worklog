# Install JDK in Ubuntu

이 문서는 Java 8을 기준으로 작성된 [이 문서](https://m.blog.naver.com/opusk/220985259485)를 참조해 작성했습니다.

---

## Java 버전 확인

```shell
java --version
```

## Java 설치

```shell
sudo apt install default-jdk # jdk 설치
```

```shell
sudo apt install default-jre # jre만 설치
```

위 명령이 동작하지 않는다면, 아래 명령어를 참조하세요.

```shell
sudo apt install openjdk-8-jdk # JDK 8 설치
```

```shell
sudo apt install openjdk-8-jre # JDK 8의 JRE만 설치
```

위의 명령 또한 존재하지 않는다면, 추가적인 설정이 필요합니다.

[이 문서](https://wiki.ubuntuusers.de/Java/Installation/Oracle_Java/Java_8/)를 참조하세요.

## 복수의 Java 버전 관리 (복수 개의 Java가 설치된 경우)

```shell
sudo update-alternatives --config java
```

## Java 환경변수 지정

우선 자바의 설치 경로를 먼저 확인해주세요.

환경 변수는 2가지 방법을 통해 설정할 수 있습니다.

1. ```shell
   nano /etc/environment
   ```

   위의 명령을 실행한 후, ``JAVA_HOME="<Java 경로>"``를 입력해주세요.

   예시:

   ```shell
   JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
   ```

   ``Ctrl + X``를 통해 수정한 파일을 저장한 후, 아래의 명령을 실행해 환경 변수를 저장해주세요.

   ```shell
   source /etc/environment
   ```

   > 참조: 이 방법은, Ubuntu에서 환경 변수를 저장/관리하기 위해 사용되는 파일을 수정하는 방법입니다.
   > 경고: 파일 내의 ``PATH`` 환경 변수를 잘못 건드리면, 운영체제 자체에 문제가 생길 수 있으니 주의하세요.

2. ```shell
   nano ~/.bashrc
   ```

   위의 명령을 실행해 ``~/.bashrc``의 파일 수정 화면에 들어간 후, ``export JAVA_HOME=<Java 경로>``를 입력해주세요.

   예시:

   ```shell
   export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
   ```

   > ``export`` 명령어에 대해 자세히 알고 싶다면 [이 포스트](http://keepcalmswag.blogspot.com/2018/06/linux-unix-export-echo_49.html)를 확인해주세요.

   ``Ctrl + X``를 통해 수정된 내용을 저장했다면, 아래의 명령을 실행해 현재 세션에 ``JAVA_HOME`` 환경 변수를 설정해주세요.

   ```shell
   source ~/.bashrc
   ```

   > 설명: 이 방법은, Ubuntu가 부팅될 때 자동으로 실행되는 파일의 내용을 수정하는 방법입니다. 이 파일의 한 부분에 환경 변수 설정을 함으로써, 원하는 내용을 처리할 수 있습니다.

