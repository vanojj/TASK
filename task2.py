#создай тут фоторедактор Easy Editor!main_layout = QHBoxLayout() #главная горизонтальная направляющая
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
app = QApplication([])
win = QWidget()
win.show()

main_layout = QVBoxLayout() #V - вертикальная направляющая
win.setLayout(main_layout) #устанаваливаем окну win layout - main_layout

a = QHBoxLayout()
m = QHBoxLayout()
main_layout.addLayout(a)

b1 = QPushButton("Button 1")
b2 = QPushButton("Button 2")
b3 = QPushButton("Button 3")
b5 = QPushButton("Button 5")
b4 = QPushButton("Button 4")
b6 = QPushButton("Button 6")


a.addWidget(b1) 
a.addWidget(b2) 
a.addWidget(b5) 
main_layout.addLayout(m)
m.addWidget(b6) 
m.addWidget(b4)
app.exec()
