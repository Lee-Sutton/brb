FROM nginx:1.15.0-alpine

COPY ./data/certbot/conf /etc/letsencrypt
COPY ./data/certbot/www /var/www/certbot

RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/production/nginx/nginx.conf /etc/nginx/conf.d
