#!/bin/bash

sshpass  -p $1 ssh -o StrictHostKeyChecking=no root@$2 <<-'ENDSSH'
    cd rouana/
    docker-compose stop bot
		docker-compose rm -f bot
		docker-compose pull bot
    docker-compose up -d bot
ENDSSH
