FROM nginx:1.25.2-alpine-slim

RUN rm /etc/nginx/conf.d/default.conf && rm /etc/nginx/nginx.conf && mkdir -p /var/www/static

COPY ./static /var/www/static
COPY default.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/


