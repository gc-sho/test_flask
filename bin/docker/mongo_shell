#!/usr/bin/env bash

source lib/functions

echo -e ""

echo "Opening Mongo shell..."
if container_exists test-flask-mongo; then
  echo "Mongo shell"
  docker exec -it test-flask-mongo mongo
fi

if !container_exists test-flask-mongo; then
  echo "Please start your mongo container (test-flask-mongo)"
fi