from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.core.db.database import SessionLocal
from app.services import book_service
from app.api.v1.schemas.book import BookCreate, BookUpdate, BookOut
from app.core.security import get_current_username

router = APIRouter(prefix="/books", tags=["books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[BookOut])
def list_books(db: Session = Depends(get_db)):
    return book_service.get_books(db=db)

@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = book_service.get_book_by_id(db=db, book_id=book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db), username: str = Depends(get_current_username)):
    return book_service.create_book(db=db, book=book)

@router.put("/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    updated_book = book_service.update_book(db=db, book_id=book_id, book_update=book)
    if not updated_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return updated_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db), username: str = Depends(get_current_username)):
    deleted_book = book_service.delete_book_by_id(db=db, book_id=book_id)
    if not deleted_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return None