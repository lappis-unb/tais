run-rocketchat:
	python3 run-rocketchat.py

run-console:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug \
	--endpoints endpoints.yml
	
run-api:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current \
	--endpoints endpoints.yml --debug --enable_api --port 5005

evaluate:
	python3 -m rasa_core.evaluate -d models/dialogue -s data/core/

# Force Makefile to execute e2e command every time
.PHONY: all e2e clean
e2e:
	python3 -m rasa_core.evaluate default --core models/dialogue \
	--nlu models/nlu/current --stories e2e/e2e_stories_1.md --e2e
	python3 -m rasa_core.evaluate default --core models/dialogue \
	--nlu models/nlu/current --stories e2e/e2e_stories_2.md --e2e

e2e-test:	
	python3 -m rasa_core.evaluate default --core models/dialogue \
	--nlu models/nlu/current --stories e2e/e2e_stories_erro.md --e2e
