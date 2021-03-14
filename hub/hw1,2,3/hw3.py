more= True
while more == True:
 Ad =str(input('isim giriniz: '))
 Ara_sınav =int(input('Ara sınav notu : '))
 Proje_notu=int(input('Proje notu : '))
 Final_notu=int(input('Final notu : '))
 Geçme_notu=(int(Ara_sınav)*(0.3))+(int(Proje_notu)*(0.3))+(int(Final_notu)*(0.4))
 print("Geçme notu :{0} ".format(Geçme_notu))
 if(Geçme_notu<50):
      print("Kaldınız")
 elif(75>Geçme_notu>=50):
      print("notunuz cc")
 elif(85>Geçme_notu>=75):
      print("notunuz BB")
 else:
      print("AA ile Geçtiniz")
 print(Geçme_notu)
 a = input("Devam edecek misiniz? evet/hayır ")
if a!="evet":
       more=False
