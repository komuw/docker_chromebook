############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER komuw05@gmail.com

# Add the application resources URL
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty main universe" >> /etc/apt/sources.list

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip libpq-dev python-dev postgresql postgresql-contrib

# ADD /home/appdir /home/appdir

# Copy the application folder inside the container
# ADD /home/appdir/docker_example /home/appdir

# Expose ports
EXPOSE 7000
EXPOSE 80
EXPOSE 9000

# Set the default directory where CMD will execute
WORKDIR /home/appdir/docker_example

RUN pip install --upgrade pip

#RUN pip install -r requirements.txt

#RUN python manage.py syncdb --noinput --settings=config.settings.development

#RUN python manage.py migrate --settings=config.settings.development

#RUN python manage.py collectstatic --noinput --settings=config.settings.development

# Set the default directory where CMD will execute
WORKDIR /home/appdir/docker_example

# Set the default command to execute    
# when creating a new container

CMD python manage.py createsuperuser --settings=config.settings.development


# how to build an image from this Dockerfile
# sudo docker build -t test_img .

# how to run an app from that image
# sudo docker run --name test_app -p 7000:7000 -i -t test_img
#  sudo docker run --name web -v /home/appdir/docker_example:/opt/webapp
# sudo docker run --name web -v /home/appdir/docker_example:/home/appdir/docker_example -p 7000:7000 -i -t test_img make run