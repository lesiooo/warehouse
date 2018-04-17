# Django warehouse

The application was initially created by Leszek Stencel, useing python, django, django-rest-framework, PostgreSQL and React.
Project is a web Warehouse Menagment System, that will allow you to track and management items in warehouse, creating orders.
## Getting Started

### Prerequisites
This is intruction how to install and run backend, still working with frontend.

1) Get Docker, and install it in your system.

```
https://www.docker.com/get-docker
``` 

2) Create docker-machine

```
$ docker-machine create -d virtualbox MACHINE_NAME
```


### Installing

1) Download repository from git.

```
$ git clone https://github.com/lesiooo/warehouse

```

2) Paste instructions to terminal to create Docker image, create database and admin profile, install requirements and run server. 

```
$ cd warehouse/warehouse_rest
$ docker-compose  run web python manage.py migrate
$ docker-compose  run web python manage.py createsuperuser
$ docker-compose build
$ docker-compose up
```
3) Open web browser and go to 

```
127.0.0.1:8000/

```
4) Enjoy  :)


## Running the tests

If you want run test aplication

```
$docker-compose  run web python manage.py test

```
