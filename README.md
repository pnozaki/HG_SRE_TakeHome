# HG_SRE_TakeHome
This is the project for the Healthgrades Site Reliability Engineer take home test

The API is written in Python utilizing the Flask microframework.  It takes any HTTP method request on any URI 
and then logs it on the local machine in directory ~/dockerlogs which maps to /var/log within the container.  The API runs 
in a lightweight docker container utilizing the Alpine base image, and leverages a Makefile with a target of make run
to build and run the docker container on port 3000.
