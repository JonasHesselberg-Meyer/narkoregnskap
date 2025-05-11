import customtkinter as ctk
from signatur_gui import Signaturvindu
from sykepleier import Sykepleier

spl= Sykepleier()
class Nytt_legemiddelvindu(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Nytt legemiddelvindu")
        self.geometry("600x200")
        self.grab_set()

        self.info_label = ctk.CTkLabel(self, text="^Legg til et nytt preparat i regnskapet.", font=("Arial", 14), corner_radius=5)
        self.info_label.pack(pady=10, padx=20)

        self.frame= ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=20)

        # Opprett tekstfelt
        self.entry1 = ctk.CTkEntry(self.frame, placeholder_text="Legemiddelnavn og styrke")
        self.entry1.pack(side="left",pady=10, padx=20)

        self.ab_var = ctk.StringVar(self,value="B")
        ab=["A","B"]
        # Opprett nedtrekksmeny
        self.preparat_menu = ctk.CTkOptionMenu(self.frame, values=ab, variable=self.ab_var, width=100)
        self.preparat_menu.pack(side="left",pady=10, padx=20)
        
        #self.entry2 = ctk.CTkEntry(self, placeholder_text="A/B")
        #self.entry2.pack(pady=10, padx=20)

        self.entry3 = ctk.CTkEntry(self.frame, placeholder_text="Beholdning:")
        self.entry3.pack(side="left",pady=10, padx=20)

        # Opprett knapp
        self.button = ctk.CTkButton(self, text="Vis verdier", command=self.on_button_click)
        self.button.pack(pady=20)

    # Funksjon som kjører når knappen trykkes
    def on_button_click(self):
        self.navn = self.entry1.get().lower()
        if not self.navn:
            self.info_label.configure(fg_color="red",text="Legemiddelet må ha et navn." ) 
            return        
        self.ab = self.ab_var.get()
        self.beholdning = self.entry3.get()
        try:
            self.beholdning=int(self.beholdning)
        except:
            ValueError, self.info_label.configure(fg_color="red",text="Verdien i feltet:Beholdning må være et tall." ) 
            return


        signaturvindu = Signaturvindu(self)
        self.wait_window(signaturvindu)
        if signaturvindu.result:

            spl.nytt_legemiddel(self.ab, self.navn, self.beholdning)
            

            spl.logg_dict["medid"]=spl.legemiddel_dict["medid"]
            spl.logg_dict["innskudd"]=self.beholdning
            spl.logg_dict["beholdning"]=self.beholdning
            spl.logg_dict["signatur"]=signaturvindu.sign
            spl.logg_dict["brukerinputtext"]=self.navn
            spl.registrer_logg(spl.logg_dict)
            

            
            
            self.destroy()
        


