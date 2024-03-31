#!/bin/bash

#update OS
yum update -y

#install Apache
yum install httpd -y

#copy content to /var/www/html
cd /var/www/html
#wget https://raw.githubusercontent.com/padehatgit/my-repository/main/101-kittens-carousel-static-website-ec2/static-web/index.html
# we create a and assign it to the url to be able to reuse it easily with content of static-web folder
FOLDER=  https://raw.githubusercontent.com/padehatgit/my-repository/main/101-kittens-carousel-static-website-ec2/static-web/
wget ${FOLDER}/index.html
wget ${FOLDER}/cat0.jpg
wget ${FOLDER}/cat1.jpg
wget ${FOLDER}/cat2.jpg
