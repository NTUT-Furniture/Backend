FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=NFT
ENV MYSQL_USER=backend
ENV MYSQL_PASSWORD=backend

COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

EXPOSE 3306