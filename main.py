'''
Mapa de adjacência dos bares.
'''
mapa = {
    'flama': [
        ('boteco_do_cruz', 100),
        ('bar_amizade', 130),
        ('psj',140),
        ('container',150)
        ],
    'bar_amizade': [('flama', 30)],
    'boteco_do_cruz': [('flama', 60), ('psj', 60),('container',120)],
    'psj': [('container', 130), ('skina', 120),('polska',130)],
    'skina': [('container', 80), ('oponente', 80), ('psj', 80), ('franconi', 100),('franca',80),('universitario_bar',80),('leila',60)],
    'container': [('skina', 140), ('oponente', 140),('franconi',140),('franca',140),('leila',140)],
    'polska': [('container', 20), ('oponente', 10),('franconi',10),('franca',10),('leila',10)],
    'leila': [('container', 40), ('oponente', 40),('franconi',40),('franca',40),('polska',40)],
    'franca': [('container', 10), ('oponente', 10),('franconi',10),('universitario_bar',20),('leila',10)],
    'universitario_bar': [('franca', 10), ('oponente', 10),('leila',10)],
    'oponente': [('franca', 60), ('franconi', 60),('container',60)],
    'franconi': [ ('oponente', 100),('franca',100),('container',100),('ze',100),('papuera',100),('vizinho_franconi',100)],
    'papuera': [('franconi', 50),('ze',50),('fora_de_hora',50)],
    'vizinho_franconi': [('franconi', 10),('papuera',10)],
    'fora_de_hora': [('papuera', 50),('ze',50)],
    'zezinho': [('ze',30),('barnaneiras',30),('fora_de_hora',30)],
    'barnaneiras': [('zezinho',30),('fora_de_hora',30),('ze',30)],
    'ze': [('franconi',40),('bocao',40),('zezinho',40)],
    'bocao': [('ze',40),('fora_de_hora',40)]
}

bares = {

    'flama': {
        'nota': 4.8,
        'horario_fechamento': '23:00',
        'tipo': 'arrumadinho',
        'tem_sinuca': True
    },

    'bar_amizade': {
        'nota': 2.0,
        'horario_fechamento': '23:00',
        'tipo': 'bar',
        'tem_sinuca': False
    },

    'boteco_do_cruz': {
        'nota': 3.5,
        'horario_fechamento': '01:00',
        'tipo': 'arrumadinho',
        'tem_sinuca': False
    },

    'psj': {
        'nota': 4.8,
        'horario_fechamento': '00:00',
        'tipo': 'arrumadinho',
        'tem_sinuca': False
    },

    'skina': {
        'nota': 4.0,
        'horario_fechamento': '00:00',
        'tipo': 'bar',
        'tem_sinuca': False
    },

    'container': {
        'nota': 4.9,
        'horario_fechamento': '0:30',
        'tipo': 'arrumadinho',
        'tem_sinuca': True
    },

    'polska': {
        'nota': 2.0,
        'horario_fechamento': '00:00',
        'tipo': 'venda',
        'tem_sinuca': False
    },

    'leila': {
        'nota': 3.8,
        'horario_fechamento': '01:00',
        'tipo': 'bar',
        'tem_sinuca': True
    },

    'franca': {
        'nota': 3.5,
        'horario_fechamento': '02:00',
        'tipo': 'bar',
        'tem_sinuca': False
    },

    'universitario_bar': {
        'nota': 3.1,
        'horario_fechamento': '00:00',
        'tipo': 'chinelao',
        'tem_sinuca': False
    },

    'oponente': {
        'nota': 4.7,
        'horario_fechamento': '02:00',
        'tipo': 'chinelao',
        'tem_sinuca': True
    },

    'franconi': {
        'nota': 4.9,
        'horario_fechamento': '02:00',
        'tipo': 'bar',
        'tem_sinuca': False
    },

    'papuera': {
        'nota': 4.0,
        'horario_fechamento': '03:00',
        'tipo': 'bar',
        'tem_sinuca': False
    },

    'vizinho_franconi': {
        'nota': 2.0,
        'horario_fechamento': '01:00',
        'tipo': 'chinelao',
        'tem_sinuca': True
    },

    'fora_de_hora': {
        'nota': 4.0,
        'horario_fechamento': '04:00',
        'tipo': 'chinelao',
        'tem_sinuca': False
    },

    'zezinho': {
        'nota': 4.2,
        'horario_fechamento': '02:00',
        'tipo': 'chinelao',
        'tem_sinuca': False
    },

    'barnaneiras': {
        'nota': 3.5,
        'horario_fechamento': '04:00',
        'tipo': 'chinelao',
        'tem_sinuca': False
    },

    'ze': {
        'nota': 3.8,
        'horario_fechamento': '03:00',
        'tipo': 'chinelao',
        'tem_sinuca': False
    },

    'bocao': {
        'nota': 4.0,
        'horario_fechamento': '03:00',
        'tipo': 'chinelao',
        'tem_sinuca': True
    }
}

def selecionaBarInicial():      
    print("""
===============================
      ESCOLHA O BAR INICIAL
===============================
 
 [1]  Flama
 [2]  Boteco do Cruz
 [3]  PSJ
 [4]  Skina
 [5]  Container
 [6]  Polska
 [7]  Leila
 [8]  Franca
 [9]  Universitario Bar
[10]  Oponente
[11]  Franconi
[12]  Papuera
[13]  Vizinho Franconi
[14]  Fora de Hora
[15]  Zezinho
[16]  Barnaneiras
[17]  Zé
[18]  Bocão
 
===============================
""")
    op = int(input())              
    match op:
        case 1:  barPartida = 'flama'
        case 2:  barPartida = 'boteco_do_cruz'
        case 3:  barPartida = 'psj'
        case 4:  barPartida = 'skina'           
        case 5:  barPartida = 'container'
        case 6:  barPartida = 'polska'
        case 7:  barPartida = 'leila'
        case 8:  barPartida = 'franca'
        case 9:  barPartida = 'universitario_bar'
        case 10: barPartida = 'oponente'
        case 11: barPartida = 'franconi'
        case 12: barPartida = 'papuera'
        case 13: barPartida = 'vizinho_franconi'
        case 14: barPartida = 'fora_de_hora'    
        case 15: barPartida = 'zezinho'    
        case 16: barPartida = 'barnaneiras'
        case 17: barPartida = 'ze'
        case 18: barPartida = 'bocao'
        case _:
            print("opção invalida, container por padrão.")
            barPartida = 'container'
 
    return barPartida
    

def calculaTempoMaximo(horaPartida, horaChegada):
    if horaChegada < horaPartida:
        horaChegada += 24

    tempoMaximo = (horaChegada - horaPartida)*60

    return tempoMaximo


def coletaParametros():
    print("gerador de rota de bares:")
    print("-------------------------")
    print()
    print("que horas começa:")
    horaPartida = int(input())
    print("que horas termina:")
    horaChegada = int(input())
    print("qual o bar inicial:")
    barPartida = selecionaBarInicial()
    print("máximo de bares:")
    maxBares = int(input())
    print("sinuca? (sim/nao)")
    res = input().lower()
    if res == 'sim':
        sinuca = True
    else:
        sinuca = False

    tempoMaximo = calculaTempoMaximo(horaPartida, horaChegada)
    return (
        horaPartida,
        tempoMaximo,
        barPartida,
        maxBares,
        sinuca
    )

def rota(mapa, bares, barPartida, maxBares, tempoMaximo, sinuca, horaPartida):
    rotasEncontradas = []

    def dfs(barAtual, rotaAtual, tempoGasto):

        print(f"bar: {barAtual}")
        print(f"rota: {rotaAtual}")
        
        registraRota = True
        for vizinho, distancia in mapa[barAtual]:
            if vizinho in rotaAtual:
                continue

            tempoAteVizinho = tempoGasto + distancia

            if tempoAteVizinho > tempoMaximo:
                continue
            if len(rotaAtual) >= maxBares:
                continue
            if sinuca and not bares[vizinho]['tem_sinuca']:
                continue

            registraRota = False
            dfs(vizinho, rotaAtual + [vizinho], tempoAteVizinho) 
        
        if registraRota:
            rotasEncontradas.append(rotaAtual)
    
    dfs(barPartida, [barPartida], 0)
    print("Rotas encontradas:")
    for rota in rotasEncontradas:
        print(rota)

    def calculaNota(rota):
        return sum(bares[bar]['nota'] for bar in rota) / len(rota)

    melhorRota = max(rotasEncontradas, key=calculaNota)
        
    print("Melhor rota:")
    print(melhorRota)


def main():
  horaPartida, tempoMaximo, barPartida, maxBares, sinuca = coletaParametros()
  rota(mapa, bares, barPartida, maxBares, tempoMaximo, sinuca, horaPartida)


main()