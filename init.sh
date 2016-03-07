#!/bin/bash
#/etc/nginx/nginx.conf - config nginx
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/alexandr/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
