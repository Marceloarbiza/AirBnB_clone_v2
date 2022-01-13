#!/usr/bin/env bash
# comment

apt update
apt install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
chown -R ubuntu /data
chgrp -R ubuntu /data
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default
service nginx restart
