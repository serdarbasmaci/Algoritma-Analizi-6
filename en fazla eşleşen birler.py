import itertools
import random

boyut = 10
baslik = []
for i in range(boyut):
    baslik.append("kolon" + str(i))

veri = []
for i in range(boyut):
    veri.append([])
    for j in range(boyut):
        veri[i].append(random.choice(['0', '1']))

for adet in range(1,boyut+1):
    komb=list(itertools.combinations(range(0,boyut), adet))
    maks=0
    for eleman in komb:
        curmaks=0
        for satir in veri:
            durum=1
            for indis in eleman:
                deger=satir[indis]
                if(deger=='0'):
                    durum=0
            if durum==1:
                curmaks=curmaks+1

        if(curmaks>maks):
            maks=curmaks
            indisler=eleman


    urun=""
    for i in indisler:
        urun=urun+baslik[i].replace('\n','')

    print("------- %s karsilastirma ------"%adet)
    if(maks==0):
        print ("%s adet urun icin maks bulunamadi"%adet)
    else:
        print ("%s urunleri %s kere satildi"%(urun,maks))
    print("")
