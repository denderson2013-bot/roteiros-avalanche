import json, re

with open('/tmp/roteiros-edit/roteiros.json') as f:
    data = json.load(f)

r25 = {
    "ato1_gancho": "Sabe qual cargo tá sendo extinto em 2026? Não é operário. Não é estagiário. Não é recepcionista. É gerente. A Gartner, maior consultoria de tecnologia do mundo, confirmou essa semana que 20% das grandes empresas já estão usando inteligência artificial pra eliminar mais da metade dos cargos de gerência média. Vinte por cento. Não é previsão. É dado real, coletado de empresas que já fizeram o corte. Se você é gerente, coordenador ou supervisor, esse vídeo vai te tirar o sono. Se você é dono de empresa, vai te dar ideias perigosas.",

    "ato2_buraco": "Pensa comigo no que um gerente médio faz no dia a dia. Cobra relatório. Monitora performance. Organiza agenda do time. Repassa informação de cima pra baixo e de baixo pra cima. Filtra dados. Manda email cobrando prazo. Agenda reunião pra falar sobre outra reunião. Agora olha essa lista e me diz: qual dessas tarefas um agente de IA não faz melhor, mais rápido e sem reclamar? Nenhuma. O agente monitora em tempo real. Gera relatório instantâneo. Prioriza tarefas automaticamente. Manda alerta pro diretor sem precisar de intermediário. A camada do meio existia porque a informação precisava de tradutor humano. A IA eliminou a necessidade de tradução. E junto com ela, eliminou o tradutor. A Gartner projeta que até 2028, 50% das organizações vão ter achatado suas hierarquias especificamente por causa de agentes de IA. Cinquenta por cento. Não é um departamento perdendo gente. É a estrutura inteira mudando.",

    "ato3_virada": "E aqui é onde a história muda pra quem tem visão. Enquanto gerente tá com medo de perder o emprego, dono de empresa tá calculando quanto economiza. Eu vivi isso na pele. Tinha uma operação com 37 vendedores. Folha entre 90 e 120 mil reais por mês. No meio disso, três coordenadores, dois supervisores, um gerente comercial. Seis pessoas só pra garantir que os outros 31 fizessem o trabalho deles. E quando olhei os números de verdade, esses 6 da gerência média custavam quase 40% da folha. E entregavam informação que eu podia ter num dashboard em tempo real. Quando coloquei agentes de IA pra atender, qualificar e fazer follow-up 24 horas, a primeira coisa óbvia foi: eu não precisava mais de ninguém cobrando ninguém.",

    "ato4_caos": "Mas antes de achar que foi tudo lindo, deixa eu contar o que aconteceu no meio do caminho. Quando comecei a transição, um coordenador que tava comigo há 3 anos entrou em modo sabotagem. Desligava automação. Mudava configuração do CRM de propósito. Espalhava pro time que a IA ia dar errado. Em duas semanas, a operação virou caos. Lead caindo sem resposta porque alguém desativou o agente. Mensagem duplicada porque as regras tinham sido alteradas. Cliente ligando furioso porque recebeu proposta errada. Perdi 14 vendas confirmadas num único mês por causa dessa sabotagem interna. Sentei na cadeira do escritório às 2 da manhã pensando que tinha cometido o maior erro da minha vida profissional. Que talvez a estrutura antiga, com toda a gordura, era mais segura que essa bagunça nova.",

    "ato5_cta": "Não voltei atrás. Reconstruí do zero. Processo antes de tecnologia. Regras claras pro agente. Supervisão humana nos pontos críticos. E o mais importante: conversa honesta com o time. Quem queria ficar, ficou numa função que fazia sentido. Quem não queria se adaptar, saiu. Em 60 dias, a operação tava rodando melhor do que nunca. Atendimento 24 horas. Lead respondido em 3 segundos. Qualificação automática com 94% de precisão. Folha caiu 80%. Se você é dono de empresa e sente que tem gente demais fazendo trabalho que máquina faz melhor, faz o quiz de maturidade em IA. Link na bio. São 2 minutos. Você descobre onde tá e o que precisa mudar primeiro.",

    "ato6_recompensa": "Hoje mais de 30 empresas rodam com esse modelo. Clínica que tinha coordenadora de atendimento ganhando 5 mil por mês só pra repassar mensagem de paciente pro dentista. Agora o agente faz triagem, agenda e confirma sozinho. Faculdade que tinha supervisor de matrícula controlando planilha no braço. Agora o agente qualifica o aluno, manda proposta personalizada e fecha matrícula sábado de madrugada. Farmácia, escola, loja, agência. O padrão é sempre o mesmo: a camada do meio era um gargalo disfarçado de estrutura. Quando tira, a informação flui direto, a decisão acontece mais rápido e o custo despenca. A Gartner confirmou o que essas empresas já vivem na prática.",

    "ato7_fechamento": "Manda esse vídeo pro gerente que acha que tá seguro porque sempre entregou resultado. Porque a Gartner não tá falando de gerente ruim. Tá falando de gerente. Ponto. A função tá sumindo. E quem não se reposicionar agora vai descobrir tarde demais."
}

teleprompter = "\n\n".join([r25[k] for k in r25])
word_count = len(teleprompter.split())
sentences = len([s for s in re.split(r'[.!?]+', teleprompter) if s.strip()])
duration_min = word_count / 150
minutes = int(duration_min)
seconds = int((duration_min - minutes) * 60)

data[25]['roteiro'] = r25
data[25]['teleprompter'] = teleprompter
data[25]['metricas'] = {
    'totalPalavras': word_count,
    'totalFrases': sentences,
    'duracaoFinal': f"{minutes}:{seconds:02d}"
}

print(f"Index 25: {word_count} palavras, {sentences} frases")

with open('/tmp/roteiros-edit/roteiros.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Salvo!")
