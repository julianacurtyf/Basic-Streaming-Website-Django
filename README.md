# StreamingWebsiteDjango

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/julianacurtyf/StreamingWebsiteDjango.git
$ cd StreamingWebsiteDjango
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Walkthrough

Once you run the server, you will get to a login page:

<img width="452" alt="login" src="https://user-images.githubusercontent.com/93845875/165349416-7f648d3a-b1d9-4ddf-bcda-0be215b8b429.png">

After selecting one of the users, you will get to a home page. The authentication of the users was not the goal of the project, so in this case, is non existent.

<img width="297" alt="home" src="https://user-images.githubusercontent.com/93845875/165349651-42db1f26-1989-490b-b975-8a044474b091.png">





## Technologies

The project was developed mainly using Django (Python), as well as HTML, CSS, and JavaScript for the website template.
