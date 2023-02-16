print("Seja Muito Bem-Vindo ao Quiz do TRAP MUSIC!")
an_user = input("Quer Começar? (sim/nao)").lower()

if an_user != "sim":
    quit()

score = 0

print("O quiz esta iniciando…")
print("Qual foi o ano de lançamento do segundo álbum de estúdio do grupo Migos intitulado Culture? \n (A) 18 de Agosto de 2016 \n (B) 27 de Janeiro de 2017 \n (C) 15 de Fevereiro de 2018 \n (D) 16 de Março de 2018 \n")
an_1 = input("Resposta: ").upper()

if an_1 == "B":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print("PROXIMA PERGUNTA!")

print("Qual nome completo de Travis scott? \n (A) Jacques Berman Webster II \n (B) Jacques Jack Webster II \n (C) Jacques Webster II \n (D) Jacques Berman II \n")
an_2 = input("Resposta: ").upper()

if an_2 == "A":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print("PROXIMA PERGUNTA!")

print("Qual desses artistas possui um grammy? \n (A) Lil Yachty \n (B) Trippie Redd \n (C) Travis Scott \n (D) 21Savage \n")
an_3 = input("Resposta: ").upper()

if an_3 == "D":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print("PROXIMA PERGUNTA!")

print("Qual artista foi responsável por popularizar o gênero Drill no mundo? \n (A) Central Cee \n (B) King Von \n (C) Lil Tjay \n (D) Pop Smoke \n")
an_4 = input("Resposta: ").upper()

if an_4 == "D":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print("PROXIMA PERGUNTA!")

print("Qual Musica possui mais Visualizacoes no Spotify? \n (A) Calling My Phone - Lil Tjay \n (B) Freestyle - Lil Baby \n (C) RAPSTAR - Polo G \n (D) Time Today - Moneybagg Yo \n")
an_5 = input("Resposta: ").upper()

if an_5 == "C":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print("PROXIMA PERGUNTA!")

print("Qual desses artistas não possui música colaborativa com Young Thug? \n (A) Central Cee \n (B) Polo G \n (C) Dababy \n (D) Kodak Black \n")
an_6 = input("Resposta: ").upper()

if an_6 == "A":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print("PROXIMA PERGUNTA!")

print("Qual desses artistas Sampleou a clássica música 'Say My Name' do grupo Destiny's Child? \n (A) Pop Smoke \n (B) Drake \n (C) Fivio Foreign \n (D) Gucci Mane \n")
an_7 = input("Resposta: ").upper()

if an_7 == "C":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print("PROXIMA PERGUNTA!")

print("Qual desses artistas Não lançou álbum em 2020? \n (A) Don Toliver \n (B) Roddy Ricch \n (C) Drake \n (D) Lil Baby \n")
an_8 = input("Resposta: ").upper()

if an_8 == "B":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print("PROXIMA PERGUNTA!")

print("Qual desses artistas não fez show no Brasil? \n (A) Quavo \n (B) A$AP Rocky \n (C) Travis Scott \n (D) Future \n")
an_9 = input("Resposta: ").upper()

if an_9 == "D":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print("PROXIMA PERGUNTA!")

print("Qual desses artistas não possui um album colaborativo com Future? \n (A) Drake \n (B) Gunna \n (C) Lil Uzi Vert \n (D) Juice WRLD \n")
an_10 = input("Resposta: ").upper()

if an_10 == "B":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print(f"O quiz acabou... Pontuação: {score}/10")
