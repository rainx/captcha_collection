验证码收集器
===============

简介
-----
验证码收集器是为了收集验证码图片和对应答案,为后续机器学习提供训练样本的收集程序

目前它分内两部分

1. 基于django的验证码管理和收集rest api
1. 基于PySide(QT)的收集录入客户端

依赖
-----
Python3 and packages in requiements.txt

RestAPI
---------

```git clone```

之后
```python
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

### rest api

地址:

```
http://[serverhost]/anwser/post
```

方式:
POST

参数:

```
 [anwser] - (string) 验证码的答案
 [site] - (stirng) 验证码的site_name, 用来区分不同网站的验证码
 [captcha_file] - (file) 验证码的图片内容(binary)
```

### 查看地址

```
http://[serverhost]/admin/anwser/captchaanwser
```

GUI 客户端
---------

提供一种插件机制, 运行后选择指定的网站开始输入, 输入答案后按回车键, 结果会自动提交到服务器端的rest api上

插件地址

```
[code root]/guis/site/
~/.captcha_collection_sites/
```

插件格式

```
"""
config the name of site , it will provide as the site param to post to API server.
"""
site_name = 'etrade.cs.ecitic.com'

"""
ext name of the CAPTCHA image
"""
image_ext = ".jpg"

def get_entry_page():
    """
    the entry page contains the captcha
    we start a session from this page
    :return: url of entry page
    """
    return "http://etrade.cs.ecitic.com/"


def get_captcha_url(page_content, session):
    """
    get the url of captcha
    :param page_content: the content of page from get_entry_page
    :return: the url of captcha
    """
    return "https://etrade.cs.ecitic.com/webtrade/pic/Kaptcha.jpg"
```

其中 ```site_name```, ```image_ext```, ```get_entry_page```, ```get_captcha_url```

都是必选项