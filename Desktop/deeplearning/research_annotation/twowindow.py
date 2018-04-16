import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import shutil
import PIL 
import json

class show_list(QWidget):
    global data1
    data1 = {}
    def __init__(self, parent = None):
        super(show_list, self).__init__(parent)

        self.left = 100
        self.top = 100
        self.width = 100
        self.height = 100
        self.list = QListWidget()
        
        item = QListWidgetItem(self.list)
        #os.makedirs("/Users/Rentongxuan/Deskstop/images2")
        files = os.listdir("./images")
        files1 = os.listdir("./images1")
        global tasks
        tasks = []
        self.tasks1 = []
        self.delete_list = []
        self.move_from = []
        self.move_to = []
        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox)
        self.setLayout(self.hbox)
        self.text_label = QLabel()
        self.text_label1 = QLabel()
        
        for file in files: 
            if not os.path.isdir(file): 
                  str = ""  
                  str = str + file 
                  
                  tasks.append(str)
                  print(tasks[-1])
        del tasks[0]
        print(tasks)
        self.list.addItems(tasks)
        btn_delete = QPushButton("Delete")
        btn_delete.clicked.connect(self.delete_func)
        btn_delete.setShortcut(QKeySequence("Ctrl+D"))
        btn_undo  = QPushButton("Undo")
        btn_undo.clicked.connect(self.undo_func)
        btn_undo.setShortcut(QKeySequence("Ctrl+U"))
        self.vbox.addWidget(self.list)
        # btn_quick = QPushButton("Quick")
        # btn_quick.clicked.connect(self.shortcut_list)
        btn_down = QPushButton("Down")
        btn_up = QPushButton("Up")
        btn_down.clicked.connect(self.down_func)
        btn_up.clicked.connect(self.up_func)
        btn_down.setShortcut(Qt.Key_Down)
        btn_up.setShortcut(Qt.Key_Up)
        btn_show = QPushButton("Display")
        btn_show.clicked.connect(self.display_img)

        # btn_save = QPushButton("Save")
        # btn_save.clicked.connect(self.save_img)
        self.vbox.addWidget(btn_delete)
        self.vbox.addWidget(btn_undo)
        self.vbox.addWidget(btn_show)
        # self.vbox.addWidget(btn_quick)
        # self.vbox.addWidget(btn_save)
        self.vbox.addWidget(btn_up)
        self.vbox.addWidget(btn_down)
        self.img_label = QLabel()
        self.img_label.move(70, 70)
        # self.display = "./images/" 
        self.img_label1 = QLabel()
        self.img_label1.move(90, 90)
        self.list.itemClicked.connect(self.open_img)
        # self.list.itemClicked.connect(self.open_img1)

    def delete_func(self):
        
        try:
            task = self.list.currentItem().text()
            print(task + "delete")
            if task in tasks:
                path = "./images/" + task
                newpath = "./images2/" + task
                task_mark = task.split(".")[0]
                task1 = task_mark + "_mark.png"
                path1 = "./images1/" + task1
                newpath1 = "./images2/" + task1
                self.move_from.append(path)
                self.move_to.append(newpath)
                tasks.remove(task)
                shutil.move(self.move_from[-1], self.move_to[-1])
                self.delete_list.append(task)
                self.move_from.append(path1)
                self.move_to.append(newpath1)
                # self.tasks.remove(task1)
                shutil.move(self.move_from[-1], self.move_to[-1])
                self.delete_list.append(task1)
                print(self.move_from[-1])
                # print(task)

                print(tasks)
            self.update_list()
        except AttributeError:
            print("You should select one image")

    def undo_func(self):
        try:
            undo_item = self.delete_list[-1]
            # print("undo_item " + undo_item)
            # self.tasks.append(undo_item)
            self.delete_list.remove(undo_item)
            undo_item1 = self.delete_list[-1]
            tasks.append(undo_item1)
            self.delete_list.remove(undo_item1)
            shutil.move(self.move_to[-1], self.move_from[-1])
            self.move_from.pop()
            self.move_to.pop()
            shutil.move(self.move_to[-1], self.move_from[-1])
            self.move_from.pop()
            self.move_to.pop()
            self.update_list()
            print(undo_item + "undo")

        except IndexError:
            print ("Cannot undo anymore")

    
    def update_list(self):
        self.clear_list()
        for task in tasks:
            self.list.addItem(task)
        # self.layout.addWidget(self.list)
        # print(self.tasks)


    def clear_list(self):
        self.list.clear()
        # self.layout.addWidget(self.list)

    def open_img(self):
        if self.list.currentItem():
            # print("image" + self.list.currentItem)
            global show_text
            show_text = self.list.currentItem().text()
            global display 
            task_mark = show_text.split(".")[0]
            task1 = task_mark + "_mark.png"
            display = "./images/" + show_text
            global display1

            display1 = "./images1/" + task1
            print("open " + display)
            pixmap = QPixmap(display)
            pixmap1 = QPixmap(display1)
            pixmap5 = pixmap.scaled(100, 100)
            pixmap51 = pixmap1.scaled(100, 100)
            self.img_label.setPixmap(pixmap5)
            self.img_label.adjustSize()
            self.img_label1.setPixmap(pixmap51)
            self.img_label1.adjustSize()
            self.vbox.addWidget(self.img_label)
            self.vbox.addWidget(self.img_label1)
            self.index = self.list.currentRow();
    def open_img1(self):
        if self.index <= self.list.count:
            # print("image" + self.list.currentItem)
            show_text = self.list1.currentItem().text()
            
            display1 = "./images2/" + show_text
            print("open " + display1)
            pixmap = QPixmap(display1)
            pixmap5 = pixmap.scaled(100, 100)
            self.img_label1.setPixmap(pixmap5)
            self.img_label1.adjustSize()
            self.vbox.addWidget(self.img_label1)
    
    
    def display_img(self):

        self.SW = SecondWindow()
        print("SW")
        # print(self.SW.data)
        self.SW.show()

    

    def shortcut_list(self):
        self.SL = ThirdWindow()
        self.SL.show()
    def up_func(self):
        # cur = self.list.currentItem().text()
        self.text_label.clear()
        self.text_label1.clear()
        global show_text
        now = tasks.index(show_text)
        print(now)
        now = now - 1
        print(len(tasks))
        
        self.text_label.setText(tasks[now])
        
        now_show = tasks[now]
        display = "./images/" + now_show
        task_mark = now_show.split(".")[0]
        task1 = task_mark + "_mark.png"
        self.text_label1.setText(task1)
        display1 = "./images1/" + task1
        pixmap = QPixmap(display)
        pixmap1 = QPixmap(display1)
        pixmap5 = pixmap.scaled(100, 100)
        pixmap51 = pixmap1.scaled(100, 100)
        show_text = tasks[now]
        self.img_label.setPixmap(pixmap5)
        self.img_label.adjustSize()
        self.img_label1.setPixmap(pixmap51)
        self.img_label1.adjustSize()
        self.vbox.addWidget(self.img_label)
        self.vbox.addWidget(self.img_label1)
        self.vbox.addWidget(self.text_label)
        self.vbox.addWidget(self.text_label1)


    def down_func(self):
        global show_text
        now = tasks.index(show_text)
        print(now)
        now = now + 1
        print(len(tasks))
        if now < len(tasks):
            now_show = tasks[now]
            display = "./images/" + now_show
            task_mark = now_show.split(".")[0]
            task1 = task_mark + "_mark.png"
            display1 = "./images1/" + task1
            pixmap = QPixmap(display)
            pixmap1 = QPixmap(display1)
            pixmap5 = pixmap.scaled(100, 100)
            pixmap51 = pixmap1.scaled(100, 100)
            show_text = tasks[now]
            self.img_label.setPixmap(pixmap5)
            self.img_label.adjustSize()
            self.img_label1.setPixmap(pixmap51)
            self.img_label1.adjustSize()
            self.vbox.addWidget(self.img_label)
            self.vbox.addWidget(self.img_label1)

    

class SecondWindow(QWidget):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.resize(200, 200)
        # self.setStyleSheet("background: black")
        list  = show_list()
       
            
        self.setMouseTracking(False)
        self.pos1 = [0,0]
        self.pos2 = [0,0]
        self.pixmap = QPixmap(display)
        
    def paintEvent(self, event):
        self.width = self.pos2[0]-self.pos1[0]
        self.height = self.pos2[1] - self.pos1[1]     
        # global data
        # global ddd
        self.qp = QPainter()
        pen = QPen(Qt.red, 3)
        self.qp.setPen(pen)
        self.item  = list.list.currentItem()
        if list.list.currentItem:
            # self.pixmap = QPixmap(display)
            self.pixmap_resize = self.pixmap.scaled(100, 100)
            # qp.drawPixmap(self.rect(), self.pixmap_resize)
            self.qp.begin(self) 
            self.qp.drawPixmap(self.rect(), self.pixmap_resize)             
            self.qp.drawRect(self.pos1[0], self.pos1[1], self.width, self.height)
            self.qp.end()
            key = self.item.text()
            value = str(self.pos1[0])+ " "+ str(self.pos1[1])+ " " + str(self.pos2[0])+ " " + str(self.pos2[1])
            # self.data[self.item.text()] = value
            data1[key] = value
           
            with open('data.json', 'w+') as f:
                json.dump(data1, f)
                

    def mousePressEvent(self, event):
        self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()
        print("clicked")

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
        print("released")
        
        self.update()
    def take_screenshot(self):
        print("start save")

        cropQPixmap = self.pixmap_resize.copy()

        cropQPixmap.save('output.png')
        print("save")
        # self.qp.deletelater()
class ThirdWindow(QWidget):
    def __init__(self, parent=None):
        super(ThirdWindow, self).__init__(parent)

        self.resize(200, 200)
        list = show_list()
        item = list.list.currentItem()
        print(item)
        
        
        # showitem = tasks.index(item)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.imglabel = QLabel()
        self.vbox.addWidget(self.imglabel)
        self.btn_dis = QPushButton("SHOW")
        self.btn_back = QPushButton("BACK")

        self.btn_dis.clicked.connect(self.showdis)
        self.btn_back.clicked.connect(self.goback)     
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.vbox.addWidget(self.btn_dis)
        self.vbox.addWidget(self.btn_back)
        self.hbox.addLayout(self.vbox)
        self.setLayout(self.hbox)
    def showdis(self):
        item  = list.list.currentItem()
        if list.list.currentItem:
            # self.pixmap = QPixmap(display)
            # self.pixmap_resize = self.pixmap.scaled(100, 100)
            # qp.drawPixmap(self.rect(), self.pixmap_resize)
            # display = "./images1/" + str(item)
            # print("open " + item )
            pixmap = QPixmap(display)
            pixmap1 = pixmap.scaled(100, 100)
            self.imglabel.setPixmap(pixmap1)
            self.imglabel.adjustSize()
            self.vbox.addWidget(self.imglabel)
    def goback(self):
        self.close()

    def keyPressEvent(self, event):
        e = event.key()
        if e == QKeySequence("Ctrl+N"):
            print("WHo")
            item = list.list.currentItem.next()
            display  = "./images/" + item
            pixmap = QPixmap(display)
            pixmap1 = pixmap.scaled(100, 100)
            self.imglabel.setPixmap(pixmap1)
            self.imglabel.adjustSize()
            # print(self.list.currentItem().text())
            # self.index = self.index - 1
            # self.open_img1()
            print("what")
            # print("row" + str(row))
        elif e == Qt.Key_Down:
            # print(self.list.currentItem().text())
            # self.index = self.index + 1
            # self.open_img1()
            print("Down")
    # def keyReleaseEvent(self, event):
    #     e = event.key()
    #     if e == Qt.Key_Up:
    #         print("lalala")
    #         # print(str(row))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = QWidget()

    title = QLabel("Image List ")
    # undo = CustomQWidget()
    # delete = delete_img()
    list = show_list()
    list.show()
    sys.exit(app.exec_())