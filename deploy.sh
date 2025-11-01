#!/bin/bash
echo "🚀 Starting deployment..."
git pull origin main
docker-compose down
docker-compose build --no-cache
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --noinput
echo "✅ Deployment complete!"
echo "🌐 Site: http://46.17.102.12:8000"
