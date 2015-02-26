upstream parser {
       server 127.0.0.1:9015;
}

server {
  listen 80;
  server_name parser.ru *.parser.ru;

  client_max_body_size 5M;
  access_log  /var/log/parser/nginx.access.log;
  error_log  /var/log/parser/nginx.error.log;

  location ^~ /static/js/tinymce/ {
        rewrite ^/static/js/tinymce/(.*)$ /$1 break;
        root /usr/share/tinymce/www;
        #access_log /v;
        expires  30d;
  }

  location ^~ /media {
     root  /var/www/parser/;
     access_log off;
     expires    30d;
  }

  location ~* ^.+\.(jpg|jpeg|gif|png|ico|css|doc|pdf|bmp|js|html|txt) {
   root         /usr/share/parser-static/;
   rewrite  ^/robots.txt$ /static/robots.txt;
   access_log   off;
   expires  30d;
  }

  location / {
    proxy_pass http://parser;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP   $remote_addr;
    proxy_set_header X-Forwarded-For  $remote_addr;

    proxy_redirect off;

    proxy_intercept_errors on;

    proxy_read_timeout 60s;
  }
}
