from faker import Faker
from sqlalchemy.orm import Session
from app.core.db.database import SessionLocal
from app.core.db.models.book import Book

fake = Faker()

def seed_books(n=10):
    db: Session = SessionLocal()
    for _ in range(n):
        book = Book(
            title=fake.sentence(nb_words=4),
            author=fake.name(),
            year=fake.year(),
            isbn=fake.isbn13(),
            summary=fake.text(max_nb_chars=200)
        )
        db.add(book)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_books(10)