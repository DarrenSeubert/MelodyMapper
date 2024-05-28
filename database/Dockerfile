FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=my_root_password
ENV MYSQL_DATABASE=mp_database
COPY init.sql /docker-entrypoint-initdb.d/
