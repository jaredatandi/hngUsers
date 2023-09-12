# Use the official MySQL image as the base image
FROM mysql:latest

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=Users
ENV MYSQL_USER=db_user
ENV MYSQL_PASSWORD=db_password

# Expose MySQL port (default is 3306)
EXPOSE 3306

# Customize MySQL configuration (optional)
# COPY my.cnf /etc/mysql/my.cnf

# Run MySQL as a non-root user (optional)
# RUN usermod -d /var/lib/mysql/ mysql

# Copy SQL script to create the "users" table
COPY create_table.sql /docker-entrypoint-initdb.d/

# Start MySQL when the container starts
CMD ["mysqld"]
