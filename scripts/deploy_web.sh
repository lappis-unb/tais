#!/bin/bash

sshpass  -p $1 ssh -o StrictHostKeyChecking=no root@$2 <<-'ENDSSH'
		cd rouana/
    docker-compose stop web
		docker-compose rm -f web
		docker-compose pull web
    docker-compose up -d web
ENDSSH
