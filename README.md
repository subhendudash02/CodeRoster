# MIC FFCS Project - CodeRoster

This is the fullstack project for MIC FFCS 2022.

<br>

Our project aims to fetch Codechef, Codeforces contests and practice questions based on an user's
division and starts in Codechef, or rating in Codeforces. The website also aims to display
hackathons and other competitions based on user's interests. The website will have personalized
dashboard in which the user needs to register and set the interests and Codechef username to get
suitable hackathons and coding competitions.

<br>

## Tech Stack

1. HTML, CSS, Bootstrap (Frontend)
2. Django (Backend)
3. Sqlite (Database, managed by django)

<br>

## Features

1. Sign-in, sign-out and register
2. Web scraping of Codechef and Codeforces contests

<br>

## Setup

1. Install django

```
pip install django
```

2. Clone this project

```
git clone git@github.com:subhendudash02/MIC_ffcs_backend.git
```

3. Run the project

```
python manage.py runserver
```

<br>

<b>Note: </b> If you find any problems registering and signing in, type the following commands

```
    python manage.py makemigrations
    python manage.py migrate
```

<b>Note: </b> In linux, type `python3` instead of `python` and `pip3` instead of `pip`.

# Points to be remembered

 If git asks to stage `__pycache__` and `db.sqlite3` (after running the django app), execute 

`git rm -r <file directory>`

where all the file directories are mentioned in `.gitignore`.
