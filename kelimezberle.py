import random
#renk kısmı başlangıç
import colorama 
from colorama import Fore, Back, Style
colorama.init()
#renk kısmı son

dct = {
    "Teizm": "Tanrıcılık",
    "Deizm": "Yaratancılık",
    "Hümanizm": "İnsancıllık",
    "Metaryalizm": "Maddecilik",
    "İdealizm": "Fikircilik",
    "Monizm": "Bircilik",
    "Relativizm": "Görecelilik"
    }

if not dct:
    exit()

print(Fore.LIGHTCYAN_EX+'\n================\t'+Fore.MAGENTA+'Soru/Cevap'+Fore.LIGHTCYAN_EX+'\t================')

while True:
    kelime, cevap = random.choice(list(dct.items()))
    print(Fore.MAGENTA+"\n[x]Soru:\t\t"+Fore.YELLOW+kelime+Style.RESET_ALL,end=Fore.BLUE+"\t\n[-]Cevabın:\t\t"+Style.RESET_ALL)
    input_ = input()
    if input_ == "q":
        break
    
    print("[+]Doğru Cevap:\t\t"+Fore.RED+cevap, end=Fore.RED+"\n\n================\n")
    del dct[kelime]
