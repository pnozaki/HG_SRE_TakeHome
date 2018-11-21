# HG_SRE_TakeHome
This is the project for the Healthgrades Site Reliability Engineer take home test

The API is written in Python utilizing the Flask microframework.  It takes any HTTP method request on any URI 
and then logs it in the following format:
  ```
  { 'method' : 'POST', 'uri' : '/golang'}
  { 'method' : 'GET', 'uri' : '/nodejs'}
  { 'method' : 'DELETE', 'uri' : '/hello/world'}
  { 'method' : 'PUT', 'uri' : '/foo/bar'}
  ```
The logs will be located on your local machine in directory ~/dockerlogs which maps to /var/log within the container.
The log follows the naming convention `log-yyyy-mm-dd.txt`.
The API runs in a lightweight docker container utilizing the Alpine base image, and leverages a `Makefile` with a target 
of `make run` to build and run the docker container on port 3000.

# Installation

Prerequisites
* Docker

To install and run the API
````
$ git clone https://github.com/pnozaki/HG_SRE_TakeHome.git && cd HG_SRE_TakeHome
$ make run

````
