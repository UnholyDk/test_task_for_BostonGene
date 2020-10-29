#!/bin/bash
docker-compose build && docker-compose up -d server && docker-compose run pytest && docker-compose down