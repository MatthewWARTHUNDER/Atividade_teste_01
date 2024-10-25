from codigo import *


def test_email_valido():
    assert email_valido("teste@exemplo.com") == True
    assert email_valido("teste@exemplo") == False
    assert email_valido("email.com") == False


def test_eh_par():
    assert eh_par(4) == True
    assert eh_par(5) == False


def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(4) == 24
    assert fatorial(2) == 2

def test_quadrado():
    assert quadrado(2) == 4
    assert quadrado(5) == 25
    assert quadrado(6) == 36

def test_eh_positivo():
    assert eh_positivo(2) == True
    assert eh_positivo(-2) == False
    assert eh_positivo(-3) == False

def test_eh_idade():
    assert verificar_maioridade(17) == 'menor de idade'
    assert verificar_maioridade(18) == 'maior de idade'
    assert verificar_maioridade(3) == 'menor de idade'

def test_eh_temperatura():
    assert classificar_temperatura(25) == 'moderado'
    assert classificar_temperatura(50) == 'quente'
    assert classificar_temperatura(-15) ==  'frio'

def test_eh_nota():
    assert avaliar_nota(7) == 'aprovado'
    assert avaliar_nota(5) == 'recuperacao'
    

def test_eh_votar():
    assert pode_votar(18) == 'voto obrigatório'
    assert pode_votar(15) == 'não pode votar'
    assert pode_votar(12) == 'não pode votar'
    assert pode_votar(16) == 'voto facultativo'

def test_eh_avaliar_produto():
    assert avaliar_produto(5) == 'excelente'
    assert avaliar_produto(4) == 'bom'
    assert avaliar_produto(3) == 'regular'
    assert avaliar_produto(2) == 'ruim'
    assert avaliar_produto(1) == 'péssimo'
    

def test_se_a_mais_b():
    assert soma (8, 9) == 17
    assert soma (5, 5) == 10
    assert soma (6, 7) == 13


def test_se_a_menos_b():
    assert subtrai (5, 3) == 2
    assert subtrai (3, 3) == 0
    assert subtrai (4, 2) == 2

def test_se_a_vezes_b():
    assert multiplica (5, 5) == 25
    assert multiplica (6, 6) == 36
    assert multiplica (6, 4) == 24

def test_se_a_dividos_b():
    assert divide (4, 2) == 2
    assert divide (6, 2) == 3
    assert divide (64, 8) == 8

def test_area_circulo():
    assert area_circulo(3) == math.pi * 9
    assert area_circulo(-1) == "Erro: o raio não pode ser negativo."

def test_area_retangulo():
    assert area_retangulo(3, 4) == 12
    assert area_retangulo(-1, 4) == "Erro: largura e altura devem ser não-negativos."
    assert area_retangulo(3, -2) == "Erro: largura e altura devem ser não-negativos."