# i = 0
# while i < 5:
#     i+=1
#     print(i)

# i = 1
# while i < 6:
#     print(i)
#     i = i+1 # ekivalen dengan i+=1

# outputAngka = ''
# for i in range(1,10,2):
        # outputAngka = outputAngka + str(i) +','

# print(outputAngka)

# outputAngka = ''
# inputUserMaksimum = 10
# angkaYangDiSkip = [5,7]
# for i in range(1, inputUserMaksimum, 2):
#     if(i == angkaYangDiSkip):
#         continue
#     else:
#         outputAngka = outputAngka + str(i)

# print(outputAngka)

# stars = ''
# size = 5
# for i in range(size):
#     stars += '* '
#     for j in range(size):
#          stars += '\n'

# print(stars)



# namaString = 'pemanen buah'
# verbatin = 'pemanen'
# panjangVer = len(verbatin)

# print(namaString[:panjangVer])
# count = 0
# for x in namaString:
#     count = count + 1

# print(count)

# jumlahApel = 8
# inputUserApel = 0

# while(True):
#     inputUserApel = int(input("Masukkan jumlah apel: "))
#     if(inputUserApel < jumlahApel):
#         print('Jumlah stok apel kurang, hanya ada {}'.format(jumlahApel))
#         continue
#     else:
#         break

# print('Jumlah apel yang anda beli adalah: {}'.format(inputUserApel))

a = "Halo nama saya Randy"
b = [i.capitalize() for i in a.split()]

print(b)