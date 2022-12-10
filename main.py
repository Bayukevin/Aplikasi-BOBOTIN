import sys
from PyQt5.QtWidgets import QApplication
from controller.SplashScreenController import SplashScreenController


class Main(SplashScreenController):
    def __init__(self):
        super().__init__()
        SplashScreenController()

def main():
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
