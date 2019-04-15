## end-to-end story 1
* cumprimentar: oi
   - utter_cumprimentar
* lei_rouanet_remuneracao_proponente: o proponente é remunerado?
   - utter_lei_rouanet_remuneracao_proponente
   - utter_continuar_conversa
* definicao_projeto: como se caracteriza um projeto?
    - utter_definicao_projeto
    - utter_continuar_conversa
* o_que_sei_falar: o que mais você sabe falar?
    - utter_o_que_sei_falar
* definicao_minc: o que significa MINC?
    - utter_definicao_minc
    - utter_objetivo
* negar: não
   - utter_continuar_conversa
* lei_rouanet_o_que_eh: me fale sobre a lei rouanet
   - utter_lei_rouanet_o_que_eh
   - utter_continuar_conversa
* negar: não obrigado
   - utter_despedir

## end-to-end story 2
* cumprimentar: ola
   - utter_cumprimentar
* lei_rouanet_quem_pode_incentivar: qualquer empresa pode se beneficiar ao apoiar um projeto?
   - utter_lei_rouanet_quem_pode_incentivar
   - utter_continuar_conversa
* definicao_vinculada: o que é vinculada?
   - utter_definicao_vinculada
   - utter_objetivo
* negar: não
   - utter_continuar_conversa
* lei_rouanet_promocao_de_marca: eu posso divulgar a logo do patrocinador?
   - utter_lei_rouanet_promocao_de_marca
   - utter_continuar_conversa
* lei_rouanet_beneficios_incentivo_projetos_culturais: quem tem o beneficio fiscal?
   - utter_lei_rouanet_beneficios_incentivo_projetos_culturais
   - utter_continuar_conversa
* negar: não obrigado
   - utter_despedir

## end-to-end story 3
* lei_rouanet_o_que_eh: me fale sobre a lei rounet 
   - utter_lei_rouanet_o_que_eh
   - utter_continuar_conversa
* lei_rouanet_etapas_aprovacao_projeto: quais são as etapas de aprovação de projeto
   - utter_lei_rouanet_etapas_aprovacao_projeto
   - utter_continuar_conversa
* lei_rouanet_analise_tecnica: #análisetecnica
   - utter_lei_rouanet_analise_tecnica
   - utter_continuar_conversa
* processo_como_funciona: como enviar uma proposta?
   - utter_processo_como_funciona
* afirmar: sim
   - utter_cadastro_salic_video
* negar: não
   - utter_salic_cadastro_proponente
   - utter_continuar_conversa
* negar: não, obrigado
   - utter_despedir

## end-to-end story 4
* tudo_bem: tudo bem?
    - utter_tudo_bem
    - utter_menu
* definicao_salic: O que é o Salic?
    - utter_definicao_salic
    - utter_objetivo
* negar: não
    - utter_continuar_conversa
* lei_rouanet_o_que_eh: o que é a lei rouanet?
    - utter_lei_rouanet_o_que_eh
    - utter_continuar_conversa
* processo_como_funciona: como fazer um projeto?
    - utter_processo_como_funciona
* negar: não
    - utter_continuar_conversa
* tem_wpp: tem whatsapp?
    - utter_tem_wpp
    - utter_objetivo
* afirmar: sim
    - utter_processo_como_funciona
* negar: não obrigado
    - utter_continuar_conversa
* despedir: nada, obrigado tais
    - utter_despedir