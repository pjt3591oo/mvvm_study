class BookModel {
  constructor () {
    this.books = [
      {
        name: "파이썬으로 배우는 웹 크롤러",
        author: "박정태"
      }, {
        name: "자바스크립트로 서버와 크라이언트 구축하기",
        author: "박정태"
      }, {
        name: "블록체인 프로젝트",
        author: "박정태"
      }
    ]
  }

  add (book) {
    this.books.push(book)
  }
  
  remove (idx) {
    let temp = this.books[idx]
    
    this.books[idx] = this.books[this.books.length-1]
    this.books[this.books.length-1] = temp
    let removedBook = this.books.pop()
    console.log('[CALL] REMOVE', this.books)
    return removedBook
  }

  update (idx, book) {
    this.books[idx] = book
  }

  get (idx) {
    return this.books[idx]
  }

  getAll () {
    return this.books
  }
}

export default BookModel