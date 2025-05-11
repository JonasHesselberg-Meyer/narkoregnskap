import sqlite3

#conn= sqlite3.connect("regnskap_AB.db")

#c = conn.cursor()

#c.execute("PRAGMA foreign_keys = ON;")

#c.execute("CREATE TABLE Logg_regnskap (MedID INT, Dato_Tid DATETIME, Brukerinputtext varchar(50), Mengde_mottat INT, Mengde_uttak INT, Kassert INT, Signatur varchar(10),FOREIGN KEY (MedID) REFERENCES Legemiddler(MedID))")

#c.execute("INSERT INTO Brukerinfo2 (pin, Tid, tid2) VALUES('9999',CURRENT_TIMESTAMP ,CURRENT_TIMESTAMP )")

#c.execute("ALTER TABLE Logg_regnskap ADD COLUMN Beholdning INTEGER CHECK (Beholdning >= 0);")
#c.execute("SELECT * FROM Logg_regnskap WHERE MedID = 1 ORDER BY Dato_Tid DESC")
#c.execute(f"SELECT * FROM Logg_regnskap WHERE MedID =1")
#antall = c.fetchmany(10)

#for logg in antall:
#    print(logg)


#conn.commit()

#conn.close()