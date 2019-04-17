#!/bin/bash

sshpass  -p $1 ssh -o StrictHostKeyChecking=no root@$2 <<-'ENDSSH'   
    docker-compose stop $3
		docker-compose rm -f $3
    docker rmi -f $4
    docker-compose up -d $3
ENDSSH
