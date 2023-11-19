# build the react application
FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.25.2-alpine-slim

RUN rm /etc/nginx/conf.d/default.conf && rm /etc/nginx/nginx.conf && mkdir -p /var/www/static

COPY --from=build /app/static /var/www/static
COPY default.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/
