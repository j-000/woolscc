# wools.cc - URL shorter

<p align="center">
    <img src="https://github.com/j-000/woolscc/blob/master/github_images/w1.PNG" />
</p>

wools.cc is a URL shorter. Easy to use and free! Get over to [wools.cc](https://wools.cc) and meet Baaarbara.

# Tech details

This project uses Flask for the backend alongside SQLAlchemy.

The frontend was created with VueJs.

Nginx is used to serve index.html (Vue app) and to proxy_pass certain requests to the backend (Flask app).

The application is also contained using Docker and at any given time there are about 3 apps running simultaneously.

For simplicity, the application uses a single SQLite database, shared amongst multiple docker containers.

Server is an EC2 t2.medium instance.

It's a pretty simple application but it certainly helped me learn and consolidate some of my current skills.

# Employers

[My CV is on Indeed](https://my.indeed.com/p/jooo-2fu0s8b). Contact info available.

Feel free to message me on [my LinkedIn](https://www.linkedin.com/in/joao-oliveira-b2934516b/)

