# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/25 10:40'

import zmail
from config.conf import cm


def send_report():
    """发送报告"""
    with open(cm.REPORT_FILE, encoding='utf-8') as f:
        content_html = f.read()
    try:
        mail = {
            'from': '240419606@qq.com',#发件人邮箱地址
            'subject': '吾空花果山B2c项目UI自动化测试报告',#邮件主题
            'content_html': content_html,#html邮件内容
            'attachments': [cm.REPORT_FILE, ]#附件
        }
        server = zmail.server(*cm.EMAIL_INFO.values())
        server.send_mail(cm.ADDRESSEE, mail)
        print("测试邮件发送成功！")
    except Exception as e:
        print("Error: 无法发送邮件，{}！", format(e))


if __name__ == "__main__":
    '''请先在config/conf.py文件设置QQ邮箱的账号和密码'''
    send_report()
