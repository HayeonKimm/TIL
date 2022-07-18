version: "3.9"
services:
  flask:
    build:
      context: .
    volumes:
      - ./templates:/templates
    ports:
      - "5000:5000"
  mongo:
    image: mongo:latest
    volumes:
      - mongo:/data/db/
    ports:
      - "27017:27017"

volumes:
  mongo:
