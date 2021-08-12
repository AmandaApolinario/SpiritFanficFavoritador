import random

todascontas = []
FILE = open('NomesEContas/dados.txt', 'a')

for i in range(25):
    char = "0123abcdefghijklmnopqrstuvwxyz"
    maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nome = ["lisa","jisoo","soyeon","dream","jimin","jungkook","minnie","suga","cherry","moon","sunset","patty","amanda","lely","star","light","glitter","shine","angel","cherry","baby","gurl","sweet","sweetie","boom","euphoria","extasy","petrichor","angst","aesthete","nadir","miraculous","lassitude","aurora","serendipity","cherish","felicity","epiphany","nemesis","pristine","opulence","renaissance","sunshine"]
    tam = len(nome)

    usuario = nome[random.randint(0,tam-1)]+ maiusculo[random.randint(0,25)] + char[random.randint(0,29)] + char[random.randint(0,29)]
    todascontas.append(usuario)
    FILE.write(usuario)
    FILE.write("\n")
