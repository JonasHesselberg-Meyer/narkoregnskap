import re
import sqlite3
class Sykepleier:
    def __init__(self):
        self.logg_dict={    "medid":1,
                        "brukerinputtext": "test fyll database",
                        "innskudd": 0,
                        "uttak":0,
                        "kassert":0,
                        "signatur": "test12",
                        "beholdning":69}
        
        self.legemiddel_dict={  "medid":None,
                                "AB": "",
                                "fulltnavn": "",
                                "Beholdning":0
                                }
        



    def sjekk_pin(self,signatur,pin):
        conn= sqlite3.connect("regnskap_AB.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM Brukerinfo WHERE signatur='{signatur}'")
        if c.fetchone()[1] == pin:
            print("godkjent")
            return True
        else:
            print("feil pin")
            return False
        
    def registrer_logg(self,logg_dict):
    
        conn= sqlite3.connect("regnskap_AB.db")
        c = conn.cursor()
        c.execute("""INSERT INTO Logg_regnskap(
            MedID,
            Dato_Tid,
            Brukerinputtext,
            Mengde_mottat,
            Mengde_uttak, 
            Kassert, 
            Signatur,
            Beholdning) 
            VALUES(?, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)""", 
            (logg_dict["medid"], logg_dict["brukerinputtext"] ,logg_dict["innskudd"], logg_dict["uttak"], logg_dict["kassert"], logg_dict["signatur"],logg_dict["beholdning"] ))
        conn.commit()
        conn.close()

    def liste_alle_legemiddler(self):
        conn= sqlite3.connect("regnskap_AB.db")
        c = conn.cursor()
        c.execute(f"SELECT MedID, fulltnavn FROM legemiddel ")
        liste = c.fetchall()
    
        return liste        
    
    def hent_legemiddel(self,medid):
        conn= sqlite3.connect("regnskap_AB.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM Legemiddel WHERE MedID ='{medid}'")
        aktuelt_legemiddel = c.fetchone()
        return aktuelt_legemiddel
    
    def sjekk_beholdning(self,medid):
        conn= sqlite3.connect("regnskap_AB.db")
        c = conn.cursor()
        c.execute(f"SELECT Beholdning FROM Legemiddel WHERE MedID ='{medid}'")
        aktuel_beholdning = c.fetchone()[0]
    
        return aktuel_beholdning
    
    def ta_ut_legemiddel(self,medid,uttak):
        conn= sqlite3.connect("regnskap_AB.db")
        c = conn.cursor()
        
        c.execute(f"SELECT Beholdning FROM Legemiddel WHERE MedID ='{medid}'")
        antall = c.fetchone()[0]
   
        nytt_antall = antall - uttak
    
        c.execute(f"UPDATE Legemiddel SET Beholdning={nytt_antall} WHERE MedID={medid}")
        
        conn.commit()
        conn.close()



    def legg_til_legemiddel(self,medid,uttak):
        conn= sqlite3.connect("regnskap_AB.db")
        c = conn.cursor()
        c.execute(f"SELECT Beholdning FROM Legemiddel WHERE MedID ='{medid}'")
        antall = c.fetchone()[0]
        nytt_antall = antall + uttak  
        c.execute(f"UPDATE Legemiddel SET Beholdning={nytt_antall} WHERE MedID={medid}")
        conn.commit()
        conn.close()
        return nytt_antall  


    def vis_regnskap_x_linjer(self,x,medid):
        conn= sqlite3.connect("regnskap_AB.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM Logg_regnskap WHERE MedID = {medid} ORDER BY Dato_Tid DESC")
        Xlinjer_logg = c.fetchmany(x)

        

        conn.commit()
        conn.close()
        return Xlinjer_logg

    def nytt_legemiddel(self,ab,fulltnavn,beholdning):
        
        conn= sqlite3.connect("regnskap_AB.db")
        c = conn.cursor()
        c.execute(f"SELECT MedID FROM Legemiddel")
        alle_medid = c.fetchall()
        ny_medid=(len(alle_medid))+1
        self.legemiddel_dict["medid"]=ny_medid
        self.legemiddel_dict["AB"]=ab
        self.legemiddel_dict["fulltnavn"]=fulltnavn
        self.legemiddel_dict["Beholdning"]=beholdning
        print(self.legemiddel_dict)
        
        c.execute("""INSERT INTO Legemiddel(
            MedID,
            AB,
            fulltnavn,
            Beholdning) 
            VALUES( ?, ?, ?, ?)""", 
        (self.legemiddel_dict["medid"], self.legemiddel_dict["AB"] ,self.legemiddel_dict["fulltnavn"],self.legemiddel_dict["Beholdning"] ))
        conn.commit()
        conn.close() 
    
    

#print(sykepleier.nytt_legemiddel("B","ballemed",3))
#sykepleier.nytt_legemiddel()
#print(sykepleier.legemiddel_dict)
    
#sykepleier.nytt_legemiddel(sykepleier.legemiddel_dict)
#x=sykepleier.vis_regnskap_x_linjer(2,6)
#print(x)
#for i in range(50):
#    sykepleier.registrer_logg(sykepleier.logg_dict)

#sykepleier.sjekk_pin("johess","9999")        
        
        
        




#def main():
    
    
        

       
    
    


    #if __name__ =="__main__":
     #   main()
     
                
        



