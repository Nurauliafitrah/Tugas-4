print("Ayo Bikin Dengan Cara Yang Mudah")
#Konversi Desimal menjadi Biner, Oktal, Hexadesimal mengambil masukan pengguna dan 
#Select Input [1] for Binary [2] for Octal [3] for Hexadecimal


desimal = int(input("Masukkan Nilai Desimal: \n"))
convert = int(input("Konversi into: [1] Biner, [2] Oktal [3] Hexadecimal: \n"))

#if...elif ... else.... function
if convert == 1:
    print ("Converted to Binary \n", bin(desimal))
elif convert == 2:
    print ("Converted to Octal \n", oct(desimal))
elif convert == 3:
    print ("Converted to Hexadecimal \n", hex(desimal))
else: 
    print ("Please Review your Input")

