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


class BookViewModel(QMainWindow, ui_form) :
  def __init__(self):
    super().__init__()
    print(ui_form, self)
    self.setupUi(self)

    self.booksModel = BooksModel()
    self.dataInit()

    self.books.clicked.connect(self.confirm)

  def dataInit(self):
    self.books.setModel(self.booksModel.model)

  def confirm(self):
    data = self.books.selectedIndexes()
    idx = data[0].row()

    msg = '저자: %s, 제목: %s을 삭제하시겠습니까?'%(
      self.booksModel.data[idx]['author'], 
      self.booksModel.data[idx]['name']
    )
    rst = QMessageBox.question(self,'', msg, QMessageBox.Yes | QMessageBox.No)

    if rst == QMessageBox.Yes:
      self.booksModel.remove(idx)

if __name__ == "__main__":
  app = QApplication(sys.argv) 
  myWindow = BookViewModel() 
  myWindow.setWindowTitle('Books')
  myWindow.show()
  app.exec_()