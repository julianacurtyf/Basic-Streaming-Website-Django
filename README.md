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

<img width="452" alt="home" src="https://user-images.githubusercontent.com/93845875/165349651-42db1f26-1989-490b-b975-8a044474b091.png">

Then, it is possible to interact with the website, either going to the movies page, or to a particula tv show or course. Some of the possibilities can be visualized on the images below.

<img width="452" alt="movies" src="https://user-images.githubusercontent.com/93845875/165350388-6dff29fb-c646-48f3-8d7a-4888a85b0eb9.png">

All the TV Shows:

<img width="452" alt="tvshows" src="https://user-images.githubusercontent.com/93845875/165350448-93709091-12e9-4ad9-ba41-0fe58485abf1.png">

All the Courses:
<img width="452" alt="courses" src="https://user-images.githubusercontent.com/93845875/165350497-48164330-96ea-40ce-ad37-39281c3b8510.png">

A particular movie:
<img width="452" alt="movie" src="https://user-images.githubusercontent.com/93845875/165350554-4dff3ce2-7022-4fe1-82a0-337602be6108.png">

A particular TV Show:
<img width="452" alt="tvshow" src="https://user-images.githubusercontent.com/93845875/165350631-9904021d-fff7-49cb-8fe0-c790048a8a9c.png">

A particular course:
<img width="452" alt="course" src="https://user-images.githubusercontent.com/93845875/165350695-2aa30a1b-f4dd-48d7-992e-c00241accc14.png">


## Technologies

The project was developed mainly using Django (Python), as well as HTML, CSS, and JavaScript for the website template.
