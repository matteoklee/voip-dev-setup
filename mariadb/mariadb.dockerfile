FROM mariadb:10.5

#Copy the config file onto the Filesystem of the Docker instance
COPY my.cnf /etc/mysql/
ADD create_db.sql /docker-entrypoint-initdb.d
ADD kamailio_tables.sql /docker-entrypoint-initdb.d
ADD create_user.sql /docker-entrypoint-initdb.d
ADD kamailio_users.sql /docker-entrypoint-initdb.d

#Expose port 3306 (mysql) for TCP
EXPOSE 3306
