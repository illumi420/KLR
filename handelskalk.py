import pandas as pd
from tabulate import tabulate
from openpyxl import *
import os
from datetime import datetime, time

os.chdir(os.getcwd())
path = os.getcwd()
now = datetime.now()
timestamp = now.strftime("%m%d%Y%H%M%S")
excelfilename = timestamp+".xlsx"

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
       
#Ausgaben

def vorwaerts_kalk_table():
    print(" ")
    
    
    print("Ausgaben: ")
    # stueck Anzahl/Preis Vorhanden
    stueck_anzahl = float(input("Stueck Anzahl: "))
    preis_je_stueck = float(input("Stueck Preis€: "))
    total_preis_stueck = stueck_anzahl * preis_je_stueck
    
    # LEP Listeneinkaufspreis Vorhanden
    if (stueck_anzahl == 0.0) or (preis_je_stueck == 0.0):
        total_preis_stueck = float(input("Listeneinkaufspreis€: "))
    
    kalkulation = [
                  {"Name": "{}LEP Listeneinkaufspreis{}".format(bcolors.OKGREEN, bcolors.ENDC),"€":float(total_preis_stueck), "%": "","berechnung":""}, 
                  {"Name": "-Rabatt","€":0.0, "%": float(input("-Rabatt%: ")),"berechnung":""},
                  {"Name": "ZEP Zieleinkaufpreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "-Skonto","€":0.0, "%": float(input("-Skonto%: ")),"berechnung":""},
                  {"Name": "BEP Bareinkaufspreis","€":0.0, "%":"","berechnung":""},
                  {"Name": "+BK Beschaffungskosten","€":float(input("+Beschaffungskosten€: ")), "%":"","berechnung":""},
                  {"Name": "BP/EP Bezugspreis/Einstandspreis","€":0.0, "%":"","berechnung":""},
                  {"Name": "+HKZ Handlungskosten","€":float(input("+Handlungskosten€: ")), "%":float(input("+Handlungskosten%: ")),"berechnung":""},
                  {"Name": "SK Selbstkosten","€":0.0, "%":"","berechnung":""},
                  {"Name": "+Gewinn","€":0.0, "%": float(input("+Gewinn%: ")),"berechnung":""},
                  {"Name": "BVP Barverkaufspreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "+Skonto (i.H.)","€":0.0, "%": float(input("+Skonto%: ")),"berechnung":""},
                  {"Name": "+Provision (i.H.)","€":0.0, "%": float(input("+Provision%: ")),"berechnung":""},
                  {"Name": "ZVP Zielverkaufspreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "+Rabatt","€":0.0, "%": float(input("+Rabatt%: ")),"berechnung":""},
                  {"Name": "LVP Netto-/Listen-verkaufspreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "+UST Umsatzsteuer","€":0.0, "%": float(input("+Umsatzsteuert%: ")),"berechnung":""},
                  {"Name": "{}BVP Bruttoverkaufspreis{}".format(bcolors.FAIL, bcolors.ENDC),"€":0.0, "%": "","berechnung":""},
                  ]
    df = pd.DataFrame(kalkulation, columns=['Name', '€', '%', 'berechnung'])
    
    #rechnungen
    
    # LEP Listeneinkaufspreis
    if (stueck_anzahl > 0.0) or (preis_je_stueck > 0.0):
        df.loc[0,'berechnung'] =  '{} stueck * {} €'.format(stueck_anzahl, preis_je_stueck )
        
    #Rabatt
    lep = round(float(df.loc[0,'€']),2)
    rabatt = float(df.loc[1,"€"])
    rabatt += (float(df.loc[1,"%"]) * lep) / 100
    df.loc[1,"€"] = round(rabatt,2)
    df.loc[1,"berechnung"] = '{} * {} / 100'.format(df.loc[1,"%"], df.loc[0,"€"] )
    # print()
    # print("-Rabatt =",df.loc[1,"€"],"€")
    
    # ZEP Zieleinkaufpreis
    zep = float(df.loc[2,'€'])
    zep += lep - rabatt
    df.loc[2,"€"] = round(zep,2)
    # print()
    # print("ZEP =",df.loc[2,"€"],"€")
    
    # SKONTO minus
    skonto = float(df.loc[3,'€'])
    skonto += (float(df.loc[3,"%"]) * zep) / 100
    df.loc[3,"€"] = round(skonto,2)
    df.loc[3,"berechnung"] = '{} * {} / 100'.format(df.loc[3,"%"], df.loc[2,"€"] )
    # print()
    # print("-Skonto =",df.loc[3,"€"],"€")
    
    # BEP Bareinkaufspreis
    bep = float(df.loc[4,'€'])
    bep += zep - skonto
    df.loc[4,"€"] = round(bep,2)
    # print()
    # print("BEP =",df.loc[4,"€"],"€")
    
    # BP/EP Bezugspreis/Einstandspreis
    bk = float(df.loc[5,'€'])
    bp_ep = float(df.loc[6,'€'])
    bp_ep += bep + bk
    df.loc[6,'€'] = round(bp_ep,2)
    # print()
    # print("BP/EP =",df.loc[6,"€"],"€")
    
    # SK Selbstkosten
    if float(df.loc[7,'€']) != 0.0:
        hkz = float(df.loc[7,'€'])
        df.loc[7,'%'] = round((100 * float(df.loc[7,'€'])) / bp_ep,2)
        sk = float(df.loc[8,'€'])
        sk += bp_ep + hkz
        df.loc[8,'€'] = round(sk,2)
        
    elif float(df.loc[7,'€']) == 0.0:
        hkz = float(df.loc[7,'€'])
        hkz = (float(df.loc[7,'%']) * bp_ep) / 100
        df.loc[7,'€'] = round(hkz, 2) 
        df.loc[7,"berechnung"] = '{} * {} / 100'.format(df.loc[7,"%"], df.loc[6,"€"] )
        sk = float(df.loc[8,'€'])
        sk += bp_ep + float(df.loc[7,'€'])
        df.loc[8,'€'] = round(sk,2)
        print()
        #print("HKZ€ =",float(df.loc[7,'€'])),"€"
           
    
    # Gewinn
    gewinn = (float(df.loc[9,'%']) * sk) / 100
    df.loc[9,'€'] += round(gewinn,2) 
    df.loc[9,"berechnung"] = '{} * {} / 100'.format(df.loc[9,"%"], df.loc[8,"€"] )
    # print()
    # print("Gewinn =",df.loc[9,"€"],"€")
    
    # BVP Barverkaufspreis
    bvp = float(df.loc[9,'€']) + sk
    df.loc[10,'€'] = round(bvp,2)    
    # print()
    # print("BVP =",df.loc[10,"€"],"€")   
    
    # (i.H)
    im_hundert = 100
    
     # SKONTO und Provision
    im_hundert -= (float(df.loc[11,'%']) + float(df.loc[12,'%']))
    
    kundenskonto = float(df.loc[11,'€'])
    kundenskonto += (float(df.loc[11,"%"]) * bvp) / im_hundert
    df.loc[11,"€"] = round(kundenskonto,2)
    df.loc[11,"berechnung"] = '{} * {} / {}'.format(df.loc[11,"%"], df.loc[10,"€"], im_hundert )
    # print()
    # print("kundenskonto =",df.loc[11,"€"],"€") 
    
    provision = float(df.loc[12,'€'])
    provision += (float(df.loc[12,"%"]) * bvp) / im_hundert
    df.loc[12,"€"] = round(provision,2)
    df.loc[12,"berechnung"] = '{} * {} / {}'.format(df.loc[12,"%"], df.loc[10,"€"], im_hundert )
    # print()
    # print("provision =",df.loc[12,"€"],"€") 
    
    # Reset
    im_hundert = 100
    
    
    #ZVP Zielverkaufspreis
    zvp = float(df.loc[13,'€']) + float(df.loc[11,'€']) + float(df.loc[12,'€']) + float(df.loc[10,'€'])
    df.loc[13,'€'] = round(zvp,2)
    # print()
    # print("ZVP =",df.loc[13,"€"],"€") 
    
    # Rabatt
    im_hundert -= float(df.loc[14,"%"])
    kundenrabatt = float(df.loc[14,'€'])
    kundenrabatt += (float(df.loc[14,"%"]) * zvp) / im_hundert
    df.loc[14,"€"] = round(kundenrabatt,2)
    df.loc[14,"berechnung"] = '{} * {} / {}'.format(df.loc[14,"%"], df.loc[13,"€"], im_hundert )
    # print()
    # print("kundensrabatt =",df.loc[14,"€"],"€")
    
    
    
    # LVP Netto-/Listen-verkaufspreis
    lvp = float(df.loc[15,'€']) + float(df.loc[13,'€']) + float(df.loc[14,'€'])
    df.loc[15,'€'] =  round(lvp,2)
    # print()
    # print("LVP =",df.loc[15,"€"],"€")
    
    # Reset
    im_hundert = 100
    
    # UST Umsatzsteuer
    #im_hundert -= float(df.loc[16,"%"])
    ust = float(df.loc[16,'€'])
    ust += (float(df.loc[16,"%"]) * lvp) / im_hundert
    df.loc[16,"€"] = round(ust,2)
    if ust > 0:
        df.loc[16,"berechnung"] = '{} * {} / {}'.format(df.loc[16,"%"], df.loc[15,"€"], im_hundert )
        
    
    # BVP Bruttoverkaufspreis
    bvp = float(df.loc[17,'€']) + float(df.loc[15,'€']) + float(df.loc[16,"€"])
    df.loc[17,'€'] = round(bvp,2)
    if (stueck_anzahl > 0.0) or (preis_je_stueck > 0.0):
        bvp_je_stueck = bvp / stueck_anzahl
        df.loc[17,'berechnung'] =  '{} € / {} stueck = {} €/stueck '.format(round(bvp,2), stueck_anzahl, round(bvp_je_stueck,2))
        
   
    print("")  
    excel = input("Möchten Sie eine Excel-Tabelle für die Berechnung erstellen ? (y/n) ").lower()
    if excel == "y": 
    
        writer = pd.ExcelWriter("Vorwaertskalk"+excelfilename, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='sheet1', index = False)
        writer.save()
        print("Datei ist gespeichert in: {}".format(path))
        print("") 
    
    print("{}[Vorwaerts]{}".format(bcolors.WARNING, bcolors.ENDC))
    
    return  tabulate(df, showindex=False, headers=df.columns)
    

def rueckwaerts_kalk_table():
    print("Ausgaben: ")
    
     # stueck Anzahl/Preis Vorhanden
    stueck_anzahl = float(input("Stueck Anzahl: "))
    preis_je_stueck = float(input("Stueck Preis€: "))
    total_preis_stueck = stueck_anzahl * preis_je_stueck
    
    # LVP Listeneinkaufspreis Vorhanden
    if (stueck_anzahl == 0.0) or (preis_je_stueck == 0.0):
        total_preis_stueck = float(input("Listenverkaufspreis€: "))
    
    kalkulation = [
                  {"Name": "{}BVP Bruttoverkaufspreis{}".format(bcolors.OKGREEN, bcolors.ENDC),"€":total_preis_stueck, "%": "","berechnung":""},
                  {"Name": "+UST Umsatzsteuer","€":0.0, "%": float(input("+Umsatzsteuert%: ")),"berechnung":""},
                  {"Name": "LVP Netto-/Listen-verkaufspreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "+Rabatt","€":0.0, "%": float(input("+Rabatt%: ")),"berechnung":""},
                  {"Name": "ZVP Zielverkaufspreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "+Skonto (i.H.)","€":0.0, "%": float(input("+Skonto%: ")),"berechnung":""},
                  {"Name": "+Provision (i.H.)","€":0.0, "%": float(input("+Provision%: ")),"berechnung":""},
                  {"Name": "BVP Barverkaufspreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "+Gewinn","€":0.0, "%": float(input("+Gewinn%: ")),"berechnung":""},
                  {"Name": "SK Selbstkosten","€":0.0, "%":"","berechnung":""},
                  {"Name": "+HKZ Handlungskosten","€":float(input("+Handlungskosten€: ")), "%":float(input("+Handlungskosten%: ")),"berechnung":""},
                  {"Name": "BP/EP Bezugspreis/Einstandspreis","€":0.0, "%":"","berechnung":""},
                  {"Name": "+BK Beschaffungskosten","€":float(input("+Beschaffungskosten€: ")), "%":"","berechnung":""},
                  {"Name": "BEP Bareinkaufspreis","€":0.0, "%":"","berechnung":""},
                  {"Name": "-Skonto","€":0.0, "%": float(input("-Skonto%: ")),"berechnung":""},
                  {"Name": "ZEP Zieleinkaufpreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "-Rabatt","€":0.0, "%": float(input("-Rabatt%: ")),"berechnung":""},
                  {"Name": "{}LEP Listeneinkaufspreis{}".format(bcolors.FAIL, bcolors.ENDC),"€":0.0, "%": "","berechnung":""}, 
                  ]
    df = pd.DataFrame(kalkulation, columns=['Name', '€', '%', 'berechnung'])
    
    #rechnungen
    
    # BVP Bruttoverkaufspreis
    if (stueck_anzahl > 0.0) or (preis_je_stueck > 0.0):
        df.loc[0,'berechnung'] =  '{} stueck * {} €'.format(stueck_anzahl, preis_je_stueck )
    bvp = df.loc[0,'€']
    df.loc[0,'€'] = round(bvp,2)
    
    # UST Umsatzsteuer
    ust = float(df.loc[1,'€'])
    ust += (float(df.loc[1,"%"]) * bvp) / (100 + (float(df.loc[1,"%"])))
    df.loc[1,"€"] = round(ust,2)
    if ust > 0:
        df.loc[1,"berechnung"] = '{} * {} / {}'.format(df.loc[1,"%"], df.loc[0,"€"], (100 + (float(df.loc[1,"%"]))) )
    
    # LVP Netto-/Listen-verkaufspreis
    lvp = float(df.loc[2,'€']) + (float(df.loc[0,'€']) - float(df.loc[1,'€']))
    df.loc[2,'€'] =  round(lvp,2)
    
    # Rabatt
    kundenrabatt = float(df.loc[3,'€'])
    kundenrabatt += (float(df.loc[3,"%"]) * lvp) / 100
    df.loc[3,"€"] = round(kundenrabatt,2)
    df.loc[3,"berechnung"] = '{} * {} / {}'.format(df.loc[3,"%"], df.loc[2,"€"], 100 )
    
    
    # ZVP Zielverkaufspreis
    zvp = float(df.loc[4,'€']) + (float(df.loc[2,'€']) - float(df.loc[3,'€']))
    df.loc[4,'€'] = round(zvp,2)
    
    
     # SKONTO und Provision
    
    kundenskonto = float(df.loc[5,'€'])
    kundenskonto += (float(df.loc[5,"%"]) * zvp) / 100
    df.loc[5,"€"] = round(kundenskonto,2)
    df.loc[5,"berechnung"] = '{} * {} / {}'.format(df.loc[5,"%"], df.loc[4,"€"], 100 )
    
    
    provision = float(df.loc[6,'€'])
    provision += (float(df.loc[6,"%"]) * zvp) / 100
    df.loc[6,"€"] = round(provision,2)
    df.loc[6,"berechnung"] = '{} * {} / {}'.format(df.loc[6,"%"], df.loc[4,"€"], 100 )
    
    
    # BVP Barverkaufspreis
    bvp = float(df.loc[7,'€']) + (float(df.loc[4,"€"]) - (float(df.loc[5,"€"]) + float(df.loc[6,"€"])))
    df.loc[7,'€'] = round(bvp,2)  
    
    
    # Gewinn
    im_hundert = 100
    gewinn = (float(df.loc[8,'%']) * bvp) / (im_hundert + (float(df.loc[8,'%'])))
    df.loc[8,'€'] += round(gewinn,2) 
    df.loc[8,"berechnung"] = '{} * {} / {}'.format(df.loc[8,"%"], df.loc[7,"€"],(im_hundert + (float(df.loc[8,'%'])))  )
    
    # SK Selbstkosten
    sk = float(df.loc[9,'€']) + (float(df.loc[7,'€']) - float(df.loc[8,'€']))
    df.loc[9,'€'] = round(sk,2)  
    
    # HKZ Handlungskostenzuschlag und BP/EP Bezugspreis/Einstandspreis
    if float(df.loc[10,'€']) == 0.0:
        hkz = (float(df.loc[10,'%']) * sk) / (im_hundert + (float(df.loc[10,'%'])))
        df.loc[10,'€'] += round(hkz,2)
        df.loc[10,"berechnung"] = '{} * {} / {}'.format(df.loc[10,"%"], df.loc[9,"€"],(im_hundert + (float(df.loc[10,'%'])))  )
        
        bp_ep = float(df.loc[11,'€']) + (float(df.loc[9,'€']) - float(df.loc[10,'€']))
        df.loc[11,'€'] = round(bp_ep,2)
        
    elif float(df.loc[10,'€']) != 0.0:
        df.loc[10,'%'] = round(((100 * float(df.loc[10,'€'])) / sk),2)
        bp_ep = float(df.loc[11,'€']) + (float(df.loc[9,'€']) - float(df.loc[10,'€']))
        df.loc[11,'€'] = round(bp_ep,2)
    
    # BEP Bareinkaufspreis
    bep = float(df.loc[13,'€']) + (float(df.loc[11,'€']) - float(df.loc[12,'€']))
    df.loc[13,"€"] = round(bep,2)
    
    # SKONTO
    skonto = float(df.loc[14,'€'])
    skonto += (float(df.loc[14,"%"]) * bep) / (im_hundert - float(df.loc[14,"%"]))
    df.loc[14,"€"] = round(skonto,2)
    df.loc[14,"berechnung"] = '{} * {} / {}'.format(df.loc[14,"%"], df.loc[13,"€"], (im_hundert - float(df.loc[14,"%"])))
    
    # ZEP Zieleinkaufpreis
    zep = float(df.loc[15,'€'])
    zep += bep + skonto
    df.loc[15,"€"] = round(zep,2)
    
    #Rabatt
    rabatt = float(df.loc[16,"€"])
    rabatt += (float(df.loc[16,"%"]) * zep) / (im_hundert - float(df.loc[16,"%"]))
    df.loc[16,"€"] = round(rabatt,2)
    
    if rabatt > 0:
        df.loc[16,"berechnung"] = '{} * {} / {}'.format(df.loc[16,"%"], df.loc[15,"€"], (im_hundert - float(df.loc[16,"%"])) )
    
    # LEP Listeneinkaufspreis
    lep = float(df.loc[17,'€']) + float(df.loc[15,"€"]) + float(df.loc[16,"€"])
    df.loc[17,'€'] = lep
    if (stueck_anzahl > 0.0) or (preis_je_stueck > 0.0):
        lep_je_stueck = lep / stueck_anzahl
        df.loc[17,'berechnung'] =  '{} € / {} stueck = {} €/stueck '.format(round(lep,2), stueck_anzahl, round(lep_je_stueck,2))
   
    
    print("")  
    excel = input("Möchten Sie eine Excel-Tabelle für die Berechnung erstellen ? (y/n) ").lower()
    if excel == "y": 
    
        writer = pd.ExcelWriter("Rueckwaertskalk"+excelfilename, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='sheet1', index = False)
        writer.save()
        print("Datei ist gespeichert in: {}".format(path))
        print("") 
       
    print("{}[Rueckwaerts]{}".format(bcolors.WARNING, bcolors.ENDC))
    return tabulate(df[::-1], showindex=False, headers=df.columns)
    
    
def differenz_kalk_table():
    print(" ")
    
    
    print("Ausgaben: ")
    stueck_anzahl = float(input("Stueck Anzahl: "))
    
    # stueck Anzahl/Preis Vorhanden
    lep_preis_je_stueck = float(input("LEP Stueck Preis€: "))
    lep_total_preis_stueck = stueck_anzahl * lep_preis_je_stueck
    
    # LEP Listeneinkaufspreis Vorhanden
    if (stueck_anzahl == 0.0) or (lep_preis_je_stueck == 0.0):
        lep_total_preis_stueck = float(input("Listeneinkaufspreis€: ")) 
        
    # stueck Anzahl/Preis Vorhanden
    lvp_preis_je_stueck = float(input("BVP Stueck Preis€: "))
    lvp_total_preis_stueck = stueck_anzahl * lvp_preis_je_stueck
    
    # BVP Listeneinkaufspreis Vorhanden
    if (stueck_anzahl == 0.0) or (lvp_preis_je_stueck == 0.0):
        lvp_total_preis_stueck = float(input("BVP Listenverkaufspreis€: ")) 
        
        
        
    kalkulation = [
                  {"Name": "{}LEP Listeneinkaufspreis{}".format(bcolors.OKGREEN, bcolors.ENDC),"€":lep_total_preis_stueck, "%": "","berechnung":""}, 
                  {"Name": "-Rabatt","€":0.0, "%": float(input("-Rabatt%: ")),"berechnung":""},
                  {"Name": "ZEP Zieleinkaufpreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "-Skonto","€":0.0, "%": float(input("-Skonto%: ")),"berechnung":""},
                  {"Name": "BEP Bareinkaufspreis","€":0.0, "%":"","berechnung":""},
                  {"Name": "+BK Beschaffungskosten","€":float(input("+Beschaffungskosten€: ")), "%":"","berechnung":""},
                  {"Name": "BP/EP Bezugspreis/Einstandspreis","€":0.0, "%":"","berechnung":""},
                  {"Name": "+HKZ Handlungskosten","€":float(input("+Handlungskosten€: ")), "%":float(input("+Handlungskosten%: ")),"berechnung":""},
                  {"Name": "SK Selbstkosten","€":0.0, "%":"","berechnung":""},
                  {"Name": "{}BVP Bruttoverkaufspreis{}".format(bcolors.OKGREEN, bcolors.ENDC),"€":lvp_total_preis_stueck, "%": "","berechnung":""},
                  {"Name": "+UST Umsatzsteuer","€":0.0, "%": float(input("+Umsatzsteuert%: ")),"berechnung":""},
                  {"Name": "LVP Netto-/Listen-verkaufspreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "+Rabatt","€":0.0, "%": float(input("+Rabatt%: ")),"berechnung":""},
                  {"Name": "ZVP Zielverkaufspreis","€":0.0, "%": "","berechnung":""},
                  {"Name": "+Skonto (i.H.)","€":0.0, "%": float(input("+Skonto%: ")),"berechnung":""},
                  {"Name": "+Provision (i.H.)","€":0.0, "%": float(input("+Provision%: ")),"berechnung":""},
                  {"Name": "BVP Barverkaufspreis","€":0.0, "%": "","berechnung":""}, 
                  {"Name": "{}+Gewinn{}".format(bcolors.FAIL, bcolors.ENDC),"€":0.0, "%":"","berechnung":""},        
                  
                  ]
    
    df = pd.DataFrame(kalkulation, columns=['Name', '€', '%', 'berechnung'])
    
    # berechnungen
    
    #rechnungen
    
    # LEP Listeneinkaufspreis
    if (stueck_anzahl > 0.0) or (lep_preis_je_stueck > 0.0):
        df.loc[0,'berechnung'] =  '{} stueck * {} €'.format(stueck_anzahl, lep_preis_je_stueck )
        
    #Rabatt
    lep = round(float(df.loc[0,'€']),2)
    rabatt = float(df.loc[1,"€"])
    rabatt += (float(df.loc[1,"%"]) * lep) / 100
    df.loc[1,"€"] = round(rabatt,2)
    df.loc[1,"berechnung"] = '{} * {} / 100'.format(df.loc[1,"%"], df.loc[0,"€"] )
    # print()
    # print("-Rabatt =",df.loc[1,"€"],"€")
    
    # ZEP Zieleinkaufpreis
    zep = float(df.loc[2,'€'])
    zep += lep - rabatt
    df.loc[2,"€"] = round(zep,2)
    # print()
    # print("ZEP =",df.loc[2,"€"],"€")
    
    # SKONTO minus
    skonto = float(df.loc[3,'€'])
    skonto += (float(df.loc[3,"%"]) * zep) / 100
    df.loc[3,"€"] = round(skonto,2)
    df.loc[3,"berechnung"] = '{} * {} / 100'.format(df.loc[3,"%"], df.loc[2,"€"] )
    # print()
    # print("-Skonto =",df.loc[3,"€"],"€")
    
    # BEP Bareinkaufspreis
    bep = float(df.loc[4,'€'])
    bep += zep - skonto
    df.loc[4,"€"] = round(bep,2)
    # print()
    # print("BEP =",df.loc[4,"€"],"€")
    
    # BP/EP Bezugspreis/Einstandspreis
    bk = float(df.loc[5,'€'])
    bp_ep = float(df.loc[6,'€'])
    bp_ep += bep + bk
    df.loc[6,'€'] = round(bp_ep,2)
    # print()
    # print("BP/EP =",df.loc[6,"€"],"€")
    
    # SK Selbstkosten
    if float(df.loc[7,'€']) != 0.0:
        hkz = float(df.loc[7,'€'])
        df.loc[7,'%'] = round((100 * float(df.loc[7,'€'])) / bp_ep,2)
        sk = float(df.loc[8,'€'])
        sk += bp_ep + hkz
        df.loc[8,'€'] = round(sk,2)
        
    elif float(df.loc[7,'€']) == 0.0:
        hkz = float(df.loc[7,'€'])
        hkz = (float(df.loc[7,'%']) * bp_ep) / 100
        df.loc[7,'€'] = round(hkz, 2) 
        df.loc[7,"berechnung"] = '{} * {} / 100'.format(df.loc[7,"%"], df.loc[6,"€"] )
        sk = float(df.loc[8,'€'])
        sk += bp_ep + float(df.loc[7,'€'])
        df.loc[8,'€'] = round(sk,2)
        
        
     # BVP Bruttoverkaufspreis
    if (stueck_anzahl > 0.0) or (lvp_preis_je_stueck > 0.0):
        df.loc[9,'berechnung'] =  '{} stueck * {} €'.format(stueck_anzahl, lvp_preis_je_stueck )
    bvp = df.loc[9,'€']
    df.loc[9,'€'] = round(bvp,2)
    
    # UST Umsatzsteuer
    ust = float(df.loc[10,'€'])
    ust += (float(df.loc[10,"%"]) * bvp) / (100 + (float(df.loc[10,"%"])))
    df.loc[10,"€"] = round(ust,2)
    if ust > 0:
        df.loc[10,"berechnung"] = '{} * {} / {}'.format(df.loc[10,"%"], df.loc[9,"€"], (100 + (float(df.loc[10,"%"]))) )
    
    # LVP Netto-/Listen-verkaufspreis
    lvp = float(df.loc[11,'€']) + (float(df.loc[9,'€']) - float(df.loc[10,'€']))
    df.loc[11,'€'] =  round(lvp,2)
    
    # Rabatt
    kundenrabatt = float(df.loc[12,'€'])
    kundenrabatt += (float(df.loc[12,"%"]) * lvp) / 100
    df.loc[12,"€"] = round(kundenrabatt,2)
    df.loc[12,"berechnung"] = '{} * {} / {}'.format(df.loc[12,"%"], df.loc[11,"€"], 100 )
    
    
    # ZVP Zielverkaufspreis
    zvp = float(df.loc[13,'€']) + (float(df.loc[11,'€']) - float(df.loc[12,'€']))
    df.loc[13,'€'] = round(zvp,2)
    
    
     # SKONTO und Provision
    
    kundenskonto = float(df.loc[14,'€'])
    kundenskonto += (float(df.loc[14,"%"]) * zvp) / 100
    df.loc[14,"€"] = round(kundenskonto,2)
    df.loc[14,"berechnung"] = '{} * {} / {}'.format(df.loc[14,"%"], df.loc[13,"€"], 100 )
    
    
    provision = float(df.loc[15,'€'])
    provision += (float(df.loc[15,"%"]) * zvp) / 100
    df.loc[15,"€"] = round(provision,2)
    df.loc[15,"berechnung"] = '{} * {} / {}'.format(df.loc[15,"%"], df.loc[13,"€"], 100 )
    
    
    # BVP Barverkaufspreis
    bvp = float(df.loc[16,'€']) + (float(df.loc[13,"€"]) - (float(df.loc[14,"€"]) + float(df.loc[15,"€"])))
    df.loc[16,'€'] = round(bvp,2)      
    
    # Gewinn 
    gewinn = float(df.loc[17,'€']) + (float(df.loc[16,'€']) - float(df.loc[8,'€']))
    df.loc[17,'€'] = round(gewinn,2)
    df.loc[17,'%'] = round(float(df.loc[17,'€']) * 100 / float(df.loc[8,'€']),2)
    df.loc[17,"berechnung"] = '{} * 100 / {}'.format(df.loc[17,'€'], df.loc[8,'€'])
    
    if stueck_anzahl > 0:
        df.loc[17,"berechnung"] = '{} * 100 / {}  Gewinn per Stueck = {} / {} = {}'.format(df.loc[17,'€'], df.loc[8,'€'], df.loc[17,'€'], stueck_anzahl, round((df.loc[17,'€']/stueck_anzahl),2) )
    
    
    df3 = pd.DataFrame(kalkulation, columns=['Name', '€', '%', 'berechnung'])
    df3 = df3.append(df[0:9])
    df3 = df3.append(df[9:18][::-1])
      
    
    
    print("")
    excel = input("Möchten Sie eine Excel-Tabelle für die Berechnung erstellen ? (y/n) ").lower()
    if excel == "y": 
    
        writer = pd.ExcelWriter("Differenz"+excelfilename, engine='xlsxwriter')
        df3[18:36].to_excel(writer, sheet_name='sheet1', index = False)
        writer.save()
        print("Datei ist gespeichert in: {}".format(path))
        print("") 
    
    print("{}[Differenz]{}".format(bcolors.WARNING, bcolors.ENDC))
    
    return tabulate(df3[18:36], showindex=False, headers=df.columns)

