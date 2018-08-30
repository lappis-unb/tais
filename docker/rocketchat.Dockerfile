from python:3.6

run apt-get install -y git


run git clone https://github.com/lappis-unb/rasa_core.git  && \
    cd rasa_core                                           && \
    pip install -r requirements.txt                        && \
    pip install -e .

run pip install rasa-nlu[spacy]==0.13.0   && \
    python -m spacy download pt

run pip uninstall -y tensorflow && pip install tensorflow==1.5

run mkdir /tais

add ./tais /tais
workdir /tais

env TRAINING_EPOCHS=300                    \
    CREDENTIALS="/tais/credentials.yml"  \
    TAIS_PORT=5005

cmd python train-rocketchat.py
