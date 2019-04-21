#!/bin/bash

sshpass  -p $1 ssh -o StrictHostKeyChecking=no root@$2 <<-'ENDSSH'
		cd rouana/
    docker-compose -f ./beta.docker-compose.yml stop web
		docker-compose -f ./beta.docker-compose.yml rm -f web
    docker rmi -f registry.gitlab.com/lappis-unb/services/tais/web
    docker-compose -f ./beta.docker-compose.yml up -d web
ENDSSH
