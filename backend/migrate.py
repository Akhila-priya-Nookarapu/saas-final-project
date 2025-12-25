from database import Base, engine
from models import *

print("Running migrations...")
Base.metadata.create_all(bind=engine)
print("Migrations complete")
