# def salam():
#     print('Hello selamat datang di Purwadhika!')
#     print('Semoga harimu menyenangkan!')
    # return 1

# salam()
# print(salam())

# def salamBalik(nama, usia):
#     print(f'Halo kak {nama}, anda saat ini berumur {usia} tahun ya?')

# nama = input('Masukkan nama anda: ')
# usia = int(input('Masukkan umur anda: '))
# salamBalik(nama, usia)

# def salamBalik(nama, usia):
#     print(f'Halo kak {nama}, anda saat ini berumur {usia} tahun ya?')

# salamBalik(usia=25, nama='Budi')

# def salamBalik(nama = '', usia = 0):
#     if(nama == '' and usia > 0):
#         print('Saya berusia {}'.format(usia))
#     elif(nama != '' and usia == 0):
#         print('Hello nama saya {}'.format(nama))
#     elif(nama != '' and usia > 0):
#         print(f'Hello perkenalkan nama saya {nama}, dan usia saya {usia}')
#     else:
#         print('Hello')
    
#     print('Senang bertemu dengan anda')

# nama = input('Masukkan nama anda: ')
# usia = int(input('Masukkan umur anda: '))

# salamBalik(nama, usia)
# def salamBalik(usia, nama = 'Unknown'):
#     if(nama != 'Unknown'):
#         print('Hello nama saya {} dan saya berumur {} tahun'.format(nama, usia))
#     else:
#         print('Hello, saya berumur {} tahun'.format(usia))
    
#     print('Senang bertemu dengan anda')

# salamBalik(25, 'daneik')

# def pangkat(angka1, angka2):
#     return angka1 ** angka2

# angka1 = float(input("Angka 1: "))
# angka2 = float(input("Angka 2: "))

# print(pangkat(angka1, angka2))

# import time

# def tambah(num1, num2):
#     return num1 + num2

# def kurang(num1, num2):
#     return num1 - num2

# def kali(num1, num2):
#     return num1*num2

# def bagi(num1, num2):
#     return num1/num2

# def hasilHitung(functionName, angka1, angka2):
#     if(functionName == "tambah"):
#         print(f"{angka1} + {angka2} = {tambah(angka1, angka2)}")
#     elif(functionName == "kurang"):
#         print(f"{angka1} - {angka2} = {kurang(angka1, angka2)}")
#     elif(functionName == "kali"):
#         print(f"{angka1} X {angka2} = {kali(angka1, angka2)}")
#     elif(functionName == "bagi"):
#         print(f"{angka1} : {angka2} = {bagi(angka1, angka2)}")
#     else:
#         print("error")

# angka1 = int(input("Masukkan angka pertama: "))
# time.sleep(2)
# angka2 = int(input("Masukkan angka kedua: "))
# time.sleep(2)
# operator = input("Masukkan operasi matematika yang ingin dijalankan (tambah, kurang, kali, bagi): ")
# time.sleep(2)
# hasilHitung(operator,angka1,angka2)

# lisstUsia = [18,23,17,8,2,99,77,54]

# hasilMapUsia = list(map(lambda usia : True if usia >= 18 else False, lisstUsia))

# print(hasilMapUsia)

# hasilFilterUsiaMengemudi = list(filter(lambda usia : True if usia >= 18 else False, lisstUsia))

# print(hasilFilterUsiaMengemudi)

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