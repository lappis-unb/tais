FROM lappis/coach:latest as coach

FROM lappis/botrequirements:latest

COPY ./bot /bot
COPY --from=coach /src_models/ /models/
COPY ./scripts /scripts

WORKDIR /bot

ENV ROCKETCHAT_URL=rocketchat:3000         \
    MAX_TYPING_TIME=10                     \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ROCKETCHAT_ADMIN_USERNAME=admin        \
    ROCKETCHAT_ADMIN_PASSWORD=admin        \
    ROCKETCHAT_BOT_USERNAME=tais           \
    ROCKETCHAT_BOT_PASSWORD=tais           \
    ENVIRONMENT_NAME=localhost             \
    BOT_VERSION=last-commit-hash           \
    ENABLE_ANALYTICS=False                 \
    ELASTICSEARCH_URL=elasticsearch:9200   

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
