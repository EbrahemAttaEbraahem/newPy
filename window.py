from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import  sys



app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("القائمه الرئيسيه")
# window.resize(100,100)
# window.move(100,100)
window.setGeometry(300,150,400,350)
text_box1 = QLineEdit(window)
text_box1.move(10,50)





window.show()
app.exec()