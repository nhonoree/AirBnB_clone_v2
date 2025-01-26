#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

# Install Nginx if it's not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create the necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to the ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/
sudo sed -i '33i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart
