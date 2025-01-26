#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

# Update package lists and install Nginx if not already installed
sudo apt-get update -y
sudo apt-get install -y nginx

# Create required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or update the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of the /data/ directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ via hbnb_static
sudo sed -i '/server_name _;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart

# Exit successfully
exit 0
