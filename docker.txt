# To build a Docker image, use the following command:
docker build -t <image_name>:<tag> .

# Replace <image_name> with the desired name for your image.
# Replace <tag> with the version tag (e.g., "latest").
# The '.' at the end specifies the current directory as the build context.

# Example:
docker build -t myfullstack .

docker-compose up --build


container ke ander kaise aaye
docker ps -a 

dockke exec -it container_id bash
docker exec -it <container_id> bash


#enter the postgres sql
psql -U postgres -d postgres
psql -U <username> -d <database_name>
\dt === show all table

select * from your_table_name
