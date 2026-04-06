import json, re

with open('/tmp/roteiros-edit/roteiros.json') as f:
    data = json.load(f)

# Rewrite index 25 to be tighter (650-750 words)
r25 = {
    "ato1_gancho": "Sabe qual cargo tá sendo extinto em 2026? Não é operário. Não é estagiário. É gerente. A Gartner, maior consultoria de tecnologia do mundo, confirmou que 20% das grandes empresas já estão usando IA pra eliminar mais da metade dos cargos de gerência média. E não é previsão. É dado real. Se você é gerente, esse vídeo vai te tirar o sono. Se você é dono de empresa, vai te dar ideias perigosas.",

    "ato2_buraco": "Pensa no que um gerente médio faz. Cobra relatório. Monitora performance. Organiza agenda. Repassa informação de cima pra baixo. Filtra dados. Agenda reunião pra falar sobre outra reunião. Agora me diz: qual dessas tarefas um agente de IA não faz melhor e mais rápido? Nenhuma. O agente monitora em tempo real. Gera relatório instantâneo. Prioriza tarefas automaticamente. Manda alerta pro diretor sem intermediário. A camada do meio existia porque a informação precisava de tradutor. A IA eliminou a tradução. E junto com ela, eliminou o tradutor. A Gartner projeta que até 2028, 50% das organizações vão achatar suas hierarquias por causa de agentes de IA.",

    "ato3_virada": "Enquanto gerente tá com medo, dono de empresa tá calculando. Eu vivi isso na pele. Tinha 37 vendedores. Folha entre 90 e 120 mil por mês. No meio disso, três coordenadores, dois supervisores, um gerente comercial. Seis pessoas só pra garantir que os outros 31 trabalhassem. Esses 6 custavam quase 40% da folha. E o resultado que entregavam era informação que eu podia ter num dashboard em tempo real. Quando coloquei agentes de IA pra atender e qualificar 24 horas, a primeira coisa óbvia foi: eu não precisava mais de ninguém cobrando ninguém.",

    "ato4_caos": "Mas antes de achar que foi lindo, deixa eu contar o que aconteceu. Quando comecei a transição, um coordenador que tava comigo há 3 anos entrou em modo sabotagem. Desligava automação. Mudava config do CRM. Falava pro time que a IA ia dar errado. Em duas semanas, a operação virou caos. Lead caindo sem resposta. Agente mandando mensagem duplicada. Cliente reclamando de proposta errada. Perdi 14 vendas confirmadas num único mês. Sentei na cadeira às 2 da manhã pensando que tinha cometido o maior erro da minha vida. Que talvez a estrutura antiga, com toda a gordura, era melhor que essa bagunça.",

    "ato5_cta": "Não voltei atrás. Reconstruí do zero. Processo antes de tecnologia. Regras claras pro agente. Supervisão humana nos pontos críticos. Conversa honesta com o time. Quem queria ficar, ficou numa função que fazia sentido. Quem não se adaptava, saiu. Em 60 dias, a operação rodava melhor que nunca. Atendimento 24 horas. Lead respondido em 3 segundos. Qualificação com 94% de precisão. Folha caiu 80%. Se você sente que tem gente demais fazendo trabalho que máquina faz melhor, faz o quiz de maturidade em IA. Link na bio. 2 minutos.",

    "ato6_recompensa": "Hoje mais de 30 empresas rodam com esse modelo. Clínica que tinha coordenadora ganhando 5 mil pra repassar mensagem de paciente pro dentista. Agora o agente faz triagem, agenda e confirma sozinho. Faculdade que tinha supervisor controlando planilha no braço. Agora o agente qualifica, manda proposta e fecha matrícula sábado de madrugada. O padrão é sempre o mesmo: a camada do meio era gargalo disfarçado de estrutura. Quando tira, a informação flui direto e o custo despenca.",

    "ato7_fechamento": "Manda esse vídeo pro gerente que acha que tá seguro porque sempre entregou resultado. A Gartner não tá falando de gerente ruim. Tá falando de gerente. Ponto. A função tá sumindo. E quem não se reposicionar agora vai descobrir tarde demais."
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

print(f"Index 25 fixed: {word_count} palavras, {sentences} frases")

with open('/tmp/roteiros-edit/roteiros.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Salvo!")
