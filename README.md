# LICENSE
[![License](https://img.shields.io/github/license/H-chauvet/DiscordBotJam)](https://github.com/H-chauvet/DiscordBotJam)

# NautiluxTest

This project is a technical test for Nautilux. The goal is to create and setup a REST API using Python with Django/Django Rest Framework.

# Installation

Before doing following steps, make sure that you have python 3.9.13 installed !
All informations can be found here : (https://www.python.org/downloads/)


1st step : Install the dependencies with `pip install -r requirements.txt`
(Note that you way need 'sudo' to garantee that all the dependencies will be correctly installed)

2st step : Go in the directory ApiRestPython/.

3rd step : Set up the project using `python manage.py migrate --run-syncdb`

4rd step : Start the project using `python manage.py runserver`

# Using the API

You can now access the API with the URL : (https://localhost:8000)


# Features

There is differents features about this API

### Endpoints

list : (https://localhost:8000/Category/) or (https://localhost:8000/Product) <br>
create : (https://localhost:8000/Category/create) or (https://localhost:8000/Product/create) <br>
retrieve : (https://localhost:8000/Category/1/retrieve) or (https://localhost:8000/Product/1/retrieve) <br>
delete : (https://localhost:8000/Category/1/delete) or (https://localhost:8000/Product/1/delete) <br>
update : (https://localhost:8000/Category/1/update) or (https://localhost:8000/Product/1/update) <br>

Please note that the "1" in the exemple URL is for make an available URL. <br>
If you don't have a Category and Product created, this will not work. <br>
The result will be 404 not found.

# Tests

There is some tests about this REST API

You can launch them with these steps :

1st step : Go into the ApiRestPython/ directory

2nd step : Launch tests using : `python manage.py test`

# Copyrights

© 2023 Henri Chauvet. All rights reserved.