#!/usr/bin/python3
"""
Script qui :
- se connecte à MySQL
- crée la table states (via SQLAlchemy)
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # mysql+mysqldb://user:passwd@host/db
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)   # <-- crée la table
