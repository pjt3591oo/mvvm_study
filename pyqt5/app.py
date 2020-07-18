import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore
from PyQt5 import uic

ui_form = uic.loadUiType("main.ui")[0]

class BooksModel(list):
  def __init__(self, l=[]):
    self.data = [{
      "name": "파이썬으로 배우는 웹 크롤러",
      "author": "박정태"
    }, {
      "name": "자바스크립트로 서버와 크라이언트 구축하기",
      "author": "박정태"
    }, {
      "name": "블록체인 프로젝트",
      "author": "박정태"
    }]

    self.model = QStandardItemModel()

    for data in self.data:
      self.model.appendRow(QStandardItem(data['name']))

  def remove(self, idx):
    temp = self.data[idx]
    last_idx = len(self.data)-1
    
    self.data[idx] = self.data[last_idx]
    self.data[last_idx] = temp
    self.data.pop()

    self.model.clear()

    for data in self.data:
      self.model.appendRow(QStandardItem(data['name']))

class BookViewModel:

  def __init__(self, view, model):
    self.view = view
    self.model = model
    self.dataInit()

    self.view.clicked.connect(self.confirm)

  def dataInit(self):
    self.view.setModel(self.model.model)

  def confirm(self):
    data = self.view.selectedIndexes()
    idx = data[0].row()

    msg = '저자: %s, 제목: %s을 삭제하시겠습니까?'%(
      self.model.data[idx]['author'], 
      self.model.data[idx]['name']
    )

    rst = QMessageBox.question(None,'', msg, QMessageBox.Yes | QMessageBox.No)

    if rst == QMessageBox.Yes:
      self.model.remove(idx)


class MainWindow(QMainWindow, ui_form) :
  def __init__(self):
    super().__init__()
    self.setupUi(self)

    self.booksModel = BooksModel()
    self.bookViewModel = BookViewModel(self.books, self.booksModel)

if __name__ == "__main__":
  app = QApplication(sys.argv) 
  myWindow = MainWindow() 
  myWindow.setWindowTitle('Books')
  myWindow.show()
  app.exec_()