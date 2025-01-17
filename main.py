from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Step 1: Configure the MySQL Database URL
DATABASE_URL = "mysql+pymysql://root:Rushi*123@localhost:3306/pyton-project-db"

# Step 2: Initialize SQLAlchemy Engine and Session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Step 3: Define the Base Model
Base = declarative_base()

# Step 4: Create the FastAPI Application
app = FastAPI()

# Step 5: Define Database Models
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255))

# Step 6: Create the Database Schema
Base.metadata.create_all(bind=engine)

# Step 7: Dependency to Get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Step 8: Define Request Models
class ItemCreate(BaseModel):
    name: str
    description: str

# Step 9: Add API Endpoints
@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item