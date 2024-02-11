from sqlalchemy.orm import Session
from typing import List

import models, schemas

def create_history(db: Session, subject):
    db_history = models.PastResults(subject=subject)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history

def create_words(db: Session, history_id: int, words: dict):
    db_words = list()
    for word in words:
        db_words.append(models.Word(word=word, count=words[word], 
                                    history_id=history_id))
    db.add_all(db_words)
    db.commit()
    return db_words

def get_history(db: Session):
    return db.query(models.PastResults)