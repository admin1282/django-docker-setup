>>docker compose -f docker-compose.dev.yml up -d


# for check images
 >>docker compose -f docker-compose.dev.yml ps
 
# access bash 
 >> docker compose -f docker-compose.dev.yml exec project_name bash
 

# if do you want to setup mannuly migration and migrate use
 >>docker-compose -f docker-compose.dev.yml up -d --build
 > 
> If you're making changes to your local code and you want those changes to reflect in your Docker container, you'll need to rebuild the container after making the changes. Simply running docker-compose -f docker-compose.dev.yml up -d won't rebuild the container automatically.
> 
'''The --build flag tells Docker Compose to rebuild the container before starting it. This ensures that any changes in your local code are reflected in the container.'''


# use for old images delete
 >>docker image prune
 > 
# use for stop container

>> docker compose -f docker-compose.dev.yml stop
