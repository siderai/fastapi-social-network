from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.types import Date

engine = create_engine("sqlite:///database.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), nullable=False, index=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, index=True)
    password = Column(String(30), nullable=False)
    birthday = Column(Date)
    signup_date = Column(Date)
    image = Column(String(255))
    friends = relationship("User", back_populates="Friend")
    country = Column(String(80))
    city = Column(String(50))

    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"User(id={self.id!r}, \
                      username={self.username!r}, \
                      fullname={self.first_name!r} {self.last_name!r}, \
                      email={self.email!r})"


Base.metadata.create_all(bind=engine)
