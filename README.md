### Project Explanation

This project implements a basic URL shortener API using FastAPI and PostgreSQL. Here's an overview of the main components:

database.py: Sets up the database connection using SQLAlchemy.
models.py: Defines the database model for storing URLs.
schemas.py: Defines Pydantic models for request/response validation.
main.py: Implements the FastAPI application with two endpoints:

POST /shorten: Accepts a long URL and returns a shortened URL.
GET /{short_code}: Redirects to the original URL.



The API uses SQLAlchemy as an ORM to interact with the PostgreSQL database. When a user submits a URL to be shortened, the API generates a random 6-character code and stores the original URL along with this code in the database. When a user requests a shortened URL, the API looks up the original URL in the database and returns it.


### To run this project, follow these steps:

1. Ensure you have Python 3.7+ installed.
2. Create a new PostgreSQL database for this project.
    a. creating a new user with full privileges:
    1. Connect to PostgreSQL as before:
    ```psql -U postgres```
    2. Create a new user:
    ```CREATE USER myuser WITH PASSWORD 'mypassword';```
    3. Grant privileges:
    ```GRANT ALL PRIVILEGES ON DATABASE url_shortener TO myuser; ```
    ```\c url_shortener```
    ```GRANT ALL PRIVILEGES ON SCHEMA public TO myuser;```
    ```ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO myuser;```

    4. Update your DATABASE_URL in .env:
    ```DATABASE_URL=postgresql://myuser:mypassword@localhost/url_shortener```

### To run this project, follow these steps:
1. Ensure you have Python 3.7+ installed.
2. Create a new PostgreSQL database for this project following the above steps
3. Create a .env file in the root directory with the following content:

```DATABASE_URL=postgresql://username:password@localhost/dbname```
Replace username, password, and dbname with your PostgreSQL credentials.

4. Install the required packages:
```pip install -r requirements.txt```

5. Navigate to the url_shortener directory and run the following command:
```unicorn main:app --reload```

6. The API should now be running at http://localhost:8000. You can access the interactive API documentation at http://localhost:8000/docs.


### To use the API:
To shorten a URL, send a POST request to http://localhost:8000/shorten with a JSON body like this:

```json
{
    "url": "https://www.example.com"
}
```

To retrieve the original URL, send a GET request to http://localhost:8000/{short_code}, replacing {short_code} with the code returned by the shorten endpoint.