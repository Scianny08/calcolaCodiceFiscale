import csv

consonanti = set("BCDFGHJKLMNPQRSTVWXYZ")
vocali = set("AEIOU")

def filtra_caratteri(s: set, stringa: str) -> list:
    lista = []
    for char in stringa:
        if char in s:
            lista.append(char)
            
    return lista


def parte_cognome(cognome):
    parte_cognome = ""
    cognome = cognome.upper().replace(" ", "")
    
    consonanti_cognome = filtra_caratteri(consonanti, cognome)
    vocali_cognome = filtra_caratteri(vocali, cognome)
    
    if len(cognome) == 3:
        parte_cognome += cognome
    elif len(cognome) > 3:
        consonanti_cognome.reverse()
        while consonanti_cognome and len(parte_cognome) < 3:
            parte_cognome += consonanti_cognome.pop()
        
        vocali_cognome.reverse()
        while vocali_cognome and len(parte_cognome) < 3:
            parte_cognome += vocali_cognome.pop()
    else:
        parte_cognome += cognome
        if len(cognome) == 1:
            parte_cognome += "XX"
        else:
            parte_cognome += "X"
            
    return parte_cognome


def parte_nome(nome):
    nome = nome.upper().replace(" ", "")
    parte_nome = ""
    
    consonanti_nome = filtra_caratteri(consonanti, nome)
    vocali_nome = filtra_caratteri(vocali, nome)
        
    if len(nome) == 3:
        parte_nome += nome
    elif len(nome) > 3:
        if len(consonanti_nome) >= 4:
            parte_nome = consonanti_nome[0] + consonanti_nome[2] + consonanti_nome[3]
        else:
            consonanti_nome.reverse()
            while consonanti_nome and len(parte_nome) < 3:
                parte_nome += consonanti_nome.pop()
            
            vocali_nome.reverse()
            while vocali_nome and len(parte_nome) < 3:
                parte_nome += vocali_nome.pop()
    else:
        parte_nome += nome
        if len(nome) == 1:
            parte_nome += "XX"
        else:
            parte_nome += "X"
            
    return parte_nome
            

def parte_anno(anno):
    return anno[2:4] #ultime 2 cifre
    
    
def parte_mese(mese):
    diz_mese = {
        "01": "A",
        "02": "B",
        "03": "C",
        "04": "D",
        "05": "E",
        "06": "H",
        "07": "L",
        "08": "M",
        "09": "P",
        "10": "R",
        "11": "S",
        "12": "T",
    }
    
    return diz_mese[mese]
    

def parte_giorno(giorno, sesso):
    return giorno if sesso == "M" else str(int(giorno)+40).zfill(2)
    

def parte_codicecatastale(comune):
    comune = comune.lower()
    
    with open("Elenco-comuni-italiani.csv", mode="r", encoding="utf-8") as elenco:
        righe = csv.reader(elenco)
    
        for riga in righe:
            if riga[0] == comune:
                return riga[1]
        
    return ""
    

def parte_caratterecontrollo(cf):
    valori_char_dispari = {
        "0": 1, "A": 1,
        "1": 0, "B": 0,
        "2": 5, "C": 5,
        "3": 7, "D": 7,
        "4": 9, "E": 9,
        "5": 13, "F": 13,
        "6": 15, "G": 15,
        "7": 17, "H": 17,
        "8": 19, "I": 19,
        "9": 21, "J": 21,
        "K": 2,
        "L": 4,
        "M": 18,
        "N": 20,
        "O": 11,
        "P": 3,
        "Q": 6,
        "R": 8,
        "S": 12,
        "T": 14,
        "U": 16,
        "V": 10,
        "W": 22,
        "X": 25,
        "Y": 24,
        "Z": 23
    }
    
    valori_char_pari = {
        "0": 0, "A": 0,
        "1": 1, "B": 1,
        "2": 2, "C": 2,
        "3": 3, "D": 3,
        "4": 4, "E": 4,
        "5": 5, "F": 5,
        "6": 6, "G": 6,
        "7": 7, "H": 7,
        "8": 8, "I": 8,
        "9": 9, "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25
    }
    
    somma = 0
    for i in range(len(cf)):
        if i % 2 == 0:
            somma += valori_char_dispari[cf[i]]
        else:
            somma += valori_char_pari[cf[i]]
    
    resto = somma % 26
    
    char_controllo = chr(resto+65)
    return char_controllo


def calcola_cf(nome, cognome, giorno, mese, anno, comune, sesso):
    cf = parte_cognome(cognome) + parte_nome(nome) + parte_anno(anno) + parte_mese(mese) + parte_giorno(giorno, sesso) + parte_codicecatastale(comune)
    cf += parte_caratterecontrollo(cf)
    return cf


print(calcola_cf("Mario", "Rossi", "01", "04", "1998", "Agliè", "M"))