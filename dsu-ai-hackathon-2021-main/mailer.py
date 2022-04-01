import smtplib
import os
import pickle  # smtplib: 메일 전송을 위한 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
# from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
# from email.mime.base import MIMEBase
# from ssl import create_default_context     # 파일을 전송할 때 사용되는 모듈


class mailer:
    def __init__(self, sender_path=None, sender_id=None, sender_pw=None):
        validity = {
            'path': not sender_path == None,
            'account': not (sender_id == None or sender_pw == None)
        }

        self.ABS_PATH = os.path.abspath('.')  # 현재 위치 절대 경로
        self.SENDER_FILE_NAME = 'usr.pickle'  # 유저 정보 파일명

        if validity['account']:  # 유저 정보를 파라미러틑 통해 입력한 경우
            self.sender_id = sender_id
            self.sender_pw = sender_pw
        else:  # 유저 정보가 저장된 경로를 파라미터로 입력한 경우
            # 파일 경로 가져오기
            self.sender_file_path = sender_path if validity['path'] else os.path.join(
                self.ABS_PATH, self.SENDER_FILE_NAME)

            # 발신자 정보 불러오기
            try:
                with open(self.sender_file_path, 'rb') as fp:
                    user_data = pickle.load(fp)
            except Exception as error:
                raise self.error(error)
            finally:
                self.sender_id = user_data['addr']
                self.sender_pw = user_data['pw']

        # 메일 서버 정보 설정
        self.smtp_addr = 'mail.hungrystudio.ml'
        self.smtp_port = 587

    def __str__(self):
        return f"[SMTP Server]\nSERVER ADDR: {self.smtp_addr}\nSERVER PORT: {self.smtp_port}\n[Sender]\nID: {self.sender_id}\nPW: {self.sender_pw}"

    def error(self, msg=""):
        return Exception("" if msg == "" else f"mailer: {msg}")

    def connect(self):
        # SMTP 서버 객체 존재 여부 확인
        validity = True
        try:
            self.__smtp__
        except AttributeError:
            validity = False

        # SMTP 서버 객체가 없는 경우 => SMTP 객체 생성
        if not validity:
            try:
                self.__smtp__ = smtplib.SMTP(
                    host=self.smtp_addr,
                    port=self.smtp_port
                )

                # @TODO STARTTLS 보안 추가해야됨.
                self.__smtp__.ehlo()
                self.__smtp__.login(self.sender_id, self.sender_pw)
            except Exception as error:
                print(self.error(error))

    def send_mail(self, __msg__="", __subject__="", __from__="", __to__=[]):
        # 암묵적으로 연결 상태를 강제함
        self.connect()

        message = MIMEText(__msg__, 'text')
        message["Subject"] = __subject__
        message["From"] = __from__ if not __from__ == "" else f"mailer - {self.sender_id}"
        # message["From"] = f"{__from__} - {self.sender_id}" if not __from__ == "" else self.sender_id
        message["To"] = ', '.join(__to__)

        self.__smtp__.sendmail(
            self.sender_id, message["To"], message.as_string())

    def send_mail_via_html(self, __html__="", __subject__="", __from__="", __to__=[]):
        self.connect()

        __request__ = MIMEMultipart('alternatives')
        __request__['Subject'] = __subject__
        __request__['From'] = __from__
        __request__['To'] = ', '.join(__to__)

        __message__ = MIMEText(__html__, 'html')

        __request__.attach(__message__)

        self.__smtp__.sendmail(self.sender_id, __request__[
                               'To'], __request__.as_string())

    def quit(self):
        self.__smtp__.quit()
        self.__smtp__.close()


if __name__ == '__main__':
    mailman = mailer()

    mailman.send_mail(
        __msg__="Hello World!",
        __subject__="Title of A Test Mail",
        __from__=f"Mr.NL Notifier - {mailman.sender_id}",
        __to__=[
            'kimdonghyun026@gmail.com'
        ]
    )
