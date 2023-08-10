# base image  
FROM python:3.8-buster

# set work directory  
# RUN mkdir -p $DockerHOME  

# setup environment variable  
# ENV DockerHOME=/home/app/webapp  


# where your code lives  
WORKDIR /djanog 

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip3 install --upgrade pip  


# copy whole project to your docker home directory. 
COPY . .  

# run this command to install all dependencies  
COPY requirements.txt requirements.txt  
RUN pip3 install -r requirements.txt  
# port where the Django app runs  
# EXPOSE 8000  
# start server  
CMD python3 manage.py runserver 0.0.0.0:8000