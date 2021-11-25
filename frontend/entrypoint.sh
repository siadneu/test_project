#!/bin/sh
sed -i "s~BACKEND_URL~`echo $BACKEND_URL`~g" /etc/nginx/nginx.conf ;
cat /etc/nginx/nginx.conf ;
nginx -g "daemon off;"