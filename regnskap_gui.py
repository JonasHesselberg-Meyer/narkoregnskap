import customtkinter as ctk
from signatur_gui import Signaturvindu
from sykepleier import Sykepleier
from nytt_legemiddelvindu import Nytt_legemiddelvindu
import sqlite3



class Regnskapgui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Regnskap for A- og B-preparater")
        self.geometry("1200x500")
        
        # Tittel
        self.title_label = ctk.CTkLabel(self, text="Regnskap for A- og B-preparater", font=("Arial", 18))
        self.title_label.grid(row=1, column=2, pady=20)

        # Preparater fra SQLite-databasen
        self.preparater = []
        for navn in spl.liste_alle_legemiddler():
            self.preparater.append(navn[1])
        
        
        
        self.preparat_var = ctk.StringVar(self,value="Velg legemiddel her:")
        
        # Opprett nedtrekksmeny
        self.preparat_menu = ctk.CTkOptionMenu(self, values=self.preparater, variable=self.preparat_var, width=300, command=self.vis_preparat_info)
        self.preparat_menu.grid(row=2, column=2, padx=10,pady=10)
        

        # Label for å vise valgt preparat
        self.result_label = ctk.CTkLabel(self, text="Valgt preparat: ", font=("Arial", 18))
        self.result_label.place(x=400, y=25)

        # Label for å vise valgt preparat
        self.info_label = ctk.CTkLabel(self, text="^Velg preparat fra nedtrekksmenyen over^", font=("Arial", 14), corner_radius=5)
        self.info_label.grid(row=4, column=2,  padx=10,pady=3)

         # ta imot tekst fra bruker
        self.entry2 = ctk.CTkEntry(self, width= 300, height= 35, placeholder_text="Info: f.eks 'Ola Normann','Fra apotek'",font=("Arial", 14))
        self.entry2.grid(row=5, column=2,  padx=10,pady=10)

        #self.text_box = ctk.CTkTextbox(self, width=550, height=300, fg_color="blue",font=("Arial", 14))
        #self.text_box.place(x=400, y=100)
        #for row in spl.vis_regnskap_x_linjer(10):
        #    self.text_box.insert("end", f"{row[1][:-2]}   {row[2]} {row[3]}  {row[4]}    {row[5]}    {row[6]} "+"\n")
        #self.text_box.configure(state="disabled")  # Make textbox read-only

        self.sframe = ctk.CTkScrollableFrame(self, width=750, height=300)
        self.sframe.place(x=400, y=100)

        def vis_loggen(self):
            header=["medid","Dato/tid","brukerinputtext","innskudd","uttak","kassert","signatur","beholdning"]
            y=1
            for box in header:
                
                if box == header[2] or box == header[1]:
                    self.info_label3 = ctk.CTkLabel(self.sframe, width=150, text=box, font=("Arial", 14),fg_color="blue", corner_radius=5).grid(row=1, column=y,  padx=3,pady=3)
                else:
                    self.info_label3 = ctk.CTkLabel(self.sframe, width=50, text=box, font=("Arial", 14),fg_color="blue", corner_radius=5).grid(row=1, column=y,  padx=3,pady=3)
                y= y+1
                
            x=2
            y=1
            for row in spl.vis_regnskap_x_linjer(50):
                
                for item in row:
                    if y==2 or y==3:
                        self.info_label3 = ctk.CTkLabel(self.sframe, width=150,wraplength=150, text=item, font=("Arial", 14),fg_color="blue", corner_radius=5).grid(row=x, column=y,  padx=3,pady=3)
                    else:
                        self.info_label3 = ctk.CTkLabel(self.sframe, width=50,wraplength=50, text=item, font=("Arial", 14),fg_color="blue", corner_radius=5).grid(row=x, column=y,  padx=3,pady=3)
                    
                    y= y+1
                x= 1+ x
                y=1

            x=1
            y=1
            #self.info_label = ctk.CTkLabel(self.sframe, text=f"{row[1][:-2]}   {row[2]} {row[3]}  {row[4]}    {row[5]}    {row[6]} ", font=("Arial", 14), corner_radius=5).pack()
                #self.segbutton= ctk.CTkSegmentedButton(self.sframe, values=(row)).pack()
            

            
        


        self.entry1 = ctk.CTkEntry(self, width= 125, height= 35, placeholder_text="Antall legemiddel:",font=("Arial", 14))
        self.entry1.grid(row=6, column=2,  padx=10,pady=10)

        # Ramme for knapper
        self.button_frame1 = ctk.CTkFrame(self)
        self.button_frame1.grid(row=7, column=2, padx=10,pady=10)

        # Ramme for knapper
        self.button_frame2 = ctk.CTkFrame(self)
        self.button_frame2.grid(row=8, column=2,  padx=10,pady=10)
        
        self.submit_button5 = ctk.CTkButton(self, text="Testknapp funksjoner", command=self.kontroll)
        self.submit_button5.grid(row=9, column=2,  padx=10,pady=10)

        self.submit_button1 = ctk.CTkButton(self.button_frame2, text="nytt LM(ikke ferdig)")
        self.submit_button1.pack(padx= 10,pady=10, side="left")

        self.submit_button4 = ctk.CTkButton(self.button_frame2, text="slett LM(ikke ferdig)")
        self.submit_button4.pack(padx= 10,pady=10, side="left")
        
        # knapp for å legge til legemiddel i regnskap
        self.submit_button2 = ctk.CTkButton(self.button_frame1, text="legg til legemiddel", command=self.legg_til)
        self.submit_button2.pack(padx= 10,pady=10, side="left")
        
        # knapp for å ta ut legemiddel i regnskap
        self.submit_button3 = ctk.CTkButton(self.button_frame1, text="ta ut legemiddel", command=self.ta_ut)
        self.submit_button3.pack(padx= 10,pady=10, side="left")

        
        
    def vis_loggen(self,medid):
            header=["MedID","Dato/tid","Brukerinputtext","Mottat","Tatt ut","kassert","Signatur","Beholdning"]
            y=1
            for box in header:
                
                if box == header[2] or box == header[1]:
                    self.info_label3 = ctk.CTkLabel(self.sframe, width=150, text=box, font=("Arial", 14),fg_color="blue", corner_radius=5).grid(row=1, column=y,  padx=3,pady=3)
                else:
                    self.info_label3 = ctk.CTkLabel(self.sframe, width=50, text=box, font=("Arial", 14),fg_color="blue", corner_radius=5).grid(row=1, column=y,  padx=3,pady=3)
                y= y+1
                
            x=2
            y=1
            for row in spl.vis_regnskap_x_linjer(20,medid):
                
                for item in row:
                    if y==2 or y==3:
                        self.info_label3 = ctk.CTkLabel(self.sframe, width=150,wraplength=150, text=item, font=("Arial", 14),fg_color="blue", corner_radius=5).grid(row=x, column=y,  padx=3,pady=3)
                    else:
                        self.info_label3 = ctk.CTkLabel(self.sframe, width=50,wraplength=50, text=item, font=("Arial",14),fg_color="blue", corner_radius=5).grid(row=x, column=y,  padx=3,pady=3)
                    
                    y= y+1
                x= 1+ x
                y=1

            x=1
            y=1      

    def legg_til(self):
        self.innskudd = self.entry1.get()
        self.menyvalget = self.preparat_var.get()  # Hent valgt preparat
        if self.menyvalget:
            try:
                uttak=int(self.innskudd)
            except:
                ValueError, self.info_label.configure(fg_color="red", text="Verdien i feltet må være et tall.") 
                return
            signaturvindu = Signaturvindu(self)
            self.wait_window(signaturvindu)
            try:
                if signaturvindu.result:
                    
                    for legemiddel in spl.liste_alle_legemiddler():
                        if legemiddel[1] == self.menyvalget:
                            
                            legemiddelID= legemiddel[0]
                            spl.legg_til_legemiddel(legemiddelID,int(self.innskudd))
                            self.beholdning=spl.sjekk_beholdning(legemiddel[0])
                            self.info_label.configure(fg_color="green",text=f"{signaturvindu.sign} la til {self.innskudd} {legemiddel[1]} i regnskapet.")
                            self.result_label.configure(text=f"Valgt preparat: {self.menyvalget}  Beholdning: {self.beholdning}")
                            self.entry1.delete(0, "end")
                            spl.logg_dict["signatur"]=signaturvindu.sign
                            spl.logg_dict["medid"]=legemiddelID
                            spl.logg_dict["uttak"]= 0
                            spl.logg_dict["kassert"]= 0
                            spl.logg_dict["innskudd"]=self.innskudd
                            spl.logg_dict["brukerinputtext"]=self.entry2.get()
                            spl.logg_dict["beholdning"]=self.beholdning
                            spl.registrer_logg(spl.logg_dict)
                            self.vis_loggen(legemiddelID)
                
                else:
                    self.info_label.configure(fg_color="red",text="Ikkg gyldig signatur." )             
            except:
                AttributeError, self.info_label.configure(fg_color="red", text="Signer regskapet med gyldig brukernavn og pin!")   
                return             
                      
                

        

    def ta_ut(self):
            self.uttak = self.entry1.get()
            self.menyvalget = self.preparat_var.get()  # Hent valgt preparat
            if self.menyvalget:
                try:
                    self.uttak=int(self.uttak)
                except:
                    ValueError, self.info_label.configure(fg_color="red",text="Verdien i feltet må være et tall." ) 
                    return 
                signaturvindu = Signaturvindu(self)
                self.wait_window(signaturvindu)
                try:
                    if signaturvindu.result:
                                
                                for legemiddel in spl.liste_alle_legemiddler():
                                    if legemiddel[1] == self.menyvalget:
                                        
                                        legemiddelID= legemiddel[0]
                                        
                                        self.beholdning=spl.sjekk_beholdning(legemiddel[0])
                                        if self.uttak>self.beholdning:
                                            self.info_label.configure(fg_color="red",text="uttak er større enn beholdning.")
                                            return
                                        spl.ta_ut_legemiddel(legemiddelID,int(self.uttak))
                                        self.beholdning=spl.sjekk_beholdning(legemiddel[0])

                                        self.info_label.configure(fg_color="green",text=f"{signaturvindu.sign} tok ut {self.uttak} {legemiddel[1]} fra regnskapet.")
                                        self.result_label.configure(text=f"Valgt preparat: {self.menyvalget}  Beholdning: {self.beholdning}")
                                        spl.logg_dict["signatur"]=signaturvindu.sign
                                        spl.logg_dict["medid"]=legemiddelID
                                        spl.logg_dict["innskudd"]= 0
                                        spl.logg_dict["kassert"]= 0
                                        spl.logg_dict["uttak"]=self.uttak
                                        spl.logg_dict["brukerinputtext"]=self.entry2.get()
                                        spl.logg_dict["beholdning"]=self.beholdning
                                        spl.registrer_logg(spl.logg_dict)
                                        self.vis_loggen(legemiddelID)
                                        self.entry1.delete(0, "end")
                                        
                                        
                    else:
                            self.info_label.configure(fg_color="red",text="Ikkg gyldig signatur." )        
                except:
                    AttributeError, self.info_label.configure(fg_color="red", text="Signer regskapet med gyldig brukernavn og pin222!")   
                    return
                    
                
    def kontroll(self):
        nyttvindu=Nytt_legemiddelvindu(self)
        self.wait_window(nyttvindu)
        
        spl.legemiddel_dict["AB"]=nyttvindu.ab
        spl.legemiddel_dict["fulltnavn"]=nyttvindu.navn
        spl.legemiddel_dict["Beholdning"]=nyttvindu.beholdning
        
        


    # Funksjon som vise legemiddel info når det trykkes på nedtrekksmenyen.
    def vis_preparat_info(self, valgtprep):
        
    
        for widget in self.sframe.winfo_children():
            widget.destroy()
            
        
        for legemiddel in spl.liste_alle_legemiddler():
            if legemiddel[1] == valgtprep:
                
                self.beholdning=spl.sjekk_beholdning(legemiddel[0])
                self.vis_loggen(legemiddel[0])
                self.result_label.configure(text=f"Valgt preparat: {valgtprep}  Beholdning: {self.beholdning}")
                
                

    

spl=Sykepleier()                

if __name__=="__main__":
    gui = Regnskapgui()
    gui.mainloop()
