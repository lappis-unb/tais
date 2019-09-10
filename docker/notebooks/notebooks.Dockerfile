FROM lappis/botrequirements:tais


COPY ./docs/tutoriais/ /work/tutoriais/

RUN apt install -y graphviz libgraphviz-dev pkg-config

# Pygraphviz depends on package graphviz wich needs to be configurated
# acording to each OS. because of it it's not added to bot.requirements
RUN pip install --no-cache-dir jupyter pygraphviz==1.5
RUN pip install notedown
RUN jupyter nbextension install https://rawgit.com/jfbercher/jupyter_nbTranslate/master/nbTranslate.zip --user
RUN jupyter nbextension enable nbTranslate/main

WORKDIR /work/

CMD ["sh","-c","cd tutoriais/ && python checked_ipynb.py && cd /work && jupyter-notebook --allow-root --NotebookApp.token='' --ip=0.0.0.0 --NotebookApp.password=''"]
