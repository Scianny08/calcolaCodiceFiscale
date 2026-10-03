from pyscript import document
import codice_fiscale

def get_valore_radio(elementi):
    for radio in elementi:
        if radio.checked:
            return radio.value

def elabora_dati(event):
    nome = document.getElementById("nome").value
    cognome = document.getElementById("cognome").value
    comune = document.getElementById("comune").value
    sesso = get_valore_radio(document.getElementsByName("sesso"))
    data = document.getElementById("dataNascita").value
    
    anno, mese, giorno = data.split("-")
    
    cf = codice_fiscale.calcola_cf(nome, cognome, giorno, mese, anno, comune, sesso)
    document.getElementById("codice-fiscale").value = cf

    