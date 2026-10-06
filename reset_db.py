from sqlmodel import SQLModel
from database import engine
import models  # noqa: F401  (registers the tables)

SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)
print("Database reset.")

import seed  # re-adds the sample products


#Reset only a sinlge table
# import sqlite3

# conn = sqlite3.connect("shop.db")

#change orderitem to the table you want to reset

# conn.execute("DROP TABLE IF EXISTS orderitem") 
# conn.commit()
# conn.close()
# print("orderitem dropped.") 
