#!/bin/sh
sed  "s~BACKEND_URL~$BACKEND_URL~g" /etc/nginx/nginx.conf ;
nginx -g "daemon off;"