from fastapi import FastAPI,Body,Path,Query,HTTPException
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()

class Book :
     id:int
     title:str
     author:str
     description:str 
     rating:int
     published:int

     def __init__(self,id,title,author,description,rating,published):
          self.id=id
          self.title=title
          self.author=author
          self.description=description
          self.rating=rating
          self.published=published



class BookRequest(BaseModel):
     id:int = Field(title="Id is not needed")
     title:str = Field(min_length=3,title="The title of the book") 
     author:str = Field(min_length=1,title="Author of the book")
     description:str  = Field(min_length=1,max_length=100,title="Describe the book")
     rating:int = Field(gt=-1,lt=6,description="Rate the book from 1,6")
     published:int = Field(gt=1900,lt=2040)





BOOKS = [

     Book(id=1,title="Computer Science"
     ,author="CodingWithRoby"
     ,description="A very nice book"
     ,rating=5,published=2020),

     Book(id=2,title="Be Fast With FastAPI",author="CodingWithRoby",description="A very great book",rating=5,published=2020),

     Book(id=1,title="Master endpoint",author="CodingWithRoby",description="A awsome book",rating=2,published=1929),
     
     Book(id=1,title="HP1",author="Author one",description="A very nice book",rating=2,published=1980),

     Book(id=1,title="HP2",author="Author two",description="A very nice book",rating=3,published=2019),

     Book(id=1,title="HP3",author="Author three",description="A very nice book",rating=1,published=2020),
]

# GET 
@app.get('/books')
async def read_all_books():
     return BOOKS
# I bon Return te gjitha librat





@app.get('/books/book_id')
async def read_book(book_id:int):
     books_to_return = []
     for book in BOOKS:
          if book_id == book.id:
               books_to_return.append(book)
     return books_to_return
     
     raise HTTPException(status_code=404, detail="Api Qe Kerkoni Nuk Egziston !")
     # I bon return librat sipas ID






@app.get('/books/')
async def read_book_by_rating(rating : int = Query(gt=0,lt=11) ):
     books_by_rating = []
     for rate in BOOKS:
          if rate.rating == rating:
               books_by_rating.append(rate)
     return books_by_rating
# I bon return librat sipas rating 










@app.get('/read_book_by_publish_date')
async def read_book_by_publish_date(date:int = Query(gt=1900,lt=2040)):
     books_returned = []
     for book in BOOKS:
          if book.published == date:
               books_returned.append(book)
     return books_returned
# I bon return librat sipas dates









# POST
@app.post('/create_book')
async def create_book(book_request: BookRequest ):
     new_book=Book(**book_request.dict())
     BOOKS.append(auto_increment(new_book))
# E krijon ni liber
def auto_increment(book:Book):
     if len(BOOKS) > 0:
          book.id = BOOKS[-1].id + 1
     else :
          book.id = 1 
     return book
# Funksioni pa async qe i perket create_book i cili luan rolin e ato incrementit te ids
     
     
# PUT
@app.put('/book/update_book')
async def update_book(book : BookRequest):
     for x in range(len(BOOKS)):
          if BOOKS[x].id == book.id:
               BOOKS[x] = book







@app.delete('/delete/')
async def delete_book_by_title(book_title):
     for us in BOOKS:
          if BOOKS[us].title.casefold() == book_title.casefold():
               BOOKS.pop(us)

# Per me bo update te dhena ne sistem me app.put duhet te deklarojme nje funksion i cili ka parameter book me instance te BOOKREQUEST dhe duhet te iterojme me for loop ne range te gjatsis se BOOKS dhe nese id e BOOKS[x] osht e njejt me id qe kemi pass in ne book.id ather shko dhe assign qat BOOK[x] me librin qe e kena pass in



