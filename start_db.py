if __name__ == '__main__':
    from server import engine
    from models.URL import Base
    Base.metadata.create_all(bind=engine)