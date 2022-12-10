import time
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from controller import HomeController
from view.splashscreen.ui_splash_screen import Ui_SplashScreen


class SplashScreenController(QMainWindow, Ui_SplashScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.counter = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter == 100:
            self.timer.stop()
            self.close()
            time.sleep(1)

            self.homeScreen = HomeController.HomeController()
            self.homeScreen.show()

        self.counter += 1