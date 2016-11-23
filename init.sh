sudo rm /etc/nginx/sites-enabled/test.conf
sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
﻿sudo /etc/init.d/mysql restart﻿
# /home/box/web sudo gunicorn - b 0.0.0.0:8080 hello:app 
