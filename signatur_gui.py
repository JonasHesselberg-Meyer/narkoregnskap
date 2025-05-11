import customtkinter as ctk

from sykepleier import Sykepleier
import re


sykepleier= Sykepleier()
class Signaturvindu(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Signer regnskap")
        self.geometry("400x400")
        self.grab_set()
        
        
        # Create a label
        self.label = ctk.CTkLabel(self, text="Signer regnskap:")
        self.label.pack(pady=20)

       

        self.entryframe1 = ctk.CTkFrame(self)
        self.entryframe1.pack(pady=5)
        
        self.label1 = ctk.CTkLabel(self.entryframe1, text="Signatur",corner_radius= 5)
        self.label1.pack(pady=5)

        self.entry1 = ctk.CTkEntry(self.entryframe1, width= 130, height= 35,placeholder_text="Signatur:" )
        self.entry1.pack(pady=5)
        
        
        self.entryframe2 = ctk.CTkFrame(self)
        self.entryframe2.pack(pady=5)

        self.label2 = ctk.CTkLabel(self.entryframe2, text="pin",corner_radius= 5)
        self.label2.pack(pady=5)
        
        self.entry2 = ctk.CTkEntry(self.entryframe2, width= 130, height= 35, placeholder_text="pin:",show="*" )
        self.entry2.pack(side="left",pady=5)
                   
        self.button1 = ctk.CTkButton(self, text="Signer",command=self.hentlogin)
        self.button1.pack(pady=20)
        self.bind("<Return>",self.trykk_enter)




    def hentlogin(self):
        pin= self.entry2.get()
        sign = self.entry1.get()
        try:
            init_krav = r"^[a-å]{6}$"
            pin_krav = r"^[0-9]{4}$"
            
            if not re.search(init_krav,sign, re.IGNORECASE):      
                
                self.destroy()
                return
                
            if not re.search(pin_krav,pin):  
                   
                self.destroy()
                return    

        
        
            if sykepleier.sjekk_pin(sign,pin):
                self.result = True
                self.sign = sign
                self.destroy()
                return True
                
            else:
                self.result= False
                self.destroy()
        except:
            TypeError, self.destroy()

    def trykk_enter(self,*args):
        self.button1.invoke()
            


        
        






# Run the application
#if __name__ == "__main__":
    #signaturvindu = Signaturvindu()
    #signaturvindu.mainloop()

