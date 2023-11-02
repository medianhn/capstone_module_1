# 1) Mencari kata dalam string

spam = 'ababaababbbbcccbabcc'
word = 'bab'

a = len(spam)
b = len(word)
count = 0

for i in range(a-b+1):
    if spam[i:i+b] == word:
        count +=1

print(f"appeard {count} times")

# 2) Jumlah o dan x (peka huruf besar-kecil/case sensitive)

spam = "ooxx"

panjang_o, panjang_O = 0, 0
panjang_x, panjang,X = 0, 0

for i in spam:
    if i == "o":
        panjang_o += 1
    elif i == "x":
        panjang_x += 1
    elif i == "O":
        panjang_O += 1
    elif i == "X":
        panjang_X += 1
    else:
    	"Error, bukan itu yang diminta"

print(panjang_x == panjang_o and panjang_X == panjang_O)

# 3) Bilangan narsistik

import math
spam=input("Masukkan angka: ")
digitTotal=len(spam)
count=0

for i in range(digitTotal):
    count=count+pow(int(spam[i]),digitTotal)

if count==int(spam):
    print(spam, "is a narcissistic number")
else:
    print(spam, "not a narcissistic number")

# contoh solusi alternatif

angka = int(input("Masukkan sebuah angka: "))
angkaStr = str(angka)
n = len(angkaStr)
totalPangkat = sum(int(digit) ** n for digit in angkaStr) # Generator Expression

if totalPangkat == angka:
    print(f"(4) {angka} adalah bilangan narsistik.")
else:
    print(f"(4) {angka} bukan bilangan narsistik.")

# 4) Bilangan prima

number = int(input("number = "))

for i in range(2, int(number ** 0.5) + 1):
    if number == 2:
        pass
    elif (number % i == 0):
        print(f"{number} bukan merupakan bilangan prima")
        break
else:
    print(f"{number} merupakan bilangan prima")

# alternatif solusi/algoritma

number = int(input("masukkan input angka = "))
count = 0
for i in range(1,number+1):
    if number == 2:
        print("bilangan prima")
        break
    if number % i == 0:
        count += 1
    elif number % i == 1:
        count += 0

if count == 2:
    print("bilangan prima")

if count > 2:
    print("bukan bilangan prima")

# 5) Inisial Nama depan & belakang

name = "Median Hardiv Nugraha"

result = ""
for i in range(len(name)):
    if i == 0:
        result += name[i]
    if name[i] == " ":
        result += name[i + 1]

print(result[0].title() + "." + result[-1].title())

# alternatif tanpa for loop

nama = input("Masukkan nama: ")

splitnama = nama.split(" ")

print(splitnama[0][0].title(),".",splitnama[-1][0].title())

# 6) Faktorial

number = int(input('Masukkan angka: '))
hasil = 1
for i in range(1, number + 1):
    hasil = hasil * int(i)
print(f'{number}! = {hasil}')

# alternatif algoritma menggunakan while loop

value=int(input("Masukkan angka: "))
i=1
faktorial=1

while i<=value:
    faktorial*=i
    i+=1

print("Faktorial dari", value, "adalah", faktorial)

# 7) Toko buah

hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

stockApel = 5
stockJeruk = 7
stockAnggur = 6

while(True) :
    jumlahApel = int(input('Masukkan Jumlah Apel : '))
    if(jumlahApel > stockApel) :
        print('Jumlah yang dimasukkan terlalu banyak \nStock Apel tinggal : ' + str(stockApel))
    else :
        break
while(True) :
    jumlahJeruk = int(input('Masukkan Jumlah Jeruk : '))
    if(jumlahJeruk > stockJeruk) :
        print('Jumlah yang dimasukkan terlalu banyak \nStock Jeruk tinggal : ' + str(stockJeruk))
    else :
        break
while(True) :
    jumlahAnggur = int(input('Masukkan Jumlah Anggur : '))
    if(jumlahAnggur > stockAnggur) :
        print('Jumlah yang dimasukkan terlalu banyak \nStock Anggur tinggal : ' + str(stockAnggur))
    else :
        break

totalHargaApel = jumlahApel * hargaApel
totalHargaJeruk = jumlahJeruk * hargaJeruk
totalHargaAnggur = jumlahAnggur * hargaAnggur
totalHarga = totalHargaAnggur+totalHargaApel+totalHargaJeruk

print('''
    Detail Belanja

    Apel : {jmlApel} x {hrgApel} = {totalHrgApel}
    Jeruk : {jmlJeruk} x {hrgJeruk} = {totalHrgJeruk}
    Anggur : {jmlAnggur} x {hrgAnggur} = {totalHrgAnggur}

    Total : {totalHarga}
    '''.format(jmlApel=jumlahApel, hrgApel=hargaApel, totalHrgApel=totalHargaApel, 
        jmlJeruk=jumlahJeruk, hrgJeruk=hargaJeruk, totalHrgJeruk=totalHargaJeruk,
        jmlAnggur=jumlahAnggur, hrgAnggur=hargaAnggur, totalHrgAnggur=totalHargaAnggur,
        totalHarga=totalHarga))

while(True) :
    jmlUang = int(input('Masukkan jumlah uang : '))

    if(jmlUang > totalHarga) :
        kembali = jmlUang - totalHarga
        print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
        break
    elif(jmlUang == totalHarga) :
        print('Terima kasih')
        break
    else :
        kekurangan = totalHarga - jmlUang
        print('Uang anda kurang sebesar {}'.format(kekurangan))

# 8) Cek alphanum, alphabet, digit, lower sama upper

characters = "qA2"

boolAlnum = False
for char in characters.split():
	if(char.isalnum):
		boolAlnum = True
		break
	
boolAlpha = False
for char in characters.split():
	if(char.isalpha):
		boolAlpha = True
		break

boolDigit = False
for char in characters.split():
	if(char.isdigit):
		boolDigit = True
		break
	
boolUpper = False
for char in characters.split():
	if(char.isupper):
		boolUpper = True
		break
	
boolLower = False
for char in characters.split():
	if(char.islower):
		boolLower = True
		break
	
print(boolAlnum)
print(boolAlpha)
print(boolDigit)
print(boolUpper)
print(boolLower)

