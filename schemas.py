from pydantic import BaseModel

class WordBase(BaseModel):
    word: str
    count: int

class WordCreate(WordBase):
    pass

class Word(WordBase):
    id: int
    history_id: int

    class Config:
        from_attributes = True

class PastResultsBase(BaseModel):
    subject: str


class PastResultsCreate(PastResultsBase):
    pass


class PastResults(PastResultsBase):
    id: int
    words: list[WordBase] = []

    class Config:
        from_attributes = True