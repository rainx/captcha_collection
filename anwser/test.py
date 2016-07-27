import requests


files = {'captcha_file': open('/Volumes/more/Kaptcha.jpg', 'rb')}

response = requests.post('http://127.0.0.1:8000/anwser/post',
              data={'site' : 'etrade.cs.ecitic.com',
                    'anwser': 'a84p'},
              files=files)


print(response.text)