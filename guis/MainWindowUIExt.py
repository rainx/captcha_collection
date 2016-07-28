from .MainWindowUI import Ui_captcha_collect_cli
from PySide import QtGui, QtCore
import requests
import os
import tempfile
import threading
import shutil
import datetime
from pprint import  pprint

CAPTCHA_COLLECTION_POST_API = 'http://captcha.rainx.cn/anwser/post'


class MainWindowUIExt(QtGui.QMainWindow, Ui_captcha_collect_cli):

    def __init__(self, conf:dict):
        """

        :param sim: Simulation the simulation client
        """
        super().__init__()
        self.conf = conf
        self.session = requests.session();
        self.image_path = os.path.join(tempfile.gettempdir(), 'vcode.jpg')

        # 访问登陆首页
        self.session.get("https://etrade.cs.ecitic.com/webtrade/login/login.jsp?ssl=true&ftype=bsn&toUrl=");

        self.setupUi(self)


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.buttonCancel.clicked.connect(self.showCode)
        self.buttonOk.clicked.connect(self.submit)
        self.lineCode.returnPressed.connect(self.submit)


        self.showCode()

    def showCode(self):
        verify_code_response = self.session.get('https://etrade.cs.ecitic.com/webtrade/pic/Kaptcha.jpg')
        # 保存验证码
        with open(self.image_path, 'wb') as f:
            f.write(verify_code_response.content)

        image = QtGui.QPixmap(self.image_path)
        self.codeLabel.setPixmap(image)
        self.lineCode.setText("")

    def submit(self):
        # 将代码发送到收集网站,这里为了速度将使用独立的线程发送

        code = str(self.lineCode.text())

        img_tmp_path = os.path.join(tempfile.gettempdir(),
                                    str(int(datetime.datetime.timestamp(datetime.datetime.now()))) + ".tmp");
        shutil.copy2(self.image_path, img_tmp_path)
        self.send_thread = SendCaptchaCode(code, img_tmp_path)
        self.send_thread.start()

        self.showCode()

class SendCaptchaCode(threading.Thread):
    def __init__(self, code, img_path):
        self.code = code
        self.img_path = img_path
        super().__init__()

    def run(self):
        with open(self.img_path, 'rb') as img_file:
            files = {'captcha_file': img_file}
            requests.post(CAPTCHA_COLLECTION_POST_API,
                          data={'site': 'etrade.cs.ecitic.com',
                                'anwser': self.code},
                          files=files)

        os.remove(self.img_path)