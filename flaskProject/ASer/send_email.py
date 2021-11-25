import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class ASer_email:
    def __init__(self):
        self.email_add = 'aser_rt@qq.com'  # 发送方邮箱
        self.passwd = ''  # 授权码
        self.msg = MIMEMultipart()
        # 设置邮件主题
        self.msg['Subject'] = "ASer动漫社"

        # 发送方信息
        self.msg['From'] = self.email_add
    def send_email(self,information):# to数组
        email = information['email']
        name = information['name']
        content = 'hello '+name+' 感谢你的意见，我们会及时处理问题，也欢迎你来到ASer动漫社官网! '
        to = []
        to.append(email)
        print(to)
        self.msg.attach(MIMEText(content, 'plain', 'utf-8'))
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录邮箱
        s.login(self.email_add, self.passwd)
        # 开始发送
        try:
            s.sendmail(self.email_add, to, self.msg.as_string())
            print('send ok')
        except:
            print('error')
# if __name__=='__main__':
#     a = ASer_email()
#     a.send_email()