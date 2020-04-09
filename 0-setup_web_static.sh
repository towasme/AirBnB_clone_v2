#!/usr/bin/env bash
#cript that sets up your web servers for the deployment of web_static

# 1 update and install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# 2 create directories if not created
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared

# 3 create html file in the test directory
sudo echo -e '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello to all</title>
</head>
<body>
	<h1>Hellooooo i am towas</h1>
</body>
</html>' | sudo tee /data/web_static/releases/test/index.html

# 4 make a simbolic link between the directory test and current directory
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# 5 give the user and group file own permissions to all dir
sudo chown -R ubuntu:ubuntu /data

# 6 add a static web page in a certain path
sudo sed -i '38a location = /hbnb_static/ { \n alias data/web_static/current/;\n}' /etc/nginx/sites-enabled/default

# 7 restart nginx
sudo service nginx restart
