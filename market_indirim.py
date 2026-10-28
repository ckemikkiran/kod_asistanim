peynir = float(input("kaç kg peynir aldınız:"))
peynir_fiyat = float(input("peynirin kg fiyatı   :"))

zeytin = float(input("kaç kg zeytin aldınız:"))
zeytin_fiyat = float(input("zeytinin kg fiyatı   :"))

pekmez = float(input("kaç kg pekmez aldınız:"))
pekmez_fiyat = float(input("pekmezin kg fiyatı   :"))

toplam_tutar = (peynir * peynir_fiyat) + (zeytin * zeytin_fiyat) + (pekmez * pekmez_fiyat)
indirimli_tutar = toplam_tutar - (toplam_tutar * 10 / 100)

print(f"toplam tutar        = {toplam_tutar:.2f}")
print(f"%10 indirimli tutar = {indirimli_tutar:.2f}")

