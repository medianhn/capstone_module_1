A = True
B = False

print(A and not(B))

x = int(input("Masukkan umur anda: "))
if (x >= 17):
    print("Email pendaftaran akan dikirim!")
else:
    print("Mohon maaf, pendaftaran anda kami tolak!")

nilai_siswa = float(input("Masukkan nilai siswa: "))
if (100 >= nilai_siswa >= 90):
    print("Grade siswa adalah A" )
elif (90 > nilai_siswa >= 80):
    print("Grade siswa adalah B")
elif (80 > nilai_siswa >= 70):
    print("Grade siswa adalah C")
elif (70 > nilai_siswa >= 60):
    print("Grade siswa adalah D")
elif ((nilai_siswa > 100) or (nilai_siswa < 0)):
    print("Nilai tidak valid")
else:
    print("Grade siswa adalah F")

theText = "Halo teman-teman semua, senang berkenalan dengan teman-teman semua!"

countTemanAll = theText.count("teman")
print(countTemanAll)
print(len(theText))
print(len(theText)//2)
countTemanHalf = theText.count("teman",0,len(theText)//2)
print(countTemanHalf)

theText = "purwadhika@gmail.com"
check1 = theText.endswith('.com')
check2 = theText.endswith('gmail')
check3 = theText.endswith('gmail',0,-4)
print(check1) # True
print(check2) # False
print(theText[14:-1]) # purwadhika@gmail
print(check3) # True

idStudent1 = "JCDS-001"
idStudent2 = "JCDS001"
idStudent = input("Masukkan ID Student Purwadhika: ")

if(idStudent.isalnum() == False):
    print("Input ID Salah! Masukkan ID yang valid (A-Z & 0-9)")
else:
    print("Input ID Benar!")

text1 = "   All the other kids with the pumped up kicks"
text2 = "       \t\n@)"
print(text2.isspace())

textBaru = "Saya ingin membeli komputer rusak di pasar, di mana komputer ini akan saya perbaiki dan menjadi komputer bermain dan komputer belajar"

textGanti = textBaru.replace("komputer", "laptop", 6)
print(textGanti)

