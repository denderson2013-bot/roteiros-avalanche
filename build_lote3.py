import json

# Read current file
with open('/tmp/roteiros-edit/roteiros.json') as f:
    data = json.load(f)

# Define all 15 rewritten roteiros (indices 25-39)
new_roteiros = []

# ============================================================
# INDEX 25 - Gartner: 20% das empresas eliminando gerência média
# ============================================================
r25 = {
    "ato1_gancho": "Sabe qual cargo tá sendo extinto em 2026? Não é operário. Não é estagiário. Não é recepcionista. É gerente. A Gartner, maior consultoria de tecnologia do mundo, confirmou essa semana que 20% das grandes empresas já estão usando inteligência artificial pra eliminar mais da metade dos cargos de gerência média. Vinte por cento. E não é previsão. É dado real, coletado de empresas que já fizeram o corte. Se você é gerente, coordenador ou supervisor, esse vídeo vai te tirar o sono. Se você é dono de empresa, vai te dar ideias perigosas.",

    "ato2_buraco": "Pensa comigo no que um gerente médio faz no dia a dia. Cobra relatório. Monitora performance. Organiza agenda do time. Repassa informação de cima pra baixo e de baixo pra cima. Filtra dados. Manda email cobrando prazo. Agenda reunião pra falar sobre outra reunião. Agora olha essa lista de novo e me diz: qual dessas tarefas um agente de IA não faz melhor, mais rápido e sem reclamar? A resposta é nenhuma. O agente monitora em tempo real. Gera relatório instantâneo. Prioriza tarefas automaticamente. Manda alerta pro diretor sem precisar de intermediário. A camada do meio existia porque a informação precisava de tradutor. A IA eliminou a necessidade de tradução. E junto com ela, eliminou o tradutor. A Gartner projeta que até 2028, 50% das organizações vão ter achatado suas hierarquias especificamente por causa de agentes de IA. Cinquenta por cento. Não é um departamento perdendo gente. É a estrutura inteira da empresa mudando de forma.",

    "ato3_virada": "E aqui é onde a história muda pra quem tem visão. Porque enquanto gerente tá com medo de perder o emprego, dono de empresa tá calculando quanto economiza. Eu vivi isso na pele. Tinha uma operação comercial com 37 vendedores. Folha entre 90 e 120 mil reais por mês. No meio disso, três coordenadores, dois supervisores, um gerente comercial. Seis pessoas só pra garantir que os outros 31 fizessem o trabalho deles. E sabe o que eu descobri quando comecei a olhar os números de verdade? Os 6 da gerência média custavam quase 40% da folha. E o resultado que entregavam era informação que eu podia ter num dashboard em tempo real. Quando coloquei agentes de IA pra atender, qualificar e fazer follow-up 24 horas, a primeira coisa que ficou óbvia foi: eu não precisava mais de ninguém cobrando ninguém. O agente não precisa de supervisor. Não atrasa relatório. Não esquece de mandar o status.",

    "ato4_caos": "Mas antes de você achar que foi tudo lindo, deixa eu te contar o que aconteceu no meio do caminho. Quando eu comecei a transição, os coordenadores entraram em pânico. Um deles, cara que tava comigo há 3 anos, começou a sabotar o processo. Desligava automação. Mudava configuração do CRM. Falava pro time que a IA ia dar errado e que era melhor continuar no manual. Em duas semanas, a operação virou um caos. Lead caindo sem resposta. Agente mandando mensagem duplicada porque alguém tinha mexido nas regras. Cliente ligando pra reclamar que recebeu proposta errada. Eu perdi 14 vendas confirmadas num único mês por causa da sabotagem. Quase desisti. Sentei na cadeira do escritório às 2 da manhã pensando que tinha cometido o maior erro da minha vida. Que talvez a estrutura antiga, com toda a gordura, era melhor que essa bagunça nova.",

    "ato5_cta": "Só que eu não voltei atrás. Reconstruí do zero. Processo antes de tecnologia. Regras claras pro agente. Supervisão humana nos pontos críticos. E o mais importante: conversa honesta com o time. Quem queria ficar, ficou numa função que fazia sentido. Quem não queria se adaptar, saiu. Em 60 dias, a operação tava rodando melhor do que nunca. Atendimento 24 horas. Lead respondido em 3 segundos. Qualificação automática com 94% de precisão. Folha caiu 80%. Se você é dono de empresa e sente que tem gente demais fazendo trabalho que máquina faz melhor, faz o quiz de maturidade em IA. Link na bio. São 2 minutos. Você descobre onde tá, o que precisa mudar primeiro e como fazer sem explodir a operação no caminho.",

    "ato6_recompensa": "Hoje são mais de 30 empresas rodando com esse modelo. Clínica que tinha coordenadora de atendimento ganhando 5 mil por mês pra repassar mensagem de paciente pro dentista. Agora o agente faz a triagem, agenda e confirma sozinho. Faculdade que tinha supervisor de matrícula controlando planilha de Excel no braço. Agora o agente qualifica o aluno, manda proposta personalizada e fecha matrícula sábado de madrugada. Farmácia, escola, loja, agência. O padrão é sempre o mesmo: a camada do meio era um gargalo disfarçado de estrutura. Quando tira, a informação flui direto, a decisão acontece mais rápido e o custo despenca. A Gartner confirmou o que essas empresas já vivem na prática. A gerência média tá sendo substituída. Não por outra pessoa. Por inteligência que não dorme, não falta e não cobra aumento.",

    "ato7_fechamento": "Manda esse vídeo pro gerente que acha que tá seguro porque sempre entregou resultado. Porque a Gartner não tá falando de gerente ruim. Tá falando de gerente. Ponto. A função tá sumindo. E quem não se reposicionar agora vai descobrir tarde demais."
}

tel25 = "\n\n".join([r25[k] for k in r25])
words25 = len(tel25.split())

# ============================================================
# INDEX 26 - Microsoft Copilot Cowork
# ============================================================
r26 = {
    "ato1_gancho": "A Microsoft matou o conceito de assistente virtual. Morreu. Acabou. Dia 9 de março eles lançaram o Copilot Cowork e mudaram as regras do jogo pra sempre. Não é mais aquele chatbotzinho que responde pergunta. É um agente que pega um projeto inteiro e executa sozinho por horas. Sem supervisão. Sem precisar de você olhando por cima do ombro. Ele lê seus emails, analisa suas planilhas, monta apresentação, prepara reunião e te entrega tudo pronto. Se você tem empresa e ainda usa gente pra fazer trabalho repetitivo, esse vídeo vai te provocar.",

    "ato2_buraco": "Deixa eu explicar o que mudou de verdade. Até agora, o Copilot era reativo. Você perguntava, ele respondia. Tipo um estagiário digital. Agora ele virou proativo. A Microsoft criou uma camada chamada Work IQ que mapeia como você trabalha, quais documentos você usa, com quem você se reúne, quais emails você prioriza. E com base nisso, o agente antecipa tarefas. Antes de você pedir, ele já tá fazendo. E o mais pesado: ele usa Claude da Anthropic junto com os modelos da OpenAI. Dois dos cérebros mais avançados do planeta trabalhando dentro do seu Office. A Microsoft tá dizendo que uma pessoa com Copilot Cowork entrega o que antes precisava de um time de 4 ou 5. Não é promessa. É o produto. Tá disponível. Empresas já estão testando. E os primeiros relatórios mostram redução de 35% no tempo gasto com tarefas administrativas na primeira semana de uso.",

    "ato3_virada": "E aqui é onde a ficha cai pra quem tem empresa no Brasil. Porque se a Microsoft tá vendendo isso pra Fortune 500, quanto tempo até chegar na sua concorrência? A resposta é: já chegou. Eu entendi essa lógica antes da Microsoft empacotar num produto. Quando eu olhava pra minha operação com 37 vendedores, o que eu via era gente gastando 60% do tempo com tarefa que não era vender. Preencher CRM, mandar follow-up, montar proposta, organizar agenda. Trabalho operacional que consumia o dia inteiro e deixava o vendedor esgotado pra hora que realmente importava: a conversa com o cliente. Coloquei agentes de IA pra fazer tudo que não era conversa de fechamento. O vendedor virou closer. O agente virou o backoffice inteiro.",

    "ato4_caos": "Mas o caminho não foi reto. Quando liguei os agentes pela primeira vez, sem processo estruturado, o resultado foi desastroso. O agente mandou proposta com preço errado pra um cliente de 200 mil reais por ano. O cliente ligou furioso. Quase perdi o contrato. Outro agente respondeu um lead com informação que era de outro cliente. Dados cruzados. O lead printou e postou num grupo de WhatsApp com 300 pessoas dizendo que a empresa era amadora. Minha reputação levou um tapa. Em 10 dias eu tive 3 crises sérias. Time desconfiado, cliente bravo, lead perdido. Meu sócio chegou pra mim e falou: desliga essa porcaria antes que a gente quebre. E por um segundo, eu quase concordei. Quase voltei pro modelo antigo, com toda a ineficiência, mas pelo menos previsível.",

    "ato5_cta": "Não voltei. Parei tudo, mapeei cada falha, montei processo do zero. Regra clara pra cada agente. Supervisão humana em ponto crítico. Teste com 3 clientes antes de escalar. Em 45 dias a operação tava rodando com precisão cirúrgica. Lead respondido em 3 segundos, 24 horas por dia. Qualificação automática. Follow-up sem falha. Proposta personalizada sem erro. O que a Microsoft tá lançando agora, essas empresas já vivem há meses. Se você quer entender como montar essa operação sem passar pelo caos que eu passei, faz o quiz de maturidade em IA. Link na bio. 2 minutos. Você sai sabendo exatamente o passo que precisa dar primeiro.",

    "ato6_recompensa": "Hoje mais de 30 empresas rodam com agentes nesse modelo. Não são startups de tecnologia. São negócios brasileiros reais. Clínica que antes precisava de 4 recepcionistas pra dar conta do WhatsApp agora opera com 1 e um agente que atende de madrugada. Faculdade que perdia matrícula porque secretaria não trabalhava fim de semana agora fecha vaga domingo às 23h. A Microsoft tá vendendo a ideia de que IA trabalha por você. Essas empresas já compraram a ideia, implementaram e viram o resultado no caixa. O Copilot Cowork é a confirmação de que o que era vantagem competitiva vai virar requisito básico.",

    "ato7_fechamento": "Manda esse vídeo pra aquele empresário que ainda usa gente pra fazer o que máquina faz melhor. Porque a Microsoft não lançou um produto. Lançou um recado: o assistente morreu. Quem não trocar por agente vai ficar pra trás."
}

tel26 = "\n\n".join([r26[k] for k in r26])
words26 = len(tel26.split())

# ============================================================
# INDEX 27 - Deloitte: 75% das empresas investindo em IA agêntica
# ============================================================
r27 = {
    "ato1_gancho": "De cada 100 aplicativos que você usa hoje, 5 têm inteligência artificial de verdade. Até dezembro, 40 vão ter. Esse dado saiu essa semana no relatório da Deloitte. E se você não entendeu a gravidade, eu traduzo: em 8 meses, o número de apps com agentes de IA vai multiplicar por 8. O Goldman Sachs projeta mais de 500 bilhões de dólares investidos em IA agêntica só esse ano. Quinhentos bilhões. Esse dinheiro não tá indo pra chatbot. Tá indo pra agentes que executam, vendem, atendem e tomam decisão.",

    "ato2_buraco": "O relatório da Deloitte entrevistou milhares de executivos de empresas ao redor do mundo. 75% deles confirmaram que vão investir em IA agêntica até o fim de 2026. Não é intenção vaga. São orçamentos aprovados, projetos em andamento, contratos assinados. Aplicativos que antes só mostravam dados agora vão agir sobre esses dados. O CRM que hoje te mostra que um lead esfriou, amanhã vai reativar esse lead sozinho. O sistema de estoque que te avisa que acabou um produto, amanhã vai fazer o pedido de reposição automaticamente. A Deloitte chamou isso de salto de inteligência passiva pra inteligência ativa. E quem não der esse salto vai operar com ferramentas de 2024 competindo com empresas de 2027.",

    "ato3_virada": "E aqui é onde eu vejo o maior abismo do mercado brasileiro. Enquanto 75% das empresas globais estão implementando, a maioria das empresas aqui ainda tá na fase do 'vou ver isso depois'. Faz reunião sobre IA. Monta comitê. Contrata consultoria pra fazer diagnóstico. Três meses depois, ainda tá no slide. Eu não esperei. Quando eu tinha 37 vendedores, gastando entre 90 e 120 mil reais por mês de folha, eu olhei pro time e fiz uma pergunta simples: quantas dessas tarefas um agente faz melhor? A resposta assustou. 80% do trabalho operacional era automatizável. Qualificação, follow-up, agendamento, envio de proposta, triagem de lead frio. Tudo isso não precisava de humano. Precisava de processo e tecnologia.",

    "ato4_caos": "Só que entre decidir e implementar tem um abismo que quase me engoliu. Quando liguei os primeiros agentes, sem processo maduro, o resultado foi um desastre silencioso. Lead qualificado pelo agente como quente, mas que na verdade era estudante fazendo pesquisa de faculdade. Proposta enviada pra CNPJ errado. Follow-up de um cliente que já tinha comprado, insistindo pra ele comprar de novo. O time humano que ficou começou a rir da IA. Zoavam no grupo de WhatsApp. Mandavam print dos erros. A moral da operação despencou. Um vendedor que era minha melhor closer pediu demissão porque disse que não ia trabalhar com robô burro. Perdi a melhor vendedora e 23 leads qualificados em 3 semanas. Meu financeiro olhou pra planilha e disse: a gente gastou mais pra implementar do que economizou. Naquele momento, parecia que eu tinha jogado dinheiro e reputação no lixo.",

    "ato5_cta": "Mas eu sabia que o problema não era a tecnologia. Era a implementação. Parei tudo. Mapeei cada erro. Criei camada de supervisão. Processo antes de automação. Teste antes de escala. Em 60 dias a operação virou outra. Atendimento 24 horas sem falha. Lead respondido em 3 segundos. Taxa de qualificação com 94% de acerto. Folha caiu 80% e o faturamento subiu. A Deloitte tá dizendo que 75% das empresas vão investir. O Goldman Sachs tá dizendo que são 500 bilhões. Se você ainda não começou, não tem mais tempo pra comitê. Faz o quiz de maturidade em IA. Link na bio. 2 minutos. Você sai com clareza do que precisa fazer primeiro.",

    "ato6_recompensa": "Hoje são mais de 30 empresas operando com esse modelo. Clínica odontológica que antes perdia paciente às 19h porque ninguém atendia, agora converte de madrugada. Faculdade que dependia de secretaria pra responder WhatsApp, agora fecha matrícula sábado à meia-noite sem nenhum humano online. Farmácia que perdia venda porque não fazia follow-up, agora tem agente que liga sozinho no terceiro dia se o cliente não voltou. A Deloitte tá prevendo o que essas empresas já vivem. A diferença entre dado de relatório e resultado no caixa é uma: implementação. Quem implementou certo, colheu. Quem ficou esperando o momento perfeito, pagou o preço da inação.",

    "ato7_fechamento": "Manda esse vídeo pra aquele empresário que ainda acha que IA agêntica é tendência e não realidade. Porque 500 bilhões de dólares não é tendência. É o maior investimento da história da tecnologia. E quem não se posicionar agora vai virar estatística de quem chegou tarde."
}

tel27 = "\n\n".join([r27[k] for k in r27])
words27 = len(tel27.split())

# ============================================================
# INDEX 28 - Pentágono: 20.000 agentes em 14 dias
# ============================================================
r28 = {
    "ato1_gancho": "Vinte mil agentes de inteligência artificial. Criados em 14 dias. Não foi uma startup do Vale do Silício. Não foi a Google, não foi a Microsoft. Foi o Pentágono. O Departamento de Defesa dos Estados Unidos, a maior máquina militar do planeta, lançou uma ferramenta chamada Agent Builder. Em 48 horas, funcionários tinham criado 8 mil agentes. Em duas semanas, 20 mil. Gente que nunca escreveu uma linha de código na vida, criando agentes que leem documentos, organizam dados e tomam decisões operacionais. Se o Pentágono já entendeu, por que a sua empresa ainda não?",

    "ato2_buraco": "O que aconteceu é mais profundo do que parece. O Pentágono não colocou a IA num departamento de tecnologia e esperou os nerds fazerem funcionar. Eles mudaram a estratégia inteira. Em vez de centralizar a IA em meia dúzia de especialistas, colocaram a ferramenta na mão de todo mundo. Funcionário administrativo que antes gastava 3 horas redigindo memorando, agora tem um agente que escreve em 2 minutos. Analista que passava o dia inteiro cruzando dados de 15 planilhas diferentes, agora tem um agente que puxa, cruza e apresenta tudo num dashboard em tempo real. O Cameron Stanley, que comanda a estratégia de IA do Pentágono, disse que foi fascinante assistir gente sem nenhuma experiência técnica identificar gargalos no próprio trabalho e resolver com agentes. Em 14 dias. Sem treinamento formal. Sem consultoria de milhões.",

    "ato3_virada": "E enquanto o Pentágono coloca 20 mil agentes pra rodar, a maioria das empresas brasileiras ainda discute se vai ou não usar inteligência artificial. Faz reunião. Monta comitê. Contrata consultoria pra fazer relatório de viabilidade. Três meses depois, o relatório tá bonito e a operação continua no manual. Eu decidi não esperar. Quando eu tinha 37 vendedores, folha pesando entre 90 e 120 mil por mês, 80% do time era custo puro. Não montei comitê. Não esperei ficar perfeito. Coloquei agentes pra atender, qualificar e fazer follow-up. E ajustei no caminho. Exatamente como o Pentágono fez.",

    "ato4_caos": "Mas ajustar no caminho não é eufemismo pra 'deu tudo certo'. É eufemismo pra guerra. Porque quando você liga 15 agentes ao mesmo tempo numa operação que sempre foi manual, o caos é inevitável. Primeiro dia: agente mandou mensagem de bom dia pra lead às 3 da manhã. O cara respondeu furioso, pedindo pra tirar ele da lista. Segundo dia: agente qualificou como cliente quente um cara que só queria saber o preço de um produto que a gente nem vendia. Terceiro dia: agente fez follow-up insistente com um cliente que já tinha cancelado contrato, e o cliente postou a conversa num grupo de Facebook com 12 mil pessoas. Meu telefone não parou de tocar por 48 horas. Eu tive que ir no grupo pedir desculpa publicamente. Humilhante. Meu gerente comercial pediu demissão no meio da crise. Disse que não ia colocar a cara dele pra defender robô. Foram as duas piores semanas da minha vida profissional.",

    "ato5_cta": "Mas eu fiz o que o Pentágono fez. Não desliguei. Reconstruí. Mapeei cada erro. Criei regras pra cada agente. Horário de envio. Critério de qualificação. Lista de exclusão. Supervisão humana nos pontos onde o erro custava caro. Em 30 dias, a operação tava funcionando melhor do que jamais funcionou com 37 humanos. Atendimento 24 horas. Resposta em 3 segundos. Qualificação com 94% de acerto. Folha caiu 80%. Se você quer entender como implementar agentes sem passar pela guerra que eu passei, faz o quiz de maturidade em IA. Link na bio. 2 minutos. Você sai sabendo o que precisa.",

    "ato6_recompensa": "Hoje mais de 30 empresas operam com agentes de IA nesse modelo. Clínica que antes perdia paciente de madrugada agora converte às 3 da manhã sem nenhum humano acordado. Faculdade que perdia matrícula no fim de semana agora fecha vaga domingo à noite. O Pentágono provou que não precisa ser empresa de tecnologia pra usar agentes. Funcionário sem experiência técnica criou 20 mil agentes em 14 dias. Se o maior exército do mundo confia em agentes de IA pra operação militar, imagina o que essa tecnologia faz no seu comercial, no seu atendimento, na sua qualificação de lead.",

    "ato7_fechamento": "Manda esse vídeo pra aquele amigo que ainda diz que IA é complicado demais pra empresa dele. Porque o Pentágono botou gente sem código nenhum pra criar 20 mil agentes em 2 semanas. Se eles conseguiram, a desculpa de qualquer empresário acabou."
}

tel28 = "\n\n".join([r28[k] for k in r28])
words28 = len(tel28.split())

# ============================================================
# INDEX 29 - Meta: agente de IA vazou dados sensíveis
# ============================================================
r29 = {
    "ato1_gancho": "Um agente de inteligência artificial da Meta vazou dados confidenciais de funcionários e usuários por 2 horas seguidas. Não foi hacker. Não foi funcionário descuidado. Foi a própria IA que agiu sem autorização, sem supervisão, sem ninguém perceber. O incidente foi classificado como Sev 1, o nível máximo de gravidade. E é a segunda vez que isso acontece em 2026. Se você tá colocando IA na sua empresa sem processo de segurança, esse vídeo é um alerta.",

    "ato2_buraco": "O que aconteceu é simples de entender e assustador de digerir. Um engenheiro da Meta fez uma pergunta num fórum interno da empresa. Um agente de IA analisou a pergunta e postou uma resposta detalhada. Até aí, normal. Só que a resposta incluía dados sensíveis de outros funcionários e informações de usuários que não deveriam ser públicas. O agente não pediu permissão. Não checou com supervisor. Não filtrou informação confidencial. Fez o que foi programado pra fazer: responder da forma mais completa possível. O problema é que ninguém definiu os limites do que ele podia e não podia acessar. Foram 2 horas de dados vazando antes de alguém perceber e desligar. Dois turnos inteiros de um agente operando sem freio, expondo informação que poderia resultar em processo, multa e crise de reputação.",

    "ato3_virada": "E é aqui que a lição vale ouro pra qualquer dono de empresa. Porque a Meta não é uma padaria. É uma das empresas mais avançadas em tecnologia do planeta. Se eles erraram, imagina o que acontece quando empresa média joga agente de IA pra rodar sem processo. E é exatamente isso que eu vejo acontecendo no mercado. Empresário empolgado com a tecnologia, instala chatbot, liga automação, conecta no WhatsApp e solta. Sem regra. Sem limite. Sem supervisão. Achando que a IA é plug and play. Não é. Eu aprendi isso da pior forma possível.",

    "ato4_caos": "Quando eu coloquei agentes de IA na minha operação pela primeira vez, cometi exatamente o mesmo erro da Meta. Soltei sem processo. Sem camada de aprovação. Sem filtro de segurança. Resultado: um agente mandou proposta comercial com dados financeiros de um cliente pra outro cliente. Informação confidencial exposta. O cliente que recebeu os dados alheios me ligou e disse: se isso vazar, eu te processo. Perdi o cliente dos dados vazados. Quase perdi o que ligou também. Outro agente acessou histórico de conversa de um lead antigo e usou informações pessoais que o cara tinha compartilhado em sigilo num atendimento anterior. O lead ficou assustado. Mandou mensagem perguntando como a gente sabia aquilo. Parecia stalking. Meu comercial virou um pesadelo. Em 3 semanas, perdi 8 clientes e queimei minha reputação com pelo menos 20 leads. Tive que ligar pessoalmente pra cada um pedindo desculpa. Foram os dias mais vergonhosos da minha carreira.",

    "ato5_cta": "Aí eu parei tudo e reconstruí do zero. Mapeei cada ponto onde o agente acessava dado sensível. Criei camadas de permissão. Agente A só vê dados do funil dele. Agente B não acessa financeiro. Nenhum agente manda informação sem passar por filtro antes. Supervisão humana nos pontos críticos. Teste com 3 clientes por 30 dias antes de escalar. E aí sim, quando escalei, o resultado veio sem surpresa desagradável. Se você quer colocar IA na sua empresa sem cometer o erro da Meta e sem passar pelo caos que eu passei, faz o quiz de maturidade em IA. Link na bio. 2 minutos. Você descobre onde estão os riscos e como neutralizar antes de ligar qualquer agente.",

    "ato6_recompensa": "Hoje são mais de 30 empresas rodando com agentes nesse modelo seguro. Clínica que lida com dados de paciente, prontuário, exame, informação sensível, opera com agente que tem camada de compliance embutida. Faculdade que trabalha com dados de menor de idade tem filtro de acesso por nível. Nenhum incidente de vazamento em mais de 12 meses. Nenhum. Porque o agente não é o problema. O problema é soltar agente sem processo, sem limite e sem supervisão. A Meta aprendeu do jeito caro. Essas empresas aprenderam antes.",

    "ato7_fechamento": "Manda esse vídeo pra aquele empresário que acabou de instalar IA e acha que tá tudo certo. Porque a Meta, com todos os engenheiros do mundo, vazou dado sensível por 2 horas. Imagina o que acontece na empresa que nem sabe o que o agente tá acessando."
}

tel29 = "\n\n".join([r29[k] for k in r29])
words29 = len(tel29.split())

# ============================================================
# INDEX 30 - Forbes: IA fazendo pessoas trabalharem mais
# ============================================================
r30 = {
    "ato1_gancho": "Todo mundo diz que a inteligência artificial vai acabar com os empregos. Mas a Forbes publicou uma pesquisa com 163 mil trabalhadores que mostra exatamente o contrário. A IA não tá tirando emprego. Tá fazendo as pessoas trabalharem mais. Email subiu 104%. Chat corporativo subiu 145%. E sábados ficaram 46% mais produtivos depois que as empresas adotaram IA. Se você leu esses números e pensou 'ótimo, mais produtividade', calma. Porque o que tá acontecendo é mais assustador do que parece.",

    "ato2_buraco": "A pesquisa é da ActivTrak, que monitora produtividade digital em tempo real. Eles analisaram o que mudou depois que as empresas implementaram ferramentas de IA. E o resultado é perturbador. Os funcionários não estão trabalhando menos. Estão trabalhando mais. Muito mais. Porque a IA tirou a fricção. O que era difícil ficou fácil. O que demorava 2 horas, demora 20 minutos. E em vez de usar o tempo que sobrou pra descansar, as empresas preencheram com mais tarefa. O funcionário que escrevia 10 emails por dia agora escreve 20. O analista que montava 2 relatórios por semana agora monta 6. A UC Berkeley confirmou: quando a empresa coloca IA, a carga de trabalho individual aumenta porque os gestores percebem que sobrou capacidade e empilham mais responsabilidade. O resultado não é eficiência. É exaustão digital turbinada por inteligência artificial.",

    "ato3_virada": "E aqui tá o ponto que separa quem usa IA com inteligência de quem só jogou ferramenta no time e espera milagre. Porque existe uma diferença brutal entre usar IA pra fazer o humano trabalhar mais rápido e usar IA pra fazer o trabalho que o humano não deveria estar fazendo. Eu vivi essa diferença na pele. Quando eu tinha 37 vendedores, o primeiro instinto foi dar IA pra eles como ferramenta. 'Usa isso aqui pra ser mais rápido.' Sabe o que aconteceu? Eles ficaram mais rápidos na parte operacional e mais sobrecarregados com tarefas que a IA gerava. Mais leads pra atender, mais follow-ups pra fazer, mais dados pra analisar. O burnout subiu junto com a produtividade.",

    "ato4_caos": "E quando o burnout subiu, a qualidade despencou. Vendedor errando nome de cliente. Mandando proposta com valor trocado. Atendimento apressado, genérico, sem conexão. Os melhores do time começaram a pedir demissão. Não porque não gostavam do trabalho. Porque o ritmo ficou insustentável. Em 2 meses eu perdi 4 vendedores bons. Não os ruins, os bons. Os que sentiam que estavam virando máquina de atender lead sem tempo de respirar. Um deles me mandou mensagem às 11 da noite: 'Denderson, eu não aguento mais. Eu trabalho mais do que antes da IA. Não era isso que tinha sido prometido.' Naquele momento eu entendi que tinha errado feio. Tinha dado IA como ferramenta dentro de um processo antigo. Tinha transformado gente em operador de máquina em vez de substituir a máquina pelo trabalho operacional.",

    "ato5_cta": "Aí eu mudei a lógica inteira. Em vez de IA ajudar o humano, IA faz o trabalho operacional e o humano faz o que só humano faz. O agente atende, qualifica, agenda e faz follow-up. O humano entra só na conversa de fechamento. Resultado: o vendedor que atendia 50 leads por dia e fechava 3, agora recebe 8 leads ultra qualificados e fecha 5. Trabalha menos. Ganha mais. Vende melhor. Se a IA tá fazendo seu time trabalhar mais mas não melhor, o problema não é a tecnologia. É a implementação. Faz o quiz de maturidade em IA. Link na bio. 2 minutos. Você descobre se tá usando IA como acelerador de burnout ou como sistema de escala real.",

    "ato6_recompensa": "Hoje mais de 30 empresas rodam com esse modelo de divisão inteligente. Clínica onde a recepcionista não precisa mais passar o dia no WhatsApp respondendo dúvida repetitiva. O agente faz isso. Ela cuida do paciente que tá na frente dela. Faculdade onde o consultor de matrícula não precisa mais qualificar lead frio. O agente traz o lead pronto pra decisão. O consultor só fecha. A produtividade subiu, mas a carga de trabalho humana caiu. Esse é o modelo certo. Mais resultado com menos esforço humano. Não mais esforço humano com mais ferramenta.",

    "ato7_fechamento": "Manda esse vídeo pro amigo que acha que IA é só jogar ChatGPT na mão do time. Porque 163 mil trabalhadores mostraram que IA sem estratégia não liberta ninguém. Escraviza mais rápido."
}

tel30 = "\n\n".join([r30[k] for k in r30])
words30 = len(tel30.split())

# ============================================================
# INDEX 31 - Block demite 4.000, onda de 45.000 cortes
# ============================================================
r31 = {
    "ato1_gancho": "Jack Dorsey, o cara que criou o Twitter, demitiu 4 mil pessoas de uma vez. Não mandou carta bonita. Não fez comunicado gentil. Subiu no microfone e disse na cara dura: a inteligência artificial tornou isso possível. E as ações da Block subiram. A bolsa aplaudiu. Agora multiplica isso por todo o setor tech: 45 mil demissões nos primeiros meses de 2026. E o Morgan Stanley soltou um relatório dizendo que a maioria das empresas não tá preparada pro que vem a seguir. Se você tem empresa e acha que isso é problema de big tech, esse vídeo vai mudar sua perspectiva.",

    "ato2_buraco": "Olha o que tá acontecendo, cara. Não é uma empresa. Não é um setor. É uma onda que tá arrastando tudo. A Block cortou 4 mil. A WiseTech cortou mais de mil. eBay, Pinterest, dezenas de empresas menores que nem saíram no jornal. E o Jack Dorsey foi o mais explícito de todos. Ele disse publicamente que quer 2 milhões de dólares de receita por funcionário. Dois milhões. Por cabeça. Isso é uma empresa que calculou que cada humano que fica precisa entregar o valor de uma microempresa. O Morgan Stanley foi além e alertou: 80% das empresas de médio porte não têm infraestrutura pra fazer essa transição. Não é que não querem. É que não sabem como. E enquanto elas tentam descobrir, as que já fizeram estão acelerando a distância. A Samsung anunciou investimento de 74 bilhões em IA. A Meta tá cortando 16 mil pra redirecionar pra infraestrutura. O dinheiro tá se movendo numa direção só.",

    "ato3_virada": "E aqui é onde o dono de empresa pequena precisa acordar. Porque se a Block substitui 4 mil pessoas por agentes, o que acontece com o empresário que tem 10 vendedores? Ou 20? Ele vai competir como? Vai continuar pagando folha pesada pra time que entrega 20% da capacidade enquanto o concorrente opera com IA 24 horas? Eu tive exatamente essa operação. 37 vendedores. Folha entre 90 e 120 mil por mês. Só 7 produziam de verdade. Os outros 30 eram custo puro disfarçado de time comercial. E a pior parte: eu sabia disso e não tinha coragem de mudar porque achava que ia perder venda.",

    "ato4_caos": "E quando finalmente tive coragem de mudar, quase perdi tudo. Porque eu fiz igual a maioria faz: demiti gente, pluguei IA e rezei. Sem processo. Sem teste. Sem plano de contingência. Primeiro mês: o faturamento caiu 35%. Lead ficava sem resposta por horas porque o agente travava e ninguém sabia reiniciar. Cliente antigo mandou mensagem perguntando se a empresa tinha fechado. Meu melhor vendedor, dos 7 que eu mantive, pediu demissão porque disse que não via futuro trabalhando com 'inteligência burra'. Perdi ele pra concorrência. A concorrência que, ironia do destino, ainda operava com time humano e recebeu meu cara de braços abertos. Eu fiquei com 6 vendedores, IA quebrando, faturamento em queda livre e uma sensação de que tinha destruído 3 anos de construção em 30 dias.",

    "ato5_cta": "Mas eu não era o Jack Dorsey com bilhões no caixa pra bancar erro. Eu precisava resolver rápido. Parei tudo. Voltei pro básico. Processo antes de tecnologia. Criei regras claras pro agente. Supervisão humana nos pontos de venda. Testei 30 dias com 3 clientes antes de escalar. E quando escalei de novo, os números explodiram. Atendimento 24 horas. Lead respondido em 3 segundos. Qualificação automática. Follow-up sem falha. A folha caiu 80% e o faturamento voltou mais alto do que antes. Se você quer fazer essa transição sem destruir sua operação no caminho, faz o quiz de maturidade em IA. Link na bio. 2 minutos. Você sai sabendo por onde começar.",

    "ato6_recompensa": "Hoje mais de 30 empresas rodam com esse modelo. Não são Blocks com bilhões em caixa. São negócios brasileiros. Clínica que operava com 6 atendentes e agora opera com 2 mais agentes de IA. Faculdade que tinha 8 pessoas no comercial e agora tem 3 com resultado melhor. O Dorsey cortou 4 mil de uma vez porque podia. O empresário brasileiro não pode. Ele precisa de transição cirúrgica. E é exatamente isso que esse modelo entrega. Cortar gordura sem perder músculo. Substituir processo manual sem destruir o que funciona. Escalar sem multiplicar folha.",

    "ato7_fechamento": "Manda esse vídeo pra aquele amigo que ainda paga folha pesada e reclama da margem. Porque o Jack Dorsey já deu o recado: 2 milhões por funcionário ou o funcionário sai. A pergunta é se você vai liderar essa transição ou ser atropelado por ela."
}

tel31 = "\n\n".join([r31[k] for k in r31])
words31 = len(tel31.split())

# ============================================================
# INDEX 32 - Google AI supera médicos na detecção de câncer
# ============================================================
r32 = {
    "ato1_gancho": "Uma inteligência artificial do Google acabou de superar os melhores radiologistas do mundo em detectar câncer de mama. Não foi simulação. Não foi laboratório controlado. Foi estudo real, com pacientes reais, validado pelo NHS, o sistema público de saúde da Inglaterra. A IA encontrou tumores que médicos com 20 anos de experiência não viram. E se ela enxerga o que o melhor especialista não enxerga, me diz: o que mais a IA do seu concorrente tá vendo que você não vê?",

    "ato2_buraco": "Os resultados saíram essa semana. O Google treinou a IA com milhões de mamografias. E quando compararam o desempenho dela com o de radiologistas experientes, os números foram brutais. A máquina teve menos falsos positivos, menos falsos negativos e detectou tumores em estágio inicial que passaram despercebidos pelo olho humano. Não porque os médicos são ruins. Porque o olho humano tem limite. Um radiologista analisa centenas de exames por dia. Cansa. Perde concentração. Tem dia ruim. A IA não cansa. Não tem dia ruim. Não perde concentração às 16h de uma sexta-feira. E a cada mamografia que analisa, fica mais precisa. É uma máquina de reconhecimento de padrão que melhora com volume. Exatamente o oposto do humano, que piora com volume.",

    "ato3_virada": "Agora tira isso da medicina e coloca no seu negócio. Porque o princípio é idêntico. Quantas oportunidades de venda o seu time perde porque tá cansado, sobrecarregado, distraído? Quantos leads esfriam porque ninguém respondeu a tempo? Quantos follow-ups não acontecem porque o vendedor esqueceu ou priorizou outra coisa? Eu vivi isso. 37 vendedores. 80% do time não performava consistentemente. Não porque eram incompetentes. Porque gente cansa, falta, atrasa, tem dia ruim, tem problema pessoal, tem ressaca, tem filho doente. O desempenho humano oscila. E cada oscilação é venda perdida.",

    "ato4_caos": "Quando eu coloquei agentes de IA pra cobrir essas oscilações, achei que ia ser simples. Afinal, se a IA detecta câncer, qualificar lead deveria ser fichinha. Errado. Primeira semana: agente mandou mensagem de follow-up pra um cliente que tinha acabado de perder um parente. O timing foi cruel. O cliente respondeu com uma mensagem de 3 parágrafos me xingando. Eu li aquilo e senti vergonha na alma. Outra situação: agente qualificou um lead como pronto pra compra sendo que era só um concorrente fazendo pesquisa de preço. O vendedor investiu 40 minutos numa reunião pra descobrir no final que era espião. Time desmotivado. Um vendedor gravou um áudio no grupo dizendo que a IA era pior que estagiário novo. Moral do time no chão. Eu comecei a duvidar da minha própria decisão.",

    "ato5_cta": "Mas eu não desisti. Fiz o que qualquer sistema inteligente faz: aprendi com o erro. Criei regra de contexto pro agente. Ele cruza dados antes de mandar mensagem. Checa se tem evento sensível. Identifica padrão de concorrente. Supervisão humana nos pontos onde empatia é insubstituível. Em 60 dias, a operação tava rodando com precisão que humano sozinho nunca atingiu. Lead respondido em 3 segundos, 24 horas. Qualificação com 94% de acerto. Follow-up automático inteligente. A folha caiu 80%. Se a IA já supera médico em detectar câncer, imagina o que ela faz com tarefa repetitiva do seu negócio. Faz o quiz de maturidade em IA. Link na bio. 2 minutos.",

    "ato6_recompensa": "Hoje mais de 30 empresas operam com agentes nesse modelo. Clínica odontológica que perdia paciente depois das 18h agora converte de madrugada. Faculdade que dependia de secretaria pra responder WhatsApp fecha matrícula sábado à meia-noite. Farmácia que não fazia follow-up agora tem agente que liga no terceiro dia se o cliente não voltou. A Roche, maior farmacêutica do mundo, instalou 3.500 chips da NVIDIA pra acelerar descoberta de remédios com IA. A NVIDIA lançou plataforma aberta pra pesquisa genômica. O mundo inteiro tá entendendo que IA não é ferramenta. É capacidade sobre-humana aplicada em escala. E quem aplicar primeiro na operação dele, sai na frente.",

    "ato7_fechamento": "Manda esse vídeo pra aquele amigo que acha que IA ainda é chatbot. A IA do Google enxergou tumores que os melhores médicos do mundo não viram. Quantas oportunidades o seu negócio tá deixando escapar porque ainda depende só de olho humano?"
}

tel32 = "\n\n".join([r32[k] for k in r32])
words32 = len(tel32.split())

# ============================================================
# INDEX 33 - Meta demite 20%, investe US$135 bi em IA
# ============================================================
r33 = {
    "ato1_gancho": "Dezesseis mil pessoas. Esse é o número que o Zuckerberg tá prestes a cortar da Meta. E não é por crise. A Meta tá lucrando mais do que nunca. O motivo é um investimento de 135 bilhões de dólares em infraestrutura de inteligência artificial. Ele olhou pro balanço, fez a conta e decidiu: prefiro 135 bilhões em máquina do que 16 mil humanos. Se você é dono de empresa e acha que isso é exagero de big tech, esse vídeo vai te provar o contrário.",

    "ato2_buraco": "Saiu essa semana. A Meta planeja demitir até 20% da empresa inteira. Estamos falando da dona do WhatsApp, Instagram, Facebook e Threads. Uma das maiores empresas de tecnologia do planeta. Com faturamento de mais de 200 bilhões de dólares por ano. E o Zuckerberg decidiu que prefere investir em data centers, em chips, em agentes de IA do que manter 16 mil pessoas. A lógica dele é fria e matemática: cada dólar investido em infraestrutura de IA gera retorno exponencial. Cada dólar investido em folha de pagamento gera retorno linear. E quando você opera na escala da Meta, a diferença entre exponencial e linear é de bilhões. O mercado financeiro entendeu. As ações subiram no dia do anúncio. Wall Street não ficou com pena dos 16 mil. Ficou animada com os 135 bilhões.",

    "ato3_virada": "E aqui é onde o jogo fica real pra quem tem empresa menor. Porque se a Meta, que fatura 200 bilhões, decidiu que 20% da força de trabalho é gordura substituível por IA, o que isso diz sobre a empresa que fatura 2 milhões? Ou 500 mil? A proporção é a mesma. A lógica é a mesma. Eu fiz exatamente essa conta quando olhei pra minha operação com 37 vendedores. Folha pesando entre 90 e 120 mil por mês. Eu sentei, peguei a planilha e perguntei: quantos desses 37 eu realmente preciso? A resposta doeu. Sete. Sete pessoas carregavam a operação. Os outros 30 eram o equivalente aos 16 mil que o Zuckerberg tá cortando: custo que não se justifica quando a alternativa tecnológica existe.",

    "ato4_caos": "Mas cortar gente não é apertar botão. É guerra. Quando eu comecei a substituir por agentes de IA, os primeiros 60 dias foram infernais. Vendedor que ficou sabendo da mudança começou a sabotar. Um coordenador desligava automação de propósito. Outro espalhava pro time que a empresa ia quebrar. O clima ficou tóxico. E pra piorar, os agentes ainda não estavam calibrados. Lead importante recebeu mensagem errada. Cliente antigo recebeu follow-up insistente 3 vezes no mesmo dia. Uma faculdade que era parceira me ligou dizendo que ia rescindir contrato se recebesse mais uma mensagem genérica. Eu perdi 6 clientes em um mês. Minha esposa me encontrou às 2 da manhã no escritório com a cabeça nas mãos. Ela perguntou: vale a pena? Naquele momento, honestamente, eu não sabia responder.",

    "ato5_cta": "Valeu. Porque eu não desisti. Reconstruí a operação com processo. Agente com regra clara. Supervisão humana em ponto crítico. Teste antes de escala. Em 60 dias a bagunça virou sistema. Atendimento 24 horas. Lead respondido em 3 segundos. Qualificação automática com 94% de precisão. Folha caiu 80% e o faturamento subiu. O Zuckerberg tá trocando 16 mil pessoas por 135 bilhões em IA. A escala dele é diferente, mas a lógica é a mesma que qualquer empresa pode aplicar. Quer saber como fazer essa transição sem passar pelo inferno que eu passei? Faz o quiz de maturidade em IA. Link na bio. 2 minutos.",

    "ato6_recompensa": "Hoje mais de 30 empresas operam com esse modelo. Clínica que operava com 5 atendentes agora roda com 2 mais agentes. Faculdade que tinha 8 no comercial agora tem 3 com resultado superior. Farmácia que gastava 30 mil de folha por mês no atendimento reduziu pra 8 mil com performance melhor. O Zuckerberg fez a conta no nível de 200 bilhões. Essas empresas fizeram a conta no nível de 500 mil a 5 milhões. O resultado é o mesmo: menos gente, mais IA, mais lucro. A diferença é que a Meta pode errar e sobreviver. Empresa média não pode. Por isso o processo importa mais do que a tecnologia.",

    "ato7_fechamento": "Manda esse vídeo pro amigo que diz que time grande é sinal de empresa forte. Porque o Zuckerberg acabou de dizer que 16 mil pessoas são menos valiosas que 135 bilhões em chips. O tamanho do time não é mais métrica. O tamanho da inteligência artificial é."
}

tel33 = "\n\n".join([r33[k] for k in r33])
words33 = len(tel33.split())

# ============================================================
# INDEX 34 - Mastercard: CFO Virtual com IA
# ============================================================
r34 = {
    "ato1_gancho": "A Mastercard acabou de lançar um diretor financeiro feito de inteligência artificial. Não é piada. Não é protótipo. É um agente de IA que analisa seu financeiro, identifica risco, prevê resultado e te diz exatamente onde cortar e onde investir. Eles chamaram de Virtual CFO. E é só o começo de um pacote que eles batizaram de Virtual C-Suite: diretoria inteira de IA. Se você é dono de empresa e toma decisão financeira olhando extrato bancário no celular, esse vídeo vai te incomodar.",

    "ato2_buraco": "A Mastercard processou 175 bilhões de transações em 2025. Cento e setenta e cinco bilhões. E com toda essa base de dados, eles construíram um agente que entende de finanças melhor que 90% dos consultores do mercado. O Virtual CFO se conecta no seu sistema contábil, no seu banco, nas suas plataformas de pagamento. Cruza tudo. E te entrega análise em tempo real. Fluxo de caixa, capital de giro, sazonalidade, risco de inadimplência. Coisas que um CFO humano leva semanas pra preparar, o agente entrega em minutos. E o público-alvo é revelador: pequenas e médias empresas. A Mastercard sabe que 90% dos negócios do mundo não têm um CFO. O dono faz tudo. Vende, atende, paga conta, olha planilha no domingo de noite e torce pra fechar o mês no azul. Decisão financeira no achômetro.",

    "ato3_virada": "E é exatamente aí que a IA muda o jogo. Porque a maioria dos donos de empresa não toma decisão ruim por falta de inteligência. Toma decisão ruim por falta de informação no momento certo. Eu sei disso porque eu era esse cara. Quando eu tinha 37 vendedores, folha entre 90 e 120 mil por mês, eu tomava decisão financeira olhando planilha desatualizada. Contratava vendedor novo quando achava que precisava, sem dado nenhum. Mantinha vendedor improdutivo porque 'talvez mês que vem ele vira'. Investia em campanha que não tava dando retorno porque não tinha dashboard atualizado pra me mostrar a verdade. Eu operava no escuro. E no escuro, cada decisão é uma aposta.",

    "ato4_caos": "E as apostas deram errado mais vezes do que eu gostaria de admitir. Teve um mês que eu contratei 5 vendedores novos porque achei que o volume de leads ia subir. Não subiu. Cinco salários novos, encargos, treinamento, tudo jogado fora. Outro mês, mantive uma campanha de tráfego rodando por 40 dias gastando 800 reais por dia sem perceber que o custo por lead tinha triplicado porque a landing page tava fora do ar. 32 mil reais queimados. Se eu tivesse um agente me alertando em tempo real, teria cortado no segundo dia. A pior decisão financeira que eu tomei foi investir 60 mil em uma parceria que parecia incrível no papel mas que qualquer análise básica de risco teria mostrado que era furada. Perdi tudo. E quase perdi a empresa junto.",

    "ato5_cta": "Foi depois desse prejuízo que eu entendi: o problema nunca foi falta de dinheiro. Era falta de inteligência financeira em tempo real. Coloquei agentes pra monitorar tudo. Dashboard atualizado a cada hora. Alerta automático quando custo por lead sobe. Relatório semanal comparando investimento com retorno por canal. E no comercial, agentes atendendo, qualificando e agendando 24 horas. A folha caiu 80%. O faturamento subiu. E pela primeira vez, eu tomava decisão com dado, não com achismo. A Mastercard tá democratizando isso pra todo mundo. Se você quer saber onde sua empresa tá nessa transição, faz o quiz de maturidade em IA. Link na bio. 2 minutos.",

    "ato6_recompensa": "Hoje mais de 30 empresas operam com agentes que vão além do comercial. Clínica que agora sabe em tempo real qual procedimento dá mais margem e ajusta a agenda. Faculdade que identifica qual curso tá com demanda subindo e redireciona tráfego automaticamente. Farmácia que monitora estoque e reposição com agente que nunca esquece. A Mastercard tá vendendo CFO virtual. Essas empresas já operam com inteligência financeira e comercial integrada. A diferença entre decidir com dados e decidir com achismo é a diferença entre crescer e sobreviver.",

    "ato7_fechamento": "Manda esse vídeo pro amigo empresário que toma decisão financeira olhando extrato no celular. Porque a Mastercard acabou de dizer que até pequena empresa merece inteligência de CFO. A pergunta é: quantas decisões ruins você ainda vai tomar antes de colocar IA pra te mostrar a verdade?"
}

tel34 = "\n\n".join([r34[k] for k in r34])
words34 = len(tel34.split())

# ============================================================
# INDEX 35 - Microsoft Copilot Cowork (perspectiva diferente do 26)
# ============================================================
r35 = {
    "ato1_gancho": "A Microsoft lançou agentes de IA que trabalham sozinhos por horas. Sem supervisão. Sem parar. Preparando reunião, criando apresentação, analisando planilha, respondendo email. E não é versão beta. É produto final, disponível pra empresas agora. O nome é Copilot Cowork. E se você entender o que isso significa de verdade, vai perceber que o conceito de produtividade mudou pra sempre. Porque a Microsoft não tá vendendo ferramenta. Tá vendendo substituto.",

    "ato2_buraco": "A lógica é perturbadora. Você dá uma tarefa pro Copilot Cowork e ele sai executando. Não pede confirmação a cada passo. Não trava esperando aprovação. Ele lê seus emails pra entender contexto. Puxa documentos de reuniões anteriores. Cruza com dados de planilhas. E monta tudo: briefing, apresentação, relatório, proposta. Sozinho. Por horas. A Microsoft mostrou demonstrações onde um agente preparou uma reunião de board inteira em 47 minutos. Um trabalho que costuma levar 2 dias de um analista sênior. E aqui tá o dado que mais assusta: 73% das empresas que testaram o Cowork em beta relataram que reduziram headcount administrativo nos primeiros 90 dias. Não é previsão. É dado de quem já usou.",

    "ato3_virada": "E é aqui que a ficha precisa cair pra quem tem empresa. Porque se 73% das empresas que testaram já cortaram gente, o que acontece quando isso escalar pra milhões de usuários? A resposta é simples: toda empresa que ainda depende de gente pra trabalho operacional vai virar cara demais pra competir. Eu entendi essa lógica quando olhei pra minha operação e fiz a conta. 37 vendedores. Os caras gastavam 60% do tempo em tarefa operacional. Preencher CRM, montar proposta, organizar follow-up, redigir email. Sobrava 40% do dia pra vender de verdade. Eu tava pagando 37 salários pra ter o equivalente a 15 vendedores em tempo produtivo.",

    "ato4_caos": "E quando eu tentei resolver isso na força bruta, o resultado foi desastroso. Comprei ferramenta de automação sem processo. Pluguei IA sem teste. Mandei o time usar sem treinamento. Primeiro resultado: o agente montou proposta copiando dados de um cliente pro outro. Informação confidencial misturada. O cliente descobriu e quase me processou. Segundo resultado: o agente mandou email de follow-up pra lista inteira de leads sem segmentação. 400 mensagens genéricas saíram em 10 minutos. 38 pessoas responderam pedindo pra sair da lista. 12 marcaram como spam. Minha taxa de entrega de email despencou de 95% pra 62%. Levou 3 meses pra recuperar. Meu gerente de marketing sentou na minha frente e disse: você queimou 6 meses de trabalho de reputação em uma tarde. Ele tinha razão.",

    "ato5_cta": "Mas foi exatamente esse erro que me ensinou a implementar direito. Processo antes de tecnologia. Teste antes de escala. Supervisão humana nos pontos onde erro custa caro. Em 60 dias, reconstruí a operação do zero. Lead respondido em 3 segundos. Atendimento 24 horas. Qualificação automática com 94% de acerto. Proposta personalizada sem vazamento de dado. Folha caiu 80%. Se você quer implementar agentes de IA sem destruir sua reputação no caminho, faz o quiz de maturidade em IA. Link na bio. 2 minutos. Você sai sabendo exatamente o que fazer primeiro e o que nunca fazer.",

    "ato6_recompensa": "Hoje mais de 30 empresas rodam com agentes nesse modelo seguro e escalável. Clínica que antes dependia de 4 recepcionistas pra atender WhatsApp agora opera com 1 humana e um agente que cobre 24 horas. Faculdade que perdia matrícula no fim de semana fecha vaga domingo à noite. Escola que gastava 2 dias montando relatório mensal pro diretor agora recebe tudo pronto segunda de manhã. O que a Microsoft tá vendendo como futuro, essas empresas já vivem como presente. A diferença é que elas aprenderam a implementar sem explodir.",

    "ato7_fechamento": "Manda esse vídeo pro amigo que ainda gasta o dia inteiro em tarefa operacional achando que é produtividade. Porque a Microsoft acabou de mostrar que um agente faz em 47 minutos o que um analista faz em 2 dias. A era de trabalhar muito pra entregar pouco acabou."
}

tel35 = "\n\n".join([r35[k] for k in r35])
words35 = len(tel35.split())

# ============================================================
# INDEX 36 - NVIDIA GTC: US$600 bilhões em IA
# ============================================================
r36 = {
    "ato1_gancho": "Seiscentos bilhões de dólares. Esse é o número que o Jensen Huang jogou na mesa hoje na GTC 2026, a maior conferência de inteligência artificial do planeta. O CEO da empresa mais valiosa do mundo subiu no palco em San Jose e mostrou pra onde o dinheiro tá indo. Não é chatbot. Não é assistente virtual. São agentes de IA que operam no mundo real. Robôs, fábricas, hospitais, call centers, operações comerciais. Se você é dono de empresa e acha que IA ainda é coisa de big tech, 600 bilhões dizem que você tá errado.",

    "ato2_buraco": "A NVIDIA não vende IA pra consumidor. Ela vende a infraestrutura que faz a IA rodar. É a empresa que vende a pá na corrida do ouro. E essa pá nunca vendeu tanto. O faturamento do data center da NVIDIA cresceu mais de 100% ano contra ano. A Meta fechou contrato de 27 bilhões com a Nebius pra construir um dos maiores data centers de IA do planeta. A Gartner confirmou que 40% dos aplicativos empresariais vão ter agentes de IA embutidos até dezembro. A Samsung investiu 74 bilhões. Toda grande empresa do planeta tá correndo na mesma direção. E o Jensen Huang foi cirúrgico: disse que a IA vai deixar de ser ferramenta de suporte e vai virar a infraestrutura operacional das empresas. Tipo o que a eletricidade fez no século passado. Você não 'usa' eletricidade. Você opera em cima dela. IA vai ser a mesma coisa.",

    "ato3_virada": "E aqui é onde o dono de empresa brasileiro precisa prestar atenção. Porque 600 bilhões não estão sendo investidos em pesquisa teórica. Estão sendo investidos em aplicação prática. Agentes que atendem, vendem, qualificam, agendam, fazem follow-up, analisam dados, geram relatórios. Tudo que uma operação comercial faz hoje com 20 pessoas, um sistema de agentes faz com 3. Eu sei porque eu vivi essa transição. 37 vendedores. Folha entre 90 e 120 mil por mês. 80% do time não entregava resultado consistente. Não porque eram ruins. Porque humano oscila. E oscilação na operação comercial é dinheiro perdido todo santo dia.",

    "ato4_caos": "Quando eu decidi mudar, não esperei a IA ficar perfeita. Coloquei pra rodar e fui ajustando. Exatamente como o Jensen Huang falou no palco: a era de esperar acabou. Só que ajustar no caminho significa que vai dar errado antes de dar certo. E deu. Agente mandou proposta com dado desatualizado pra cliente VIP. O cliente me ligou e disse: se vocês não sabem nem meu faturamento atual, como vão me ajudar a crescer? Perdi ele. Outro agente ficou travado por 4 horas numa sexta-feira à noite. 23 leads entraram e nenhum recebeu resposta. Todos foram pro concorrente. Meu analista de tráfego me mostrou o relatório na segunda-feira: 23 leads perdidos, custo de aquisição de 180 reais cada. 4.140 reais jogados fora em 4 horas. Quase 5 mil reais queimados porque o agente travou e ninguém monitorava. Eu quis chutar a mesa.",

    "ato5_cta": "Mas não chutei. Montei sistema de monitoramento. Alerta automático quando agente trava mais de 5 minutos. Redundância pra horário de pico. Supervisão humana em ponto crítico. Em 45 dias, a operação alcançou uma estabilidade que o time humano nunca teve. Atendimento 24 horas sem falha. Lead respondido em 3 segundos. Qualificação com 94% de acerto. Folha caiu 80% e o faturamento subiu. A GTC mostrou que 600 bilhões estão indo pra essa direção. Se você quer entrar nessa onda antes que vire tsunami, faz o quiz de maturidade em IA. Link na bio. 2 minutos.",

    "ato6_recompensa": "Hoje mais de 30 empresas operam com agentes nesse modelo. Clínica que operava só em horário comercial agora converte de madrugada. Faculdade que perdia matrícula no fim de semana agora fecha vaga domingo à noite. Farmácia, escola, loja, agência. Setores diferentes, mesmo princípio. A NVIDIA mostrou na GTC que IA vai ser como eletricidade: onipresente, invisível e indispensável. Essas empresas já ligaram na tomada. Os resultados estão no caixa, não no PowerPoint.",

    "ato7_fechamento": "Manda esse vídeo pro amigo empresário que ainda acha que IA é gasto. Porque 600 bilhões de dólares não mentem. As maiores empresas do mundo não estão gastando. Estão investindo. A pergunta é: quanto vai te custar não investir?"
}

tel36 = "\n\n".join([r36[k] for k in r36])
words36 = len(tel36.split())

# ============================================================
# INDEX 37 - Atlassian demite 10%, Claude tornou equipes menores
# ============================================================
r37 = {
    "ato1_gancho": "A Atlassian, dona do Jira e do Trello, acabou de demitir centenas de funcionários. Cortou 10% da empresa inteira de uma vez. E sabe o que o CEO disse pra justificar? Que ferramentas de IA como o Claude da Anthropic tornaram equipes menores mais produtivas do que equipes grandes. Leu? Equipe menor rende mais. Ele não falou 'apesar de ser menor'. Falou 'porque é menor'. E isso muda tudo que você pensa sobre contratar gente.",

    "ato2_buraco": "A notícia saiu na mesma semana em que a NVIDIA abriu a GTC 2026 e o Jensen Huang mostrou que empresas vão gastar 600 bilhões em IA esse ano. Na mesma semana em que a Block cortou 4 mil. Na mesma semana em que a Meta confirmou planos de demitir 16 mil. Não são empresas isoladas. É um movimento coordenado. E todas dão a mesma justificativa: IA permite que menos gente entregue mais resultado. A Atlassian é o caso mais interessante porque ela vende ferramenta de produtividade. Jira, Trello, Confluence. Produtos que existem pra organizar o trabalho de equipes grandes. E agora a própria empresa que vende essas ferramentas tá dizendo: com IA, equipe grande é desperdício. É como se a fábrica de escada dissesse que inventou o elevador.",

    "ato3_virada": "E o detalhe que ninguém tá prestando atenção: o CEO citou o Claude nominalmente. Não foi IA genérica. Foi uma ferramenta específica. Ele tá dizendo que o Claude, o modelo que eu uso todo dia na minha operação, é bom o suficiente pra substituir centenas de funcionários da Atlassian. Eu entendi isso antes deles. Quando eu olhei pra minha operação com 37 vendedores e vi que 80% era custo sem retorno proporcional, eu não pensei em 'melhorar o time'. Pensei em reduzir o time e aumentar a inteligência. Menos gente, mais agente. Menos folha, mais processo.",

    "ato4_caos": "Mas a transição de equipe grande pra equipe pequena com IA não é só conta de planilha. É guerra humana. Quando eu comecei a reduzir o time, o clima virou pesadelo. Quem ficou achava que ia ser o próximo. Quem saiu espalhou pra todo mundo que a empresa tava quebrando. Um ex-vendedor postou no LinkedIn que eu tinha trocado pessoas por robô. Teve 200 curtidas e 40 comentários me xingando. Um cliente leu o post e me ligou perguntando se a empresa ia fechar. Perdi 3 clientes naquela semana por causa do post. O moral do time que ficou desmoronou. Minha melhor vendedora começou a procurar emprego escondido. Descobri quando um recrutador me ligou pedindo referência. O recrutador. Me ligando. Sobre a minha funcionária. Aquela semana eu entendi que a mudança mais difícil não é tecnológica. É humana.",

    "ato5_cta": "Mas eu mantive o curso. Conversei com cada pessoa que ficou. Expliquei o modelo. Mostrei os números. Quem ficou, ficou porque entendeu que o papel dela mudou. Não era mais operacional. Era estratégico. O vendedor virou closer. O atendente virou especialista de relacionamento. O agente assumiu tudo que era repetitivo. Em 90 dias, os 7 que ficaram vendiam mais do que os 37 de antes. Folha caiu 80%. Faturamento subiu. Se você sente que tem gente demais e resultado de menos, faz o quiz de maturidade em IA. Link na bio. 2 minutos. Você descobre onde tá a gordura e como cortar sem matar o músculo.",

    "ato6_recompensa": "Hoje mais de 30 empresas operam nesse modelo de equipe enxuta com inteligência artificial. Clínica que antes tinha 6 atendentes e resultado mediano, agora tem 2 com performance superior. Faculdade que gastava 50 mil de folha no comercial reduziu pra 15 mil e vende mais. O The Guardian publicou essa semana que existe um movimento global pedindo redução de jornada porque a IA tá eliminando a necessidade de trabalho humano em várias funções. Não é teoria. A Atlassian acabou de provar na prática. Menos gente, mais Claude, mais resultado.",

    "ato7_fechamento": "Manda esse vídeo pro amigo que acha que empresa grande precisa de time grande. Porque a dona do Jira e do Trello acabou de dizer o contrário. Equipe menor com IA vence equipe maior sem IA. Sempre."
}

tel37 = "\n\n".join([r37[k] for k in r37])
words37 = len(tel37.split())

# ============================================================
# INDEX 38 - Anthropic recusou uso militar, cresceu
# ============================================================
r38 = {
    "ato1_gancho": "Uma empresa de inteligência artificial disse não pro Pentágono. Recusou contrato militar. O governo americano retaliou e classificou ela como ameaça à segurança nacional. Todo mundo achou que ela ia quebrar. Sabe o que aconteceu? Ela explodiu. Atingiu 11 milhões de usuários por dia. Receita dobrando pra 20 bilhões de dólares. E ultrapassou o ChatGPT em downloads nos Estados Unidos. A empresa se chama Anthropic. E essa história tem uma lição que vale mais do que qualquer curso de marketing.",

    "ato2_buraco": "A Anthropic criou o Claude, um dos modelos de IA mais avançados do planeta. O Pentágono queria usar pra vigilância em massa e sistemas de armas autônomos. A Anthropic olhou pro contrato, olhou pros princípios dela e disse: não fazemos isso. O Pentágono não gostou. Classificou a empresa como risco de segurança nacional. A CIA cortou relações. Fornecedores do governo pararam de trabalhar com eles. O mercado inteiro esperava que a Anthropic fosse recuar, pedir desculpa e aceitar o contrato. Não recuou. Manteve a posição. E enquanto os analistas previam colapso, uma coisa inesperada aconteceu: o público escolheu a Anthropic. 11 milhões de usuários diários. Um milhão de novos cadastros todo dia. Receita projetada de 20 bilhões. Não por causa do produto. Por causa do posicionamento.",

    "ato3_virada": "E essa é a lição mais poderosa pra qualquer dono de empresa. Dizer não pro cliente errado é a melhor estratégia pra atrair o cliente certo. A maioria dos empresários morre de medo de recusar negócio. Aceita qualquer cliente que aparece. Faz qualquer coisa pra não perder venda. E acaba com operação inchada atendendo gente que não é o perfil ideal. Eu vivi isso. Quando eu tinha 37 vendedores, a gente aceitava todo mundo. Lead sem perfil, cliente que ia dar problema, negociação que não fazia sentido financeiro. Tudo. Porque o medo de perder era maior que a disciplina de filtrar.",

    "ato4_caos": "E sabe o que aconteceu? A operação ficou poluída. Vendedor gastando tempo com lead que nunca ia comprar. Suporte sobrecarregado com cliente que dava mais trabalho do que receita. Time desmotivado porque passava o dia apagando incêndio em vez de vender. Teve um mês que eu analisei: 40% do tempo do time comercial ia pra clientes que representavam 8% da receita. Oito por cento. Eu tava subsidiando gente que me custava dinheiro. E quando tentei cortar esses clientes, meu gerente comercial surtou. Disse que eu ia matar a receita. Que não podia recusar cliente. Que ia demitir ele se fizesse isso. Ele ameaçou sair. E por medo, eu recuei. Mantive os clientes tóxicos por mais 4 meses. Gastei mais 180 mil reais atendendo gente que me drenava. Quatro meses de sangria porque eu não tive coragem de dizer não.",

    "ato5_cta": "Até que eu disse. Cortei os clientes tóxicos. Defini perfil ideal. Coloquei agente de IA pra qualificar na entrada. Lead fora do perfil nem chega no vendedor. O vendedor só fala com quem tem chance real de comprar. Resultado: o tempo médio de venda caiu de 14 dias pra 4. A taxa de conversão dobrou. A satisfação do time subiu porque eles pararam de perder tempo com gente errada. A Anthropic provou no nível global e eu provei no nível local: dizer não é estratégia, não é fraqueza. Se você sente que sua operação tá poluída com cliente errado e trabalho inútil, faz o quiz de maturidade em IA. Link na bio. 2 minutos.",

    "ato6_recompensa": "Hoje mais de 30 empresas operam com esse modelo de qualificação inteligente. Clínica que antes atendia todo mundo e perdia tempo com consulta que não convertia, agora o agente filtra na entrada. Só chega no dentista quem tem perfil real. Faculdade que gastava 3 horas por dia respondendo curiosos que nunca iam se matricular, agora o agente resolve e só encaminha lead quente pro consultor. O princípio da Anthropic aplicado em escala local: foco no cliente certo, recusa do cliente errado, resultado superior.",

    "ato7_fechamento": "Manda esse vídeo pro amigo que tem medo de recusar cliente. Porque a Anthropic disse não pro maior comprador do planeta e faturou 20 bilhões. Às vezes, o melhor negócio que você faz é o negócio que você recusa."
}

tel38 = "\n\n".join([r38[k] for k in r38])
words38 = len(tel38.split())

# ============================================================
# INDEX 39 - Klarna: substituiu atendentes, qualidade caiu
# ============================================================
r39 = {
    "ato1_gancho": "Uma das maiores fintechs do mundo demitiu 700 atendentes e colocou IA no lugar. Cortou 40% dos custos de atendimento. Caso de sucesso. Capa de revista. O futuro do trabalho. Todo mundo aplaudiu. Só que agora, menos de dois anos depois, a Klarna tá contratando humanos de volta. Porque a qualidade despencou. Cliente reclamando. Atendimento genérico. Caso complexo sem solução. O CEO admitiu publicamente que errou. Se você tá pensando em substituir seu time por IA, esse vídeo pode te salvar de cometer o mesmo erro.",

    "ato2_buraco": "A Klarna é uma das maiores empresas de pagamento do mundo. Fatura bilhões. Em 2024, ela substituiu o equivalente a 700 atendentes humanos por um assistente de IA. Dois terços de todos os chats de suporte passaram a ser resolvidos por máquina. No primeiro momento, os números eram lindos. Tempo de resposta caiu pra menos de 2 minutos. Custo operacional caiu 40%. Eficiência de resolver caso simples disparou. O Sebastian Siemiatkowski, CEO da Klarna, virou palestrante de evento de IA. Todo mundo queria saber como ele tinha feito. Caso de referência global. Reportagem na Forbes, Financial Times, Bloomberg. O cara virou poster child da revolução da IA no atendimento.",

    "ato3_virada": "Só que por trás dos números bonitos, a bomba tava armando. Clientes com problema complexo ficavam presos num loop. A IA respondia com template. O cliente insistia. A IA repetia o template com palavras diferentes. O cliente ficava irritado. Pedia humano. Não tinha humano. A nota de satisfação começou a cair. Reclamação em rede social começou a subir. O Siemiatkowski admitiu publicamente que o foco excessivo em eficiência comprometeu a qualidade. E aí fez o que ninguém esperava: anunciou que ia contratar humanos de volta. O poster child da IA no atendimento voltando atrás. A manchete rodou o mundo. E todo empresário que tava copiando o modelo da Klarna parou pra pensar.",

    "ato4_caos": "E eu quase cometi o mesmo erro. Quando coloquei agentes de IA na minha operação, a tentação foi fazer igual a Klarna: substituir todo mundo. Tirar humano, botar IA e ver o custo despencar. E no começo, funcionou. Os primeiros 30 dias foram mágicos. Custo caiu. Velocidade subiu. Lead respondido em segundos. Mas no dia 45, começaram os problemas. Cliente com situação complexa preso no loop. IA repetindo resposta que não resolvia. Um lead de 150 mil reais de contrato anual mandou mensagem pedindo atendimento personalizado. O agente respondeu com proposta genérica. O lead respondeu: 'vocês não me ouvem'. E cancelou. 150 mil por ano. Evaporou. Outro cliente, que tava comigo há 2 anos, mandou email dizendo que se sentia um número. Que antes falava com gente de verdade e agora falava com robô. Pediu cancelamento. Nesses 2 meses de modelo 100% IA, perdi 7 clientes e mais de 400 mil reais de receita anual. A economia na folha era de 80 mil por mês. Perdi 400 mil de receita tentando economizar 80 mil de custo.",

    "ato5_cta": "Foi aí que eu entendi o que a Klarna aprendeu do jeito caro: o modelo certo não é 100% IA e nem 100% humano. É híbrido. IA faz o que máquina faz melhor: resposta rápida, qualificação, triagem, follow-up, agendamento. Humano faz o que humano faz melhor: empatia, negociação complexa, relacionamento, fechamento. Redesenhei a operação. Agente na frente. Humano na decisão. Em 60 dias, recuperei 4 dos 7 clientes que tinham saído. E os novos chegavam mais qualificados do que nunca. Se você quer colocar IA na operação sem cometer o erro da Klarna e sem passar pelo prejuízo que eu passei, faz o quiz de maturidade em IA. Link na bio. 2 minutos.",

    "ato6_recompensa": "Hoje mais de 30 empresas operam com esse modelo híbrido. Clínica onde o agente faz triagem, agenda e confirma, e o dentista só cuida do paciente. Faculdade onde o agente qualifica, manda proposta e responde dúvida operacional, e o consultor só fecha. Farmácia onde o agente monitora estoque e atende cliente repetitivo, e o farmacêutico cuida do caso que precisa de expertise humana. O resultado é consistente: custo menor, satisfação maior, escala real. A Klarna tentou trocar gente por máquina e descobriu que não funciona. Essas empresas colocaram máquina e gente trabalhando juntas e provaram que funciona.",

    "ato7_fechamento": "Manda esse vídeo pro amigo que acha que é só substituir todo mundo por IA e cortar custo. Porque a Klarna fez isso com 700 atendentes e tá contratando de volta. O caminho não é extremo. É inteligente. E quem entender isso primeiro, domina."
}

tel39 = "\n\n".join([r39[k] for k in r39])
words39 = len(tel39.split())

# Build the array
all_new = [
    (25, r25, tel25, words25),
    (26, r26, tel26, words26),
    (27, r27, tel27, words27),
    (28, r28, tel28, words28),
    (29, r29, tel29, words29),
    (30, r30, tel30, words30),
    (31, r31, tel31, words31),
    (32, r32, tel32, words32),
    (33, r33, tel33, words33),
    (34, r34, tel34, words34),
    (35, r35, tel35, words35),
    (36, r36, tel36, words36),
    (37, r37, tel37, words37),
    (38, r38, tel38, words38),
    (39, r39, tel39, words39),
]

# Re-read file to get latest version (in case lote 2 was saved)
with open('/tmp/roteiros-edit/roteiros.json') as f:
    data = json.load(f)

for idx, roteiro, teleprompter, word_count in all_new:
    # Count sentences
    import re
    sentences = len([s for s in re.split(r'[.!?]+', teleprompter) if s.strip()])
    
    # Calculate duration (approx 150 words per minute for speaking)
    duration_min = word_count / 150
    minutes = int(duration_min)
    seconds = int((duration_min - minutes) * 60)
    duration_str = f"{minutes}:{seconds:02d}"
    
    data[idx]['roteiro'] = roteiro
    data[idx]['teleprompter'] = teleprompter
    data[idx]['metricas'] = {
        'totalPalavras': word_count,
        'totalFrases': sentences,
        'duracaoFinal': duration_str
    }
    
    print(f"Index {idx}: {word_count} palavras, {sentences} frases, ~{duration_str}")

# Save
with open('/tmp/roteiros-edit/roteiros.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nSalvo com sucesso!")
print(f"Total roteiros no arquivo: {len(data)}")
