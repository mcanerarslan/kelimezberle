import random
import colorama
from colorama import Fore, Style

# Renk modülü başlat
colorama.init()

# ─────────────────────────────
# ▸ Soru-Cevap Veritabanı
# ─────────────────────────────
quiz_data = {
    "Teizm": "Tanrıcılık",
    "Deizm": "Yaratancılık",
    "Hümanizm": "İnsancıllık",
    "Metaryalizm": "Maddecilik",
    "İdealizm": "Fikircilik",
    "Monizm": "Bircilik",
    "Relativizm": "Görecelilik"
}

if not quiz_data:
    print(Fore.RED + "❌ Veri seti boş!" + Style.RESET_ALL)
    exit()

# ─────────────────────────────
# ▸ Giriş Ekranı
# ─────────────────────────────
print(Fore.CYAN + "\n===============================")
print(Fore.MAGENTA + "         SORU / CEVAP         ")
print(Fore.CYAN + "===============================\n" + Style.RESET_ALL)
print(Fore.YELLOW + "Çıkmak için 'q' yazabilirsin.\n" + Style.RESET_ALL)

# ─────────────────────────────
# ▸ Skor Bilgileri
# ─────────────────────────────
score_true = 0
score_false = 0

# ─────────────────────────────
# ▸ Ana Döngü
# ─────────────────────────────
while quiz_data:
    kelime, cevap = random.choice(list(quiz_data.items()))
    print(Fore.MAGENTA + "[🧠 Soru]  ", end="")
    print(Fore.YELLOW + kelime + Style.RESET_ALL)

    input_ = input(Fore.BLUE + "✏️  Cevabın: " + Style.RESET_ALL).strip()

    if input_.lower() == "q":
        print(Fore.CYAN + "\n⏹️  Quiz sonlandırıldı.\n" + Style.RESET_ALL)
        break

    if input_.lower() == cevap.lower():
        print(Fore.GREEN + "✔ Doğru!" + Style.RESET_ALL)
        score_true += 1
    else:
        print(Fore.RED + f"✖ Yanlış! Doğru cevap: {cevap}" + Style.RESET_ALL)
        score_false += 1

    del quiz_data[kelime]

    print(Fore.LIGHTBLACK_EX + "──────────────────────────────\n" + Style.RESET_ALL)

# ─────────────────────────────
# ▸ Quiz Sonu
# ─────────────────────────────
print(Fore.CYAN + "🎉 Quiz Tamamlandı!" + Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX + f"✅ Doğru: {score_true}" + Style.RESET_ALL)
print(Fore.LIGHTRED_EX + f"❌ Yanlış: {score_false}" + Style.RESET_ALL)
print(Fore.CYAN + "\n🔚 Program sonlandı." + Style.RESET_ALL)
