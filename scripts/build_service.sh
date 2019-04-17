#!/bin/bash

service_name=$1
current_branch=$2
image_name=$3
ci_job_token=$4
ci_registry=$5

build_image(){
	docker login -u "gitlab-ci-token" -p $ci_job_token $ci_registry

	docker build -f docker/bot.Dockerfile -t $image_name .
	docker push $image_name
}

if [[ ($service_name = "bot") && ("$(git diff "remotes/origin/$current_branch" remotes/origin/master -- . ':!web' | wc -l)" -ge 1) ]] ||
	 [[ ($service_name = "web") && ("$(git diff "remotes/origin/$current_branch" remotes/origin/master -- web | wc -l)" -ge 1) ]]; then
	echo "** Building image for service $service_name **"
	build_image
else
	echo "** Skip building for service $service_name since there is no update on code **"
fi
