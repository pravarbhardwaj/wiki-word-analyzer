# wiki-words-analyzer
Counts the most frequent words and stores them on SQLite than can be viewed later. Project was created using FastAPI and consists of two endpoints, one for searching subject and number of top frequent words on page other for fetching previous history of searched subjects.

## How to Install and Run the Project
- Clone the project and open it using preferred editor
- Create Virtual Environment, activate it and run ```pip install -r requirements.txt``` on cmd.
- Run the project by using ```uvicorn main:app --reload``` command.

## Testing Notes
- Open local host after running the project on the hosted port example - ```http://127.0.0.1:8000/docs```, swagger docs are enabled since this is not a production project so apis can be tested from there.
- localhost/get_count api fetches the word count fot the subjet and stores it on SQLite. If invalid subject is entered it will give 422 and error message.
- localhost/history will fetch all the result. it is a paginated api so enter page number and page size in the params.

  

