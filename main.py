from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
import os
from PIL import Image 
from PyQt5.QtGui import QPixmap


workdir = ''
   

def filer (files, extentions):
    result = []
    for filename in files:
        for ext in extentions:
            if filename.endwith(ext):
                result.append(filename)
    return result

def showFilenameList():
    extension = ['.jpg', '.png', '.jpeg']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extension) 
    lw_files.clear()
    for filename in filnames:
        lw_files.addItem(filename)   

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = ' workdir'
    def LoadImage(self, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(self, filename)
        self.image = image.open(image_path)


    def showImage(self,path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w,h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path, exists(path)or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)





app = QApplication([])
win = QWidget()
win.setWindowTitle('Photoshop')
win.resize(800, 500)
lb_image = QLabel('картинка')
btn_dir = QPushButton('папка')
lw_files = QListWidget()

btn_right = QPushButton('право')
btn_left = QPushButton('лево')
btn_mirrow = QPushButton('зеркало')
btn_bw = QPushButton('черно-белое')
btn_abc = QPushButton('резкость')




row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

col2.addWidget(lb_image, 95)



row_tools = QHBoxLayout()
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_mirrow)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_abc)

col2.addLayout(row_tools)

row.addLayout(col2, 20)
row.addLayout(col1, 80)
win.setLayout(row)



row1 = QHBoxLayout()
col3 = QVBoxLayout()
col4 = QVBoxLayout()

col3.addWidget(btn_right)
col3.addWidget(btn_left)

col4.addWidget(lb_image, 95)


row1.addLayout(col4, 20)
row1.addLayout(col3, 80)
win.setLayout(row1)



workimage = ImageProcessor()

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir,workimage. filename)
        workimage.showImage(image_path)


def do_flip(self):
    self.image = self.image.rotate(image.FLIP_LEFT_RIGHT)
    self.saveImage()
    image_path = os.path.join(
        workdir, self.save_dir, self.filename
        )
    self.showImage(image_path)


lw_files.currentRowChanged.connect(showChosenImage)
btn_dir.clicked.connect(showFilenameList)
win.show()
app.exec_()















































