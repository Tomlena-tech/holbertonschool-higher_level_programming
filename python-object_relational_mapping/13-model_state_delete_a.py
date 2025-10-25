
#!/usr/bin/python3
"""
Module qui permet de suprimer la noms de ville qui sont
enregistrer dans la database, qui contiennent la lettre a
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

    state_delete = (
        session.query(State)
        .filter(State.name.ilike('%a%'))
        .all()
    )

    for state in state_delete:
        session.delete(state)

    session.commit()
