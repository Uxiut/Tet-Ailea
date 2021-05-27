# print("KIVI PAPERI SAKSET")
# def alku():
#     print("Pelaaja 1, valitse k, p tai s")
#     pelaaja_input1 = input()
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print(" ")
#     print("Pelaaja 2, valitse k, p tai s")
#     pelaaja_input2 = input()
#     return pelaaja_input1, pelaaja_input2

# def peli(pelaajainput1,pelaajainput2):
#     if pelaajainput1 == pelaajainput2:
#         print("Tasapeli")
#         return alku()
#     elif pelaajainput1 == "k" and pelaajainput2 == "p":
#         return print("Pelaaja 2 voitti!")
#     elif pelaajainput1 == "p" and pelaajainput2 == "k":
#         return print("Pelaaja 1 voitti!")
#     elif pelaajainput1 == "s" and pelaajainput2 == "k":
#         return print("Pelaaja 2 voitti!")
#     elif pelaajainput1 == "k" and pelaajainput2 == "s":
#         return print("Pelaaja 1 voitti!")
#     elif pelaajainput1 == "p" and pelaajainput2 == "s":
#         return print("Pelaaja 2 voitti!")
#     elif pelaajainput1 == "s" and pelaajainput2 == "p":
#         return print("Pelaaja 1 voitti!")
    

a1 = " # "; a2 = " # "; a3 = " # "; a4 = " # "; a5 = " # "; b1 = " # "; b2 = " # "; b3 = " # "; b4 = " # "; b5 = " # "; c1 = " # "; c2 = " # "; c3 = " # "; c4 = " # "; c5 = " # "; d1 = " # "; d2 = " # "; d3 = " # "; d4 = " # "; d5 = " # "; e1 = " # "; e2 = " # "; e3 = " # "; e4 = " # "; e5 = " # "
#def valmistelu1(laivat1):
kentta1 = [[a1,b1,c1,d1,e1],[a2,b2,c2,d2,e2],[a3,b3,c3,d3,e3],[a4,b4,c4,d4,e4],[a5,b5,c5,d5,e5]]

# (gamer1,gamer2) = alku()
# peli(gamer1,gamer2)
# input()
def position_solver2(kohta1,kohta2):
    global kentta1
    if kohta1 == "a1" and kentta1[1][0] != " H " and kentta1[0][1] != " H ":
        kentta1[0][0] = " H "
    elif kohta1 == "a2" and kentta1[0][0] != " H " and kentta1[1][1] != " H " and kentta1[2][0] != " H ":
        kentta1[1][0] = " H "
    elif kohta1 == "a3" and kentta1[1][0] != " H " and kentta1[2][1] != " H " and kentta1[3][0] != " H ":
        kentta1[2][0] = " H "
    elif kohta1 == "a4" and kentta1[2][0] != " H " and kentta1[3][1] != " H " and kentta1[4][0] != " H ":
        kentta1[3][0] = " H "
    elif kohta1 == "a5" and kentta1[3][0] != " H " and kentta1[4][1] != " H ":
        kentta1[4][0] = " H "
    elif kohta1 == "b1" and a1 != " H " and kentta1[0][2] != " H " and kentta1[1][1] != " H ":
        kentta1[0][1] = " H "
    elif kohta1 ==  "b2" and kentta1[1][0] != " H " and kentta1[1][2] != " H " and kentta1[0][1] != " H " and kentta1[2][1] != " H ":
        kentta1[1][1] = " H "
    elif kohta1 ==  "b3" and kentta1[2][0] != " H " and kentta1[2][2] != " H " and kentta1[1][1] != " H " and kentta1[3][1] != " H ":
        kentta1[2][1] = " H "
    elif kohta1 == "b4" and kentta1[3][0] != " H " and kentta1[3][2] != " H " and kentta1[2][1] != " H " and kentta1[4][1] != " H ":
        kentta1[3][1] = " H "
    elif kohta1 == "b5" and kentta1[4][0] != " H " and kentta1[4][2] != " H " and kentta1[3][1] != " H ":
        kentta1[4][1] = " H "
    elif kohta1 == "c1" and kentta1[0][0] != " H " and kentta1[0][2] != " H " and kentta1[1][1] != " H ":
        kentta1[0][2] = " H "
    elif kohta1 == "c2" and kentta1[1][0] != " H " and kentta1[1][2] != " H " and kentta1[0][1] != " H " and kentta1[2][1] != " H ":
        kentta1[1][2] = " H "
    elif kohta1 == "c3" and kentta1[2][0] != " H " and kentta1[2][2] != " H " and kentta1[1][1] != " H " and kentta1[3][1] != " H ":
        kentta1[2][2] = " H "
    elif kohta1 == "c4" and kentta1[3][0] != " H " and kentta1[3][2] != " H " and kentta1[2][1] != " H " and kentta1[4][1] != " H ":
        kentta1[3][2] = " H "
    elif kohta1 == "c5" and kentta1[4][0] != " H " and kentta1[4][2] != " H " and kentta1[3][1] != " H ":
        kentta1[4][2] = " H "
    elif kohta1 == "d1" and kentta1[0][2] != " H " and kentta1[0][4] != " H " and kentta1[1][3] != " H ":
        kentta1[0][3] = " H "
    elif kohta1 == "d2" and kentta1[1][2] != " H " and kentta1[1][4] != " H " and kentta1[0][3] != " H " and kentta1[2][3] != " H ":
        kentta1[1][3] = " H "
    elif kohta1 == "d3" and kentta1[2][2] != " H " and kentta1[2][4] != " H " and kentta1[1][3] != " H " and kentta1[3][3] != " H ":
        kentta1[2][3] = " H "
    elif kohta1 == "d4" and kentta1[3][2] != " H " and kentta1[3][4] != " H " and kentta1[2][3] != " H " and kentta1[4][3] != " H ":
        kentta1[3][3] = " H "
    elif kohta1 == "d5" and kentta1[4][2] != " H " and kentta1[4][4] != " H " and kentta1[3][3] != " H ":
        kentta1[4][3] = " H "
    elif kohta1 == "e1" and kentta1[0][0] != " H " and kentta1[0][2] != " H " and kentta1[1][4] != " H ":
        kentta1[0][4] = " H "
    elif kohta1 == "e2" and kentta1[1][3] != " H " and kentta1[0][4] != " H " and kentta1[2][4] != " H ":
        kentta1[1][4] = " H "
    elif kohta1 ==  "e3" and kentta1[2][3] != " H " and kentta1[1][4] != " H " and kentta1[3][4] != " H ":
        kentta1[2][4] = " H "
    elif kohta1 == "e4" and kentta1[3][3] != " H " and kentta1[2][4] != " H " and kentta1[4][4] != " H ":
        kentta1[3][4] = " H "
    elif kohta1 == "e5" and kentta1[4][0] != " H " and kentta1[3][4] != " H ":
        kentta1[4][4] = " H "
        if kohta2 == "a1" and (kentta1[1][0] == " H " or kentta1[0][1] == " H "):
            kentta1[0][0] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "a2" and (kentta1[0][0] == " H " or kentta1[1][1] == " H " or kentta1[2][0] == " H "):
            kentta1[1][0] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "a3" and (kentta1[1][0] == " H " or kentta1[2][1] == " H " or kentta1[3][0] == " H "):
            kentta1[2][0] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "a4" and (kentta1[2][0] == " H " or kentta1[3][1] == " H " or kentta1[4][0] == " H "):
            kentta1[3][0] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "a5" and (kentta1[3][0] == " H " or kentta1[4][1] == " H "):
            kentta1[4][0] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "b1" and (a1 == " H " or kentta1[0][2] == " H " or kentta1[1][1] == " H "):
            kentta1[0][1] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 ==  "b2"and (kentta1[1][0] == " H " or kentta1[1][2] == " H " or kentta1[0][1] == " H " or kentta1[2][1] == " H "):
            kentta1[1][1] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 ==  "b3"and (kentta1[2][0] == " H " or kentta1[2][2] == " H " or kentta1[1][1] == " H " or kentta1[3][1] == " H "):
            kentta1[2][1] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "b4" and (kentta1[3][0] == " H " or kentta1[3][2] == " H " or kentta1[2][1] == " H " or kentta1[4][1] == " H "):
            kentta1[3][1] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "b5" and (kentta1[4][0] == " H " or kentta1[4][2] == " H " or kentta1[3][1] == " H "):
            kentta1[4][1] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "c1" and (kentta1[0][0] == " H " or kentta1[0][2] == " H " or kentta1[1][1] == " H "):
            kentta1[0][2] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "c2" and (kentta1[1][0] == " H " or kentta1[1][2] == " H " or kentta1[0][1] == " H " or kentta1[2][1] == " H "):
            kentta1[1][2] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "c3" and (kentta1[2][0] == " H " or kentta1[2][2] == " H " or kentta1[1][1] == " H " or kentta1[3][1] == " H "):
            kentta1[2][2] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "c4" and (kentta1[3][0] == " H " or kentta1[3][2] == " H " or kentta1[2][1] == " H " or kentta1[4][1] == " H "):
            kentta1[3][2] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "c5" and (kentta1[4][0] == " H " or kentta1[4][2] == " H " or kentta1[3][1] == " H "):
            kentta1[4][2] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "d1" and (kentta1[0][2] == " H " or kentta1[0][4] == " H " or kentta1[1][3] == " H "):
            kentta1[0][3] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "d2" and (kentta1[1][2] == " H " or kentta1[1][4] == " H " or kentta1[0][3] == " H " or kentta1[2][3] == " H "):
            kentta1[1][3] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "d3" and (kentta1[2][2] == " H " or kentta1[2][4] == " H " or kentta1[1][3] == " H " or kentta1[3][3] == " H "):
            kentta1[2][3] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "d4" and (kentta1[3][2] == " H " or kentta1[3][4] == " H " or kentta1[2][3] == " H " or kentta1[4][3] == " H "):
            kentta1[3][3] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "d5" and (kentta1[4][2] == " H " or kentta1[4][4] == " H " or kentta1[3][3] == " H "):
            kentta1[4][3] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "e1" and (kentta1[0][0] == " H " or kentta1[0][2] == " H " or kentta1[1][4] == " H "):
            kentta1[0][4] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "e2" and (kentta1[1][3] == " H " or kentta1[0][4] == " H " or kentta1[2][4] == " H "):
            kentta1[1][4] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 ==  "e3"and (kentta1[2][3] == " H " or kentta1[1][4] == " H " or kentta1[3][4] == " H "):
            kentta1[2][4] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "e4" and (kentta1[3][3] == " H " or kentta1[2][4] == " H " or kentta1[4][4] == " H "):
            kentta1[3][4] = " H "
            print(kentta1)
            return print("Onnistui")
        elif kohta2 == "e5" and (kentta1[4][0] == " H " or kentta1[3][4] == " H "):
            kentta1[4][4] = " H "
            print(kentta1[4][4])
            return print("Onnistui")
    
# def position_solver(pos):
#     if pos == "a1":
#          " H "
#         return "Bing bong"
#     elif pos == "kentta1[1][0]":
#         kentta1[1][0] = " H "
#         return "Bing bong"
#     elif pos == "a3":
#         a3 = " H "
#         return "Bing bong"
#     elif pos == "a4":
#         a4 = " H "
#         return "Bing bong"
#     elif pos == "a5":
#         a5 = " H "
#         return "Bing bong"
#     elif pos == "b1":
#         b1 = " H "
#         return "Bing bong"
#     elif pos == "b2":
#         a1 == " H "
#         return "Bing bong"
#     elif pos == "b3":
#         return b3 = " H "
#     elif pos == "b4":
#         return b4 = " H "
#     elif pos == "b5":
#         return b5 = " H "
#     elif pos == "c1":
#         return c1 = " H "
#     elif pos == "c2":
#         return c2 = " H "
#     elif pos == "c3":
#         return c3 = " H "
#     elif pos == "c4":
#         return c4 = " H "
#     elif pos == "c5":
#         return c5 = " H "
#     elif pos == "d1":
#         return d1 = " H "
#     elif pos == "d2":
#         return d2 = " H "
#     elif pos == "d3":
#         return d3 = " H "
#     elif pos == "d4":
#         return d4 = " H "
#     elif pos == "d5":
#         return d5 = " H "
#     elif pos == "e1":
#         return e1 = " H "
#     elif pos == "e2":
#         return e2 = " H "
#     elif pos == "e3":
#         return e3 = " H "
#     elif pos == "e4":
#         return e4 = " H "
#     elif pos == "e5":
#         return e5 = " H "
# def position_figurer(position):
#     if (position == str):
#         product = str.replace(position, "1",[0]); product = str.replace(position, "2",[1]); product = str.replace(position, "3",[2]); product = str.replace(position, "4",[3]); product = str.replace(position, "5",[4]); product2 = str.replace(position, "a",[0]); product2 = str.replace(position, "b",[1]); product2 = str.replace(position, "c",[2]); product2 = str.replace(position, "d",[3]); product2 = str.replace(position, "e",[4])
#         print(product)
import array
print("LAIVANUPOTUS")
print("x  a   b   c   d   e")
print("1",kentta1[0][0],kentta1[0][1],kentta1[0][2],kentta1[0][3],kentta1[0][4])
print("2",kentta1[1][0],kentta1[1][1],kentta1[1][2],kentta1[1][3],kentta1[1][4])
print("3",kentta1[2][0],kentta1[2][1],kentta1[2][2],kentta1[2][3],kentta1[2][4])
print("4",kentta1[3][0],kentta1[3][1],kentta1[3][2],kentta1[3][3],kentta1[3][4])
print("5",kentta1[4][0],kentta1[4][1],kentta1[4][2],kentta1[4][3],kentta1[4][4])
print("Kolme laivaa, yksi kolmen pituinen, yksi kahden pituinen ja yksi, mihin ne laitetaan?")
print("Aloitetaan kolmen pituisella. Valitse kolme paikkaa toistensa vierillä ja muista pitää laiva suorana.")
print("Laivan paikkoja päättäessäsi muista aloittaa numerolla ja kirjoita perään kirjain.")
print("Ensimmäinen(esim e3):")
pelaaja1_3laiva_1 = input()
print("Toinen(esim e3):")
pelaaja1_3laiva_2 = input()
position_solver2(pelaaja1_3laiva_1,pelaaja1_3laiva_2)
#print("Toinen Laiva, muista laivanupotuksen säännöt")
#def valmistelu2(laivat2):
kentta2 = [[a1,b1,c1,d1,e1],[kentta1[1][0],b2,c2,d2,e2],[a3,b3,c3,d3,e3],[a4,b4,c4,d4,e4],[a5,b5,c5,d5,e5]]
print(kentta1[0][0],kentta1[0][1],kentta1[0][2],kentta1[0][3],kentta1[0][4])
print(kentta1[1][0],kentta1[1][1],kentta1[1][2],kentta1[1][3],kentta1[1][4])
print(kentta1[2][0],kentta1[2][1],kentta1[2][2],kentta1[2][3],kentta1[2][4])
print(kentta1[3][0],kentta1[3][1],kentta1[3][2],kentta1[3][3],kentta1[3][4])
print(kentta1[4][0],kentta1[4][1],kentta1[4][2],kentta1[4][3],kentta1[4][4])

