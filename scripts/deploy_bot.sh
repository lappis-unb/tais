#!/bin/bash

merged_branch=$3

if [[ ("$(git diff "remotes/origin/$merged_branch" remotes/origin/master -- . ':!web' | wc -l)" -ge 1) ]]; then
	sshpass  -p $1 ssh -o StrictHostKeyChecking=no root@$2 <<-'ENDSSH'
			cd rouana/
	    docker-compose -f ./beta.docker-compose.yml stop bot
			docker-compose -f ./beta.docker-compose.yml rm -f bot
	    docker rmi -f registry.gitlab.com/lappis-unb/services/tais/bot
	    docker-compose -f ./beta.docker-compose.yml up -d bot
	ENDSSH
fi
