#import betriebrechnungenkalk as bbk
import handelskalk as hk
#import betriebsabrechnungsbogen as bab
#import zuschlagskalkindustrie as zki

def main_menu():
    print("    __  __     __         ______    ")
    print("   /\ \/ /    /\ \       /\  == \   ")
    print('   \ \  _"-.  \ \ \____  \ \  __<   ') 
    print("    \ \_\ \_\  \ \_____\  \ \_\ \_\ ")
    print("     \/_/\/_/   \/_____/   \/_/ /_/ ")
    print("")
    print("")
    
    print("Kosten Leistung Rechner")
    print("Bitte wählen Sie ....")
    print(" 1 Handelskalkulation")
    #print(" 2 Zuschlagskalkulation Industrie")
    #print(" 3 Betriebsabrechnungsbogen")
    #print(" 4 Nachkalkulation")
    print(" q Beenden")

main_menu()

wahl = ""
menu = ("1", "2", "3", "4", "q")

while wahl != "q":
    for i in menu:
        print("")
        wahl = input("Ihre Wahl: ").lower()
        
        if wahl == "1":
            print("")
            print(" Handelskalkulation:")
            print("Bitte wählen Sie ....")
            print(" 1 Vorwärtskalkulation")
            print(" 2 Rückwärtskalkulation")
            print(" 3 Differenzkalkulation")
            print(" b Main Menu")
            
            sub_menu = ("1", "2", "3", "b")
            print("")
            wahl = input("Ihre Wahl: ").lower()
            for k in sub_menu:
                
                if wahl ==  "1":
                    print(hk.vorwaerts_kalk_table())
                    print("")
                    input("Weiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                
                elif wahl == "2":
                    print(hk.rueckwaerts_kalk_table())
                    print("")
                    input("Weiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                
                elif wahl == "3":
                    print(hk.differenz_kalk_table())
                    print("")
                    input("Weiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                
                
                elif wahl == "b":
                    main_menu()
                    break
                
                else:
                   print("Fehlerhafte Auswahl versuchen Sie bitte nochmal") 
        
        # elif wahl == "2":
        #     print("")
        #     print("Zuschlagskalkulation Industrie:")
        #     print("Bitte wählen Sie ....")
        #     print(" 1 Angebotspreis")
        #     print(" 2 Gemeinsamkostenzuschlagsaetze und Angebotspreis")
        #     print(" b Main Menu")
            
        #     sub_menu = ("1", "2", "b")
        #     print("")
        #     wahl = input("Ihre Wahl: ").lower()
        #     for k in sub_menu:
        #         if wahl ==  "1":
        #             print(bbk.betriebsrechnung_kalk_table())
        #             print("")
        #             input("Weiter mit der Eingabe-Taste")
        #             print("")
        #             main_menu()
        #             break
                
        #         elif wahl == "2":
        #             print(bbk.gemeinkostenzuschlagsaetze())
        #             print("")
        #             input("Weiter mit der Eingabe-Taste")
        #             print("")
        #             main_menu()
        #             break
                
        #         elif wahl == "b":
        #             main_menu()
        #             break
                
        #         else:
        #            print("Fehlerhafte Auswahl versuchen Sie bitte nochmal") 
                   
        # elif wahl == "3": 
        #     print("")
        #     print("Betriebsabrechnungsbogen:")
        #     print("Bitte wählen Sie ....")
        #     print(" 1 Betriebsabrechnungsbogen + Zuschlagssaetze")
        #     print(" 2 Betriebsabrechnungsbogen (Industrie)")
        #     print(" b Main Menu")
            
        #     sub_menu = ("1", "2", "b")
        #     print("")
        #     wahl = input("Ihre Wahl: ").lower()
        #     for k in sub_menu:
        #         if wahl == "1":
        #             print(bab.bab())
        #             print("")
        #             input("Weiter mit der Eingabe-Taste")
        #             print("")
        #             main_menu()
        #             break
                
        #         elif wahl == "2":
        #             print(bab.bab_industrie())
        #             input("Weiter mit der Eingabe-Taste")
        #             print("")
        #             main_menu()
        #             break
                
        #         elif wahl == "b":
        #             main_menu()
        #             break
                
        # elif wahl == "4":
        #     print("")
        #     print(zki.vor_nach_kalk_table()) 
        #     input("Weiter mit der Eingabe-Taste")
        #     print("")
        #     main_menu()
        #     break                  
        
        elif wahl == "q":
            exit()
            
        else:
            print("Fehlerhafte Auswahl versuchen Sie bitte nochmal")
            
                
            
            
            