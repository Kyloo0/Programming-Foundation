print(""">>====================================<<
||                                    ||
||  Welcome to Dek Depe's Calculator  ||
||                                    ||
>>====================================<<
""")

# Input Data
nama = input('Nama : ')
tanggal_lahir = input('Tanggal lahir : ')
jurusan = input('Jurusan : ')
kelompok_mentoring = input('Kelompok Mentoring: ')
motto = input('Motto : ')
masukkan_alas = input('Masukkan alas : ')
masukkan_tinggi = input('Masukkan tinggi : ')

# Cara menghitung luas
alas = int(masukkan_alas)
tinggi = int(masukkan_tinggi)
luas = int(alas*tinggi/2)

# Cara menghitung sisi miring dan keliling
import math as m
sisi_miring = float(m.sqrt(alas**2 + tinggi**2))
keliling = m.ceil(float(alas + tinggi + sisi_miring))



print ("Hallo " + nama + " dari jurusan " + jurusan + "." )
print (nama + " berasal dari kelompok mentoring" + kelompok_mentoring)
print (nama + " lahir pada " + tanggal_lahir + " dengan motto " + motto + ".")

print ("Luas dari segitiga yang dimiliki" + nama + " adalah " + str(luas) + " cm^2.")
print ("Keliling dari segitiga yang dimiliki " + nama + " adalah " + str(keliling) + " cm dengan sisi miring sepanjang " + str(sisi_miring) + ".")



print(""">>==========================================<<
||                                          ||
||  Thanks for using Dek Depe's Calculator  ||
||                                          ||
>>==========================================<<
""")

