import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ybio')
        self.move(300, 100)
        self.resize(300, 400)
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())