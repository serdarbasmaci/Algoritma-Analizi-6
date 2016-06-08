def direk_yazdir(sol, orta, sag):
    satir = ""
    for direk in [sol, orta, sag]:
        if direk['isim'] == 'sol':
            satir += "%20s" % str(direk['elemanlar'])
    for direk in [sol, orta, sag]:
        if direk['isim'] == 'orta':
             satir  += "%20s" % str(direk['elemanlar'])
    for direk in [sol, orta, sag]:
        if direk['isim'] == 'sag':
             satir += "%20s" % str(direk['elemanlar'])
    print satir

def hanoi(n, sol, orta, sag):
    if n > 0:
        hanoi(n - 1, sol, sag, orta)

        disk = sol['elemanlar'].pop()
        sag['elemanlar'].append(disk)

        direk_yazdir(sol, orta, sag)

        hanoi(n - 1, orta, sol, sag)
        
sol = {'isim': 'sol', 'elemanlar': [5,4,3,2,1]}
orta = {'isim': 'orta', 'elemanlar': []}
sag = {'isim': 'sag', 'elemanlar': []}
hanoi(len(sol['elemanlar']),sol,orta,sag)
