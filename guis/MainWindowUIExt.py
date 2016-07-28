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

    def __init__(self, site_mod:dict):
        """

        :param sim: Simulation the simulation client
        """
        super().__init__()
        self.site_mod = site_mod
        self.session = requests.session();
        self.image_path = os.path.join(tempfile.gettempdir(), 'vcode' + self.site_mod['image_ext'])

        # 访问登陆首页
        response = self.session.get(self.site_mod['get_entry_page']())

        self.fp_content = response.text

        self.setupUi(self)


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.buttonCancel.clicked.connect(self.showCode)
        self.buttonOk.clicked.connect(self.submit)
        self.lineCode.returnPressed.connect(self.submit)


        self.showCode()

    def showCode(self):

        captcha_url = self.site_mod['get_captcha_url'](self.fp_content, self.session)
        verify_code_response = self.session.get(captcha_url)
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
        self.send_thread = SendCaptchaCode(code, img_tmp_path, self.site_mod)
        self.send_thread.start()

        self.showCode()

class SendCaptchaCode(threading.Thread):
    def __init__(self, code, img_path, site_mod):
        self.code = code
        self.img_path = img_path
        self.site_mod = site_mod
        super().__init__()

    def run(self):
        with open(self.img_path, 'rb') as img_file:
            files = {'captcha_file': img_file}
            requests.post(CAPTCHA_COLLECTION_POST_API,
                          data={'site': self.site_mod['site_name'],
                                'anwser': self.code},
                          files=files)

        os.remove(self.img_path)