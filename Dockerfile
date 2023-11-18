# build the react application
FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# now run the flask application
FROM python:3.9.6-alpine3.14

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY --from=build /app .

RUN chmod +x run.sh

CMD ["sh", "run.sh"]
