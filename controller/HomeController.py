from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from controller import ResultController
from view.home.ui_home import Ui_Home


# Fungsi untuk menampilkan pesan Error
def showErrorMessage(text):
    msg = QMessageBox()
    msg.setWindowTitle('Error!')
    msg.setText(text)
    msg.setStyleSheet("background: #4834d4;\n"
                      "color: #FFFFFF;\n"
                      "font-size: 16px;\n"
                      "font-weight: bold;\n"
                      "font-family: SF Pro Display;\n"
                      "padding: 16px")
    msg.exec_()


class HomeController(QMainWindow, Ui_Home):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.category = ''
        self.ideal = ''
        self.tips = ''

        # Memberikan aksi ketika pengguna memilih jenis kelamin
        self.btnMale.toggled.connect(self.chooseGender)
        self.btnFemale.toggled.connect(self.chooseGender)

        # Memberikan aksi ketika tombol submit di Klik
        self.btnSubmit.clicked.connect(self.moveToResultPage)

        # Validasi inputan hanya angka
        self.edt_age.setValidator(QIntValidator())
        self.edt_height.setValidator(QIntValidator())
        self.edt_weight.setValidator(QIntValidator())

    def moveToResultPage(self):
        try:
            gender = self.chooseGender()
            height = int(self.edt_height.text())
            weight = int(self.edt_weight.text())
            mHeight = height / 100.0  # Konversi ke meter
            bmi = weight / (mHeight * mHeight)
            result = "{:.2f}".format(bmi)

            if gender == 'Male':
                if float(result) < 17.0:
                    self.category = 'Kurus'
                elif float(result) < 23.0:
                    self.category = 'Normal'
                elif float(result) < 27.0:
                    self.category = 'Kegemukan'
                else:
                    self.category = 'Obesitas'
                self.ideal = (int(height) - 100) - ((int(height) - 100) * 10 / 100)

            elif gender == 'Female':
                if float(result) < 18.4:
                    self.category = 'Kurus'
                elif float(result) < 25.0:
                    self.category = 'Normal'
                elif float(result) < 27.0:
                    self.category = 'Kegemukan'
                else:
                    self.category = 'Obesitas'
                self.ideal = (int(height) - 100) - ((int(height) - 100) * 10 / 100)

            # Tips sesuai kategori
            if self.category == 'Normal':
                self.tips = 'Jaga terus pola hidup anda agar tidak terjadi perubahan massa badan'
            elif self.category == 'Kurus':
                self.tips = 'Konsumsilah ikan berminyak, kacang-kacangan untuk sumber protein anda'
            elif self.category == 'Kegemukan':
                self.tips = 'Kurangilah konsumsi karbohidrat, makanlah buah-buahan, dan luangkan waktu untuk olahraga'
            else:
                self.tips = 'Mulailah merubah kebiasaan hidup anda, kurangi konsumsi karbohidrat. Serta luangkan waktu anda untuk berolahraga'

            if self.chooseGender() != '' and self.edt_age.text() != '' and self.edt_weight.text() != '' and self.edt_height.text() != '' and int(self.edt_age.text()) > 12:
                self.form = ResultController.ResultController()
                self.form.tvCount.setText(result)
                self.form.tvResult.setText(self.category)
                self.form.tvIdeal.setText(f'Berat Ideal = {int(self.ideal)} Kg')
                self.form.tvTips.setText(self.tips)
                self.show()
                self.close()
            else:
                showErrorMessage('Mohon isi isian dengan benar!')

        except:
            if self.chooseGender() == '' and self.edt_age.text() == '' and self.edt_weight.text() == '' and self.edt_height.text() == '':
                showErrorMessage('Mohon isi data terlebih dahulu!')
            elif self.chooseGender() == '':
                showErrorMessage('Jenis Kelamin belum di pilih!')
            elif self.edt_age.text() == '':
                showErrorMessage('Isian umur belum di isi!')
            elif int(self.edt_age.text()) <= 12:
                showErrorMessage('Usia harus lebih dari 12')
            elif self.edt_height.text() == '':
                showErrorMessage('Isian tinggi belum di isi!')
            elif self.edt_weight.text() == '':
                showErrorMessage('Isian berat belum di isi!')

    # Fungsi untuk memilih jenis kelamin
    def chooseGender(self):
        gender = ''

        if self.btnMale.isChecked():
            gender = 'Male'
        elif self.btnFemale.isChecked():
            gender = 'Female'

        return gender
