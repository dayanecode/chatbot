from ..models import Pergunta, Resposta
def obterPerguntaPrincipal():
    pergunta = Pergunta()
    pergunta.codigo = 1
    pergunta.titulo = "Posso ajudar você?"

    resposta1 = Resposta()
    resposta1.codigo = 1
    resposta1.valor = 'O que é ESG?'
    resposta1.descricao = "A sigla ESG abrevia as palavras environmental, social and corporate governance, " \
                          "que podem ser traduzidas como meio ambiente, sociedade e governança. " \
                          "O objetivo é pensar estratégias e adotar políticas na empresa que engloba esses três " \
                          " e cooperem para um ambiente sustentável, não somente no que tange à ecologia," \
                          " mas sim na criação de um ecossistema que cause cada vez menos impactos negativos à sociedade como um todo."
    resposta1.acao = "\esg"

    # ------------------------ Preencher ------------------------
    resposta2 = Resposta()
    resposta2.codigo = 2
    resposta2.valor = 'Como a plataforma Greenfield pode ajudar minha empresa a adotar práticas ESG?'
    resposta2.descricao = "EscreverResposta// Desculpe, ainda não sei a resposta para isso... Mas não se preocupe!" \
                           "Avise meus desenvolvedores para me ensinar o quanto antes!"
    resposta2.acao = "\greenfield-adotar-esg"

    resposta3 = Resposta()
    resposta3.codigo = 3
    resposta3.valor = 'Quais são as métricas ESG mais relevantes para minha empresa?'
    resposta3.descricao = "Separadas em 3 pilares, são elas: "\
"1 - Meio ambiente: considera a relação entre investimento e impacto, e pode abranger tópicos como" \
                          " a maneira com a qual a empresa lida com seu lixo, a emissão de carbono, o emprego de químicos," \
                          " a utilização de recursos como energia e água, entre outros." \
"2 - Sociedade: esse tópico trata das relações sociais da empresa – como os funcionários são tratados? " \
                          "Como funciona a inclusão e a acessibilidade de indivíduos de diferentes etnias e classes sociais," \
                          " LGBQIA+ e pessoas com deficiência? Qual a relação entre a empresa e o ecossistema em que ela está inserida?" \
"3 - Governança: se refere às mudanças positivas geradas pela empresa, como colaboradores bem remunerados, diversidade na liderança," \
                          " bom relacionamento com fornecedores e acionistas, recusa a práticas corruptas e cumprimento de obrigações legais."
    resposta3.acao = "\metricas-esg"

    resposta4 = Resposta()
    resposta4.codigo = 4
    resposta4.valor = 'Como podemos definir metas ESG para nossa empresa?'
    resposta4.descricao = "Você pode revisar os processos da empresa, investir em práticas ecológicas, " \
                          "definir propósito, missão e valores, criar grupos de discussão, e definir indicadores de desempenho."
    resposta4.acao = "\definir-metricas-esg"

    resposta5 = Resposta()
    resposta5.codigo = 5
    resposta5.valor = 'Quais são as tendências do mercado em relação ao ESG?'
    resposta5.descricao = "Melhores condições de trabalho e mercado de carbono são uma das principais tendências. " \
                          "Nos próximos anos, haja vista que a flexibilização do trabalho ganhou força nas empresas " \
                          "e até novos benefícios passaram a ser incluídos com a finalidade de reter talentos e manter os colaboradores motivados."
    resposta5.acao = "\tendencias-esg"

    # ------------------------ Preencher ------------------------
    resposta6 = Resposta()
    resposta6.codigo = 6
    resposta6.valor = 'Como a Greenfield avalia e monitora o desempenho ESG de uma empresa?'
    resposta6.descricao = "EscreverResposta// Desculpe, ainda não sei a resposta para isso... Mas não se preocupe!" \
                           "Avise meus desenvolvedores para me ensinar o quanto antes!"
    resposta6.acao = "\greenfield-monitora-esg"

    resposta7 = Resposta()
    resposta7.codigo = 7
    resposta7.valor = 'Quais são as melhores práticas para a implementação de um programa de sustentabilidade em uma empresa?'
    resposta7.descricao = "Adotar práticas sustentáveis em sua empresa vai fazer com que " \
                          "ela seja ainda mais valorizada pelos clientes que lhe acompanham, " \
                          "e vai fazer com que você conquiste ainda mais consumidores para " \
                          "que o seu negócio cresça de forma sempre positiva.Veja 10 delas:" \
                                "1 - Restrinja o uso de copos descartáveis;" \
                                "2 - Economize papel, água e energia;" \
                                "3 - Invista na reciclagem;" \
                                "4 - Utilize equipamentos econômicos;" \
                                "5 - Incentive o uso de transportes alternativos;" \
                                "6 - Invista e implante treinamentos sobre sustentabilidade;" \
                                "7 - Crie projetos de preservação do meio ambiente;" \
                                "8 - Respeite as leis ambientais;" \
                                "9 - Não polua o meio ambiente;" \
                                "10 - Utilize fontes de energia re nováveis."
    resposta7.acao = "\implementacao-sustentabilidade"

    # ------------------------ Preencher ------------------------
    resposta8 = Resposta()
    resposta8.codigo = 8
    resposta8.valor = 'Como a Greenfield pode ajudar a melhorar a cultura de sustentabilidade em minha empresa?'
    resposta8.descricao = "EscreverResposta// Desculpe, ainda não sei a resposta para isso... Mas não se preocupe!" \
                           "Avise meus desenvolvedores para me ensinar o quanto antes!"
    resposta8.acao = "\greenfield-sustentabilidade-empresa"

    resposta9 = Resposta()
    resposta9.codigo = 9
    resposta9.valor = 'Como posso criar um plano de ação para melhorar o desempenho ESG da minha empresa?'
    resposta9.descricao = "Seguem abaixo sete passos que irão auxiliar sua empresa a entrar nessa promissora jornada, " \
                          "rumo a um mundo corporativo de maior autorresponsabilidade e menor surpresa:" \
	                            "1 - Tenha em mente um programa específico de trabalho;" \
	                            "2 - Crie uma política alinhada a sua visão e valores;" \
	                            "3 - Defina local points para cada pilar ESG;" \
	                            "4 - Faça um brainstorm completo para compilar os riscos existentes;" \
	                            "5 - Crie uma priorização dos riscos inventariados;" \
	                            "6 -  Trabalhar nas três frentes de trabalho : Pessoas, processos e sistemas de gestão;" \
	                            "7 - Estar atento aos Resultados."
    resposta9.acao = "\desempenho-esg"

    # ------------------------ Preencher ------------------------
    resposta10 = Resposta()
    resposta10.codigo = 10
    resposta10.valor = 'Como posso acessar relatórios de desempenho ESG gerados pela plataforma Greenfield?'
    resposta10.descricao = "EscreverResposta// Desculpe, ainda não sei a resposta para isso... Mas não se preocupe!" \
                           "Avise meus desenvolvedores para me ensinar o quanto antes!"
    resposta10.acao = "\greenfield-relatorios-esg"

    # ------------------------ Preencher ------------------------
    resposta11 = Resposta()
    resposta11.codigo = 11
    resposta11.valor = 'Como começar?'
    resposta11.descricao = "EscreverResposta// Desculpe, ainda não sei a resposta para isso... Mas não se preocupe!" \
                           "Avise meus desenvolvedores para me ensinar o quanto antes!"
    resposta11.acao = "\greenfield-comecar"

    # ------------------------ Preencher ------------------------
    resposta12 = Resposta()
    resposta12.codigo = 12
    resposta12.valor = 'O que é RPG?'
    resposta12.descricao = "EscreverResposta// Desculpe, ainda não sei a resposta para isso... Mas não se preocupe!" \
                           "Avise meus desenvolvedores para me ensinar o quanto antes!"
    resposta12.acao = "\greenfield-rpg"

    # ------------------------ Preencher ------------------------
    resposta13 = Resposta()
    resposta13.codigo = 13
    resposta13.valor = 'Como funciona um RPG?'
    resposta13.descricao = "EscreverResposta// Desculpe, ainda não sei a resposta para isso... Mas não se preocupe!" \
                           "Avise meus desenvolvedores para me ensinar o quanto antes!"
    resposta13.acao = "\greenfield-funcionamento-rpg"

    # ------------------------ Preencher ------------------------
    resposta14 = Resposta()
    resposta14.codigo = 14
    resposta14.valor = 'O que é gamificação?'
    resposta14.descricao = "EscreverResposta// Desculpe, ainda não sei a resposta para isso... Mas não se preocupe!" \
                           "Avise meus desenvolvedores para me ensinar o quanto antes!"
    resposta14.acao = "\greenfield-gamificacao"

    # ------------------------ Preencher ------------------------
    resposta15 = Resposta()
    resposta15.codigo = 15
    resposta15.valor = 'Como funciona a gamificação?'
    resposta15.descricao = "EscreverResposta// Desculpe, ainda não sei a resposta para isso... Mas não se preocupe!" \
                           "Avise meus desenvolvedores para me ensinar o quanto antes!"
    resposta15.acao = "\greenfield-funcionamento-gamificação"


    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()
    resposta4.save()
    resposta5.save()
    resposta6.save()
    resposta7.save()
    resposta8.save()
    resposta9.save()
    resposta10.save()
    resposta11.save()
    resposta12.save()
    resposta13.save()
    resposta14.save()
    resposta15.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)
    pergunta.respostas.add(resposta4)
    pergunta.respostas.add(resposta5)
    pergunta.respostas.add(resposta6)
    pergunta.respostas.add(resposta7)
    pergunta.respostas.add(resposta8)
    pergunta.respostas.add(resposta9)
    pergunta.respostas.add(resposta10)
    pergunta.respostas.add(resposta11)
    pergunta.respostas.add(resposta12)
    pergunta.respostas.add(resposta13)
    pergunta.respostas.add(resposta14)
    pergunta.respostas.add(resposta15)

    return pergunta