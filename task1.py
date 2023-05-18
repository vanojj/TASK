from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
app = QApplication([])
win = QWidget()
win.show()

main_layout = QHBoxLayout() #V - вертикальная направляющая
win.setLayout(main_layout) #устанаваливаем окну win layout - main_layout

b1 = QPushButton("Button 1")
main_layout.addWidget(b1)

b2 = QPushButton("Button 2")





a = QVBoxLayout()
main_layout.addLayout(a)
b3 = QPushButton("Button 3")
b5 = QPushButton("Button 5")
b4 = QPushButton("Button 4")
b6 = QPushButton("Button 3")


a.addWidget(b4) 
main_layout.addWidget(b2) 

a.addWidget(b6) 
a.addWidget(b5) 

app.exec()
