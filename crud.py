from sqlalchemy.orm import Session
from typing import List

import models

#Creates subject in hostory table
def create_history(db: Session, subject):
    db_history = models.PastResults(subject=subject)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history

#Creates all the words in words table and links them to history table via foreign key
def create_words(db: Session, history_id: int, words: dict):
    db_words = list()
    for word in words:
        db_words.append(models.Word(word=word, count=words[word], 
                                    history_id=history_id))
    db.add_all(db_words)
    db.commit()
    return db_words
