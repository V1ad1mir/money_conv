from PySide2.QtWidgets import QApplication, QWidget,QVBoxLayout,QLabel,QLineEdit
import sys
import func

app = QApplication(sys.argv)

mywindow = QWidget();mylayout = QVBoxLayout()

mylayout.addWidget(QLabel('Convert South Korean Won to Israeli New Shekels'))

c = 0.0026948153

krw = QLineEdit()
nis = QLabel("answer")
for i in [krw,nis]:
    func.aligh(i)

mylayout.addWidget(krw)
mylayout.addWidget(nis)
mywindow.setLayout(mylayout)    






mywindow.show()  

app.exec_()

