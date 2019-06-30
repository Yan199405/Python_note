# -*- coding: utf-8 -*-
from urllib import request

if __name__ == '__main__':
    url = 'https://mail.163.com/js6/main.jsp?sid=OAGgYIpDVTbvNNzRPYDDlCECsyYezbCD&df=mail163_letter#module=welcome.WelcomeModule%7C%7B%7D'
    rsp = request.urlopen(url)
    html = rsp.read().decode('utf-8')
    with open('rsp.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print(f)