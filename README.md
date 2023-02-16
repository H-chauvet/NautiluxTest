# LICENSE
[![License](https://img.shields.io/github/license/H-chauvet/DiscordBotJam)](https://github.com/H-chauvet/DiscordBotJam)

# NautiluxTest

This project is a technical test for Nautilux. The goal is to create and setup a REST API using Python with Django/Django Rest Framework.

# Installation

1st step : Go in the directory ApiRestPython/.

2st step : Instal the dependencies with 'pip3 install -r requirements.txt'

3rd step : Start the project using 'python3.9 manage.py runserver'

# Using the API

You can now access the API with the URL : (https://localhost:4500)


# Features

There is differents features about this API

## Endpoints

list : (https://localhost:4500/Category/) or (https://localhost:4500/Product) <br>
create : (https://localhost:4500/Category/create) or (https://localhost:4500/Product/create) <br>
retrieve : (https://localhost:4500/Category/1/retrieve) or (https://localhost:4500/Product/1/update) <br>
delete : (https://localhost:4500/Category/1/delete) or (https://localhost:4500/Product/1/delete) <br>
update : (https://localhost:4500/Category/1/update) or (https://localhost:4500/Product/1/update) <br>

Please note that the "1" in the exemple URL is for make an available URL. <br>
If you don't have a Category and Product created, this will not work. <br>
The result will be 404 not found.