train-nlu:
	python3 -m rasa_nlu.train -c nlu_config.yml --fixed_model_name current \
	 --data data/intents/ -o models --project nlu --verbose

train-core:
	python3 train.py 

train: train-nlu train-core

run-rocketchat:
	python3 run-rocketchat.py

run-api:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug \
  --port 5005 --enable_api

run-console:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug

train-online:
	python3 -m rasa_core.train -d domain.yml -s data/stories -o \
	models/dialogue --epochs 15 --online --nlu models/nlu/current/

evaluate:
	python3 -m rasa_core.evaluate -d models/dialogue -s data/core/

run-validator:
	python3 validator.py --intents data/intents/ --stories data/stories --domain domain.yml

# Force Makefile to execute e2e command every time
.PHONY: all e2e clean
e2e:
	python3 -m rasa_core.evaluate default --core models/dialogue --nlu models/nlu/current --stories e2e/e2e_stories.md --e2e
	python3 -m rasa_core.evaluate default --core models/dialogue --nlu models/nlu/current --stories e2e/e2e_stories_erro.md --e2e
