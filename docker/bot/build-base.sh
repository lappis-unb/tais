#!/usr/bin/env bash


set -o errexit
set -o pipefail
set -o nounset

bot_image=bot:latest
coach_image=coach:latest

# Build base image
docker build . -f base_bot.Dockerfile -t $bot_image
docker build . -f base_coach.Dockerfile -t $coach_image

# Check if user wants to publish
if [ $# -eq 1 ]; then
    if [ "$1" = "publish" ]; then
        echo; echo; echo "PUBLISHING IMAGES"
        docker push $bot_image;
        docker push $coach_image;
    fi
else
    echo "Execute 'sh build.sh publish' to publish images"
fi
