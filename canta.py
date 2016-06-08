from itertools import combinations

canta_max = 10

yukler = [
	{'agirlik': 2, 'fiyat': 1},
	{'agirlik': 8, 'fiyat': 5},
	{'agirlik': 1, 'fiyat': 3},
	{'agirlik': 5, 'fiyat': 1},
	{'agirlik': 2, 'fiyat': 3},
	{'agirlik': 2, 'fiyat': 2},
]

secilen_fiyat = 0
secilen_elemanlar = []

for i in range(1, len(yukler)):
	for kombinasyon in combinations(yukler, i):
		fiyat_toplami = 0
		agirlik_toplami = 0
		for e in kombinasyon:
			fiyat_toplami += e['fiyat']
			agirlik_toplami += e['agirlik']

		if agirlik_toplami > canta_max:
			continue

		if fiyat_toplami > secilen_fiyat:
			secilen_fiyat = fiyat_toplami
			secilen_elemanlar = kombinasyon[:]

print secilen_fiyat
print secilen_elemanlar