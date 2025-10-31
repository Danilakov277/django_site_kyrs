#!/bin/bash

echo "Starting deployment..."

# Pull latest changes
git pull origin main

# Build and start containers
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

echo "Deployment completed!"