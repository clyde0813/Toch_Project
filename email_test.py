import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('mail.mokpo.ac.kr', 25)
smtp.connect("mail.mokpo.ac.kr",465)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login('kakao', 'Eric3371!')

msg = MIMEText('본문 테스트 메시지')
msg['From'] = 'kakao@mokpo.ac.kr'
msg['Subject'] = '테스트'
msg['To'] = 'eric3285@naver.com'
smtp.sendmail('kakao@mokpo.ac.kr', 'eric3285@naver.com', msg.as_string())

smtp.quit()
