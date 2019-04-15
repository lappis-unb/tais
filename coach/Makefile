train-nlu:
	python3 -m rasa_nlu.train -c nlu_config.yml --fixed_model_name current \
	 --data data/intents/ -o /src_models --project nlu --verbose

train-core:
	python3 train.py 

train: train-nlu train-core

train-online:
	python3 -m rasa_core.train -d domain.yml -s data/stories -o \
	models/dialogue --epochs 15 --online --nlu models/nlu/current/
