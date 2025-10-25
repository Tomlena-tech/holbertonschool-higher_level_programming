#!/usr/bin/python3
"""
Module qui permet de modifier la valeur
enregistrer à l'ID 2 par un nouveaux noms de ville
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter(State.id == 2)
        .first()
    )

    if state:
        state.name = "New Mexico"
        session.commit()
