#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QListWidget, QLabel, QFileDialog
import os
from PIL import Image, ImageFilter
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QMovie 
app = QApplication([])
G = QWidget()
G.show()
G.setWindowTitle('FFFFFFFF')

button_folder = QPushButton("Папка")
list_fils = QListWidget()
main_LH = QHBoxLayout()
main_LV_left = QVBoxLayout()
main_LV_ringt = QVBoxLayout()
Label_pic = QLabel("Картинка")
button_left = QPushButton("Лево")
button_ringt = QPushButton("Право")
button_mirror = QPushButton("Зеркало")
button_sharpness = QPushButton("Резкость")
button_BW = QPushButton("Ч/Б")
button_save = QPushButton("Сохранение")
Layout_ringt_button = QHBoxLayout()

G.setLayout(main_LH)
main_LH.addLayout(main_LV_left)
main_LH.addLayout(main_LV_ringt)
main_LV_left.addWidget(button_folder)
main_LV_left.addWidget(list_fils)
main_LV_ringt.addWidget(Label_pic)
Layout_ringt_button.addWidget(button_left)
Layout_ringt_button.addWidget(button_ringt)
Layout_ringt_button.addWidget(button_mirror)
Layout_ringt_button.addWidget(button_sharpness)
Layout_ringt_button.addWidget(button_BW)
Layout_ringt_button.addWidget(button_save)
main_LV_ringt.addLayout(Layout_ringt_button)


class ImageProcessor:
    def __init__(self):
        self.current_image = None
        self.current_name_file = None #короткое имя 
        self.namefolder = "modification"
        self.path = None
        self.pixmap = None

    def loadImage(self, filename):
        self.current_name_file = filename
        print("//////////")
        print(ip.workdir)
        print(filename)
        self.path = os.path.join(ip.workdir, filename) #полное имя файла 
        self.current_image = Image.open(self.path)
        self.pixmap = self.get_pixmap(0)
        
    def show_files(self):
        files = os.listdir(self.workdir)
        print(files)
        list_fils.clear()
        res = filter(files, ['jpg', 'png', 'bmp', 'jpeg'])
        list_fils.addItems(res)
        if not(os.path.isdir(self.workdir +"\modification")):
            print("Создать папку modification...")
            os.mkdir(self.workdir +"\modification")
        else:
            files = os.listdir(ip.workdir + "\modification")
            res = filter(files, ['jpg', 'png', 'bmp', 'jpeg'])
            list_fils.addItems(res)
            
    def filter_right(self):
        if self.current_image != None:
            self.current_image =self.current_image.transpose(Image.ROTATE_90).copy()
            self.pixmap = self.get_pixmap(1)
            self.show_image()
            


    def show_image(self):
        Label_pic.hide()

        w = Label_pic.width()
        h = Label_pic.height() 

        print("scaled image..")
        self.pixmap = self.pixmap.scaled(w, h, Qt.KeepAspectRatio)
        print("set image")
        Label_pic.setPixmap(self.pixmap)
        print("show image")
        Label_pic.show()

    def get_pixmap(self, code: int):
        
        if code == 0:
            return QPixmap(self.path)

        if code == 1:
            qim = ImageQt(self.current_image)
            return QPixmap.fromImage(qim).copy()

ip = ImageProcessor()

def click_folder():
    ip.workdir = QFileDialog.getExistingDirectory()
    print("-------------------")

    print(ip.workdir)
    if ip.workdir != "":
        ip.show_files()
   


def showChosenImage():
    if list_fils.currentRow() >= 0:
        filename = list_fils.currentItem().text()
        ip.current_name_file = filename
        ip.path = os.path.join(ip.workdir, filename)
        ip.loadImage(os.path.join(ip.workdir, filename))
        ip.show_image()

def filter(fils, extensions):
    result = []
    for f in fils:
        for e in extensions:
            if f.endswith(e):
                result.append(f)
                break
    return result

button_folder.clicked.connect(click_folder)
list_fils.currentRowChanged.connect(showChosenImage)
button_ringt.clicked.connect(ip.filter_right)
app.exec()