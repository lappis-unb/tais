run-rocketchat:
	python3 run-rocketchat.py

run-api:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug \
  --port 5005 --enable_api

run-console:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug

evaluate:
	python3 -m rasa_core.evaluate -d models/dialogue -s data/core/

run-validator:
	python3 validator.py --intents data/intents/ --stories data/stories --domain domain.yml

# Force Makefile to execute e2e command every time
.PHONY: all e2e clean
e2e:
	python3 -m rasa_core.evaluate default --core models/dialogue --nlu models/nlu/current --stories e2e/e2e_stories.md --e2e
	python3 -m rasa_core.evaluate default --core models/dialogue --nlu models/nlu/current --stories e2e/e2e_stories_erro.md --e2e
