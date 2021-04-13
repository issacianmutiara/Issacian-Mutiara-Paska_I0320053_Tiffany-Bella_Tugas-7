
#Fungsi Center

teks_1 = "Fave Hotel"
teks_2 = "Jalan Adi Sucipto No 60,Kerten, Surakarta"
a = teks_1.center(50,'=')

#Fungsi Upper()
f = a.upper()
b = teks_2.center(50)
print(f)
print(b)

#Fungsi Capitalize
name = 'issacian'
namex = 'mutiara'
namey = 'paska'
greeting = 'Anda'
greeting_2 = 'fave'
greeting_3 = 'hotel'
x = name.capitalize()
x1 = namex.capitalize()
x2 = namey.capitalize()
y = greeting.capitalize()
z = greeting_2.capitalize()
w = greeting_3.capitalize()
print("Selamat siang selamat datang ",x+ x1 + x2 )
print("Senang rasanya dapat berjumpa dengan", y)
print("Terimakasih atas kepercayaannya sehingga memilih",z + w)

#Fungsi Replace
q ='Berapa jumlah tamu perempuannya,Pak?'
n = q.replace('Pak', 'Bu')
print(n)

#Fungsi Count
teks ='Mbak Nana dan Mbak Dora'
c = (teks.count('Mbak'))
print('Oh baik ada', c,'orang')

closing = 'End'
close = closing.center(60, '*')
print(close)