import random
import mysql.connector
import tkinter as tk
from tkinter import messagebox
      
# Função para conectar ao banco de dados MySQL
def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Tabuada"
        )
        return conexao
    except mysql.connector as erro:
        print("Erro ao conectar ao banco de dados:", erro)

# Função para criar a tabela de ranking se não existir
def criar_tabela_ranking(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS ranking (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nome VARCHAR(50),
                            pontos INT
                        )""")
        conexao.commit()
        cursor.close()
    except mysql.connector as erro: 
        print("Erro ao criar a tabela de ranking:", erro)
# Função para inserir pontuação no ranking
def inserir_pontuacao(conexao, nome, pontos):
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO ranking (nome, pontos) VALUES (%s, %s)", (nome, pontos))
        conexao.commit()
        cursor.close()
    except mysql.connectorconnector as erro:
        print("Erro ao inserir pontuação no ranking:", erro)

# Função para mostrar o ranking
def mostrar_ranking(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, pontos FROM ranking ORDER BY pontos DESC LIMIT 10")
        ranking = cursor.fetchall()
        print("\nRanking:")
        for posicao, (nome, pontos) in enumerate(ranking, start=1):
            print(f"{posicao}. {nome}: {pontos} pontos")
        cursor.close()
    except mysql.connectorconnector as erro:
        print("Erro ao mostrar ranking:", erro)
        
def _init_(self, root):
        self.root = root
        self.root.title("Jogo de Tabuada")
        self.root.geometry("400x300")  # Tamanho da janela
        self.root.configure(bg="green")  # Cor de fundo
        
# Função principal do jogo
def jogo_tabuada():
    print("Bem-vindo ao jogo da tabuada!\n")
    nome_jogador = input("Digite seu nome: ")

    conexao_bd = conectar_bd()
    if conexao_bd:
        criar_tabela_ranking(conexao_bd)
    pontuacao = 0
    for _ in range(10):  # 10 perguntas
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        resposta_correta = num1 * num2
        resposta_jogador = int(input(f"Quanto é {num1} * {num2}? "))

        if resposta_jogador == resposta_correta:
            print("Resposta correta!\n")
            pontuacao += 10
        else:
            print(f"Resposta incorreta! A resposta correta era {resposta_correta}\n")

    print(f"Fim do jogo! Sua pontuação: {pontuacao} pontos")

    if conexao_bd:
        inserir_pontuacao(conexao_bd, nome_jogador, pontuacao)
        mostrar_ranking(conexao_bd)
        conexao_bd.close()

# Execução do jogo
jogo_tabuada()
