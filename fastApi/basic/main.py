from fastapi import FastAPI, HTTPException
from utils.books import books
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# ? Get-запрос
@app.get('/books', tags=["Книги"], summary="Получить все книги")
def read_books():
  return books

@app.get('/books/{book_id}', tags=["Книги"], summary="Получить конкретную книгу")
def read_book(book_id: int):
  for book in books:
    if book['id'] == book_id:
      return books
    
  # Книга не найдено
  raise HTTPException(
    status_code = 404,
    detail = "Книга не найдена"
  )

class NewBook(BaseModel):
  title: str
  author: str

# ? Post-запрос
@app.post('/books', tags=["Книги"])
def create_book(new_book: NewBook):
  books.append({
    "id": len(books) + 1,
    "title": new_book.title,
    "author": new_book.author
  })

  return {
    "success": True,
    "message": "Книга успешно добавлена"
  }