netto = float(input("Tragen Sie ihren Netto Betrag ein"))
steuer = float(input("Tragen Sie den Steuersatz ein"))
steuersatz = 1 + steuer / 100


brutto = netto * steuersatz


print(brutto)