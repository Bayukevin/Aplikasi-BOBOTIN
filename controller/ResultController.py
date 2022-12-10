from PyQt5.QtWidgets import QMainWindow

from controller import HomeController
from view.result.ui_result import Ui_Result


class ResultController(QMainWindow, Ui_Result):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Memberikan aksi ketika btn ulang di tekan
        self.btnRepeat.clicked.connect(self.toAgain)
        # Memberikan aksi ketika btn tutup di tekan
        self.btnClose.clicked.connect(self.endProgram)

    # Fungsi untuk menampilkan halaman utama
    def toAgain(self):
        self.form = HomeController.HomeController()
        self.show()
        self.close()

    # Fungsi untuk mengakhiri program
    def endProgram(self):
        self.close()
        print('Program sukses')
