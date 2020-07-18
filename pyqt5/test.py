class BooksModel(list):
  def __init__(self, l=[]):
    list.__init__(l)

    data = [{
      "name": "파이썬으로 배우는 웹 크롤러",
      "author": "박정태"
    }, {
      "name": "자바스크립트로 서버와 크라이언트 구축하기",
      "author": "박정태"
    }, {
      "name": "블록체인 프로젝트",
      "author": "박정태"
    }]
    print(data)
    for d in data:
      self.append(d)

  def remove(self, key):
    temp = self[key]
    self[key] = self[len(self) - 1]
    self[len(self) - 1] = temp
    removed = self.pop()
    return removed

  def getAll(self):
    return self
  
  def get(self, idx):
    return self[idx]


a = BooksModel()
print(a)
a.append(1)
a.append(2)
a.append(3)
print(a)

a.remove(1)
print(a)

