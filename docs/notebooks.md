---
layout: page
permalink: /notebooks/
title: Notebooks com Jupyter

---
## Utilizando notebooks para avaliar o chatbot RASA

### - Detalhando os problemas encontrados ao projetar conteúdo e diálogo de Chatbots:

Inicialmente, um dos maiores problemas encontrados no projeto do chatbot foi a      incompatibilidade de respostas oferecidas pelo bot às perguntas do usuário durante as conversas. Ou seja, o usuário formulava uma pergunta, a resposta estava mapeada na base de conhecimento do robô, e mesmo assim a resposta dada é incorreta ou inconclusiva (fallback). Foi necessário entender o motivo desse problema e como melhorá-lo para poder deixar o chatbot mais eficiente. Outro problema identificado foi a dificuldade do bot de seguir os fluxos de conversas criados nos arquivos de stories. Uma vez que o usuário interagia com o bot ele não seguia o fluxo padrão programado segundo as intenções de usuário identificadas. Sendo assim necessário identificar o motivo dessas variações de fluxo.

Durante o desenvolvimento da Tais, chatbot do Ministério da Cultura, vários estudos e testes foram realizados visando a alcançar melhores resultados de conversação a fim de melhorar a experiência do usuário ao utilizar a tecnologia Rasa, um framework para a construção de software conversacional, no desenvolvimento dessas estruturas, intents e stories.

Logo, foi necessário identificar quais melhorias deveriam ser feitas nos arquivos de stories e intents para melhorar a interação bot e usuário.




### - Resolvendo os problemas por meio da utilização de uma abordagem datascience - via notebooks:

O Jupyter foi a ferramenta escolhida para executar os scripts de análise dos datasets e treinamentos do chatbot. O objetivo é identificar os problemas de interações com o chatbot antes de colocar o conteúdo em produção, com a criação de notebooks mais interativos e explicativos para analisar os problemas.

Para facilitar a análise das intents e stories criadas que estão sendo utilizadas no chatbot, foram implementados nos notebooks scripts para gerar gráficos utilizando as bibliotecas Rasa Core e Rasa NLU. Dessa forma se torna fácil avaliar quais intents ou stories estão mal formuladas ao observar o resultado dos gráficos.

A utilização de notebooks também torna essa avaliação mais fácil, ao mostrar todas as imagens e gráficos em um só lugar, além de poder conter explicações que auxilia na sua utilização.

* **Notebook de avaliação de intents:**

    Inicialmente, a primeira implementação do notebook como meio de auxílio na análise do desenvolvimento da Tais tem como objetivo a avaliação das anotações de intents programadas do usuário, a fim de torná-las mais eficientes em termos de identificação e consequentemente retorno da utter adequada.
    
    Para realizar o treinamento do modelo Rasa NLU, todas as intents na pasta foram utilizadas para gerar os gráficos de avaliação do bot afim de treinar o modelo e executar a avaliação que pode ser verificada na imagem abaixo por meio da matriz de confusão que disponibiliza o resultado dos conflitos de intenções a cada treino.

    <img src="../assets/matriz_confusao.png" width="1000"/>


    A matriz de confusão gerada possibilita, de acordo com a quantidade de intenções criadas, identificar a quantidade de intenções que estão parecidas ou iguais e que oferece problemas quanto a identificação da mesma. Para isso foi padronizado uma quantidade específica de 20 exemplos divididos em 10 frases e 10 junções de palavras chaves utilizadas para cada uma das intenções.

    Outra possibilidade de avaliação é a de testar mensagens específicas, para que seja possível ter acesso ao nome da intenção e ao percentual de confiabilidade ao qual possui determinada mensagem, como é mostrado abaixo:

    - **Entrada**

    ``
    pprint(interpreter.parse('posso terceirizar a captação de recursos?'))
    ``

    - **Saída**

        {

            "intent": {
                "name": "captacao_quando_captar",
                "confidence": 0.7346936464309692
            },
            "entities": [],
            "intent_ranking": [
            {
                "name": "captacao_quando_captar",
                "confidence": 0.7346936464309692
            },
            {
                "name": "captacao_como_captar",
                "confidence": 0.6702125668525696
            }
        }
        

* **Notebook de avaliação de stories:**

    O notebook de avaliação de stories tem como objetivo principal analisar o fluxo das histórias programadas, de forma a gerar uma boa visualização dos fluxos implementados e encontrar possíveis falhas, como confusão entre fluxos ou um fluxo mal esquematizado.

    Essa forma de avaliação gera imagens que trazem uma boa visualização do fluxo de conversas do bot como apresentado na imagem abaixo:

    <img src="../assets/fluxo_stories.png" width="1000"/>

    Outra etapa foi gerar a matriz de confusão para avaliar possíveis problemas nos fluxos de histórias ao identificar qual utter deve ser disparada no qual mostra as possíveis falhas onde o chatbot pode se confundir no fluxo. Como a imagem abaixo.

    <img src="../assets/matriz_stories.png" width="1000"/>

    Essa matriz avalia a classificação de cada story, assim como o policy usado para a gestão do diálogo,  e  qual utter é apresentada para o usuário, a partir de uma intent de entrada, e o histórico da conversa. 
    
    Para avaliar se suas histórias estão com a classificação correta, basta visualizar as áreas em azul, estas áreas mostram quais utters estão sendo previstas pelo chatbot. Se somente a diagonal da matriz está em azul, significa que não há erro na classificação, as histórias estão bem estruturadas, caso o contrário, o fluxo está mal formulado, fazendo com que o bot entre em fluxos errados.

	Todas as imagens geradas, além de serem exibidas no notebook, são salvas, podendo assim fazer uma melhor análise caso necessário.
	A utilização dessas ferramentas no notebook que gera todas essas imagens e gráficos que nos auxiliaram a avaliar o nosso dataset de treinamento. Eles mostram tanto anotações de intents que possam dificultar a classificação, quanto das de ambiguidades nos fluxos de diálogo. Além disso, é possível otimizar a criação de novos fluxos, a partir da visualização dos fluxos já existentes assim como a forma como se relacionam.
