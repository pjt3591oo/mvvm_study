import React, { useState } from 'react';

import BookViewModel from './ViewModel'
import BookModel from './Model'


function BookView (props) {
  let [ renderFlag, setRenderFlag ] = useState(true)
  let books = props.viewModel.getAll()

  const remove = idx => {
    props.viewModel.remove(idx)
    setRenderFlag(!renderFlag)
  }

  return (
    <>
      <div className="form">
        <input type="text" placeholder="검색"/>
        <button className="read">검색</button>
        <button className="create">등록</button>
      </div>
  
      <div className="list">
        <ul>
          {books.map( (book, idx) => (
            <li key={idx}>
              <span>{book.author}-[{book.name}]</span>
              <button 
                onClick={() => remove(idx)}
                style={{color: 'red'}}
              >
                삭제
              </button>
            </li>
          ))}
        </ul>
      </div>
    </>    
  );
}

function App() {
  const bookModel = new BookModel()
  const bookViewModel = new BookViewModel(bookModel)

  return (
    <>
      <BookView 
        viewModel={bookViewModel}
      />
      <BookView 
        viewModel={bookViewModel}
      />

    </>
  )
}

export default App;
