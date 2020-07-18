class BookViewModel {
  constructor (model) {
    this.model = model
  }

  getAll () {
    return this.model.getAll()
  }

  get (idx) {
    return this.model.get(idx)
  }

  remove (idx) {
    this.model.remove(idx)
  }
}

export default BookViewModel