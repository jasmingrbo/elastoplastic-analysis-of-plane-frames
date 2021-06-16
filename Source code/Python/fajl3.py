# Autor: Jasmin Grbo# Autor: Jasmin Grbo

# #######################################
# ############ ULAZNI PODACI ############
# #######################################

import numpy as np

# ################################################
# ############ POČETAK UNOSA PODATAKA ############
# ################################################

# ###################################################
# bc - broj čvorova
# be - broj elemenata
# bcpe - broj čvorova po elementu
# bsskpc - broj stepeni slobode kretanja po čvoru
# bsskpe - broj stepeni slobode kretanja po elementu
# ###################################################

bc = 11
be = 10
bcpe = 2
bsskpc = 3
bsskpe = bcpe * bsskpc

# ###################################################
# kc - koordinate čvorova
# kc = np.array(([0, 0],   (X, Y) = (0, 0) -> čvor 0
#                [0, 4],   (X, Y) = (0, 4) -> čvor 1
#                [2, 4]))  (X, Y) = (2, 4) -> čvor 2
# ###################################################

kc = np.array(([0, 0],
               [0, 8],
               [6, 10.5],
               [12, 13],
               [12, 8],
               [12, 0],
               [18, 10.5],
               [24, 13],
               [30, 10.5],
               [36, 8],
               [36, 0],))

# ###################################################
# pe - povezanost elemenata
# pe = np.array(([0, 1],   Prvi i drugi čvor elementa 0
#                [1, 2]))  Prvi i drugi čvor elementa 1
# ###################################################

pe = np.array(([0, 1],
               [1, 2],
               [2, 3],
               [3, 4],
               [4, 5],
               [4, 6],
               [6, 7],
               [7, 8],
               [8, 9],
               [9, 10]))

# ###################################################
# kmipp - karakteristike materijala i poprečnog presjeka
# pe = np.array(([3e7, 24e-2, 72e-4],   (E, A, I) -> element 0
#                [3e7, 24e-2, 72e-4]))  (E, A, I) -> element 1
# ###################################################

kmipp = np.array(([2e8, 0.01, 0.001],
                  [2e8, 0.01, 0.001],
                  [2e8, 0.01, 0.001],
                  [2e8, 0.01, 0.001],
                  [2e8, 0.01, 0.001],
                  [2e8, 0.01, 0.001],
                  [2e8, 0.01, 0.001],
                  [2e8, 0.01, 0.001],
                  [2e8, 0.01, 0.001],
                  [2e8, 0.01, 0.001]))

# ###################################################
# pru - početni rubni uslovi
# 1 => slobodan stepen slobode kretanja
# 0 => spriječen stepen slobode kretanja
# X1, Y1, F1, X1, Y2, F2 -> redoslijed stepeni slobode
# F => ugao zaokreta
# pru = np.ones((be, bsskpe)) -> inicijalizacija jedinične matrice
# pru[0, [0, 1]] = [0, 0] -> nepokretni oslonac u čvoru 0
# pru[1, [3, 4, 5]] = [0, 0, 0] -> uklještenje u čvoru 2
# ###################################################

pru = np.ones((be, bsskpe))
pru[0, [0, 1, 2]] = [0, 0, 0]
pru[4, [3, 4, 5]] = [0, 0, 0]
pru[9, [3, 4, 5]] = [0, 0, 0]

# ###################################################
# zglob - zglobovi
# 1 => nema zgloba
# 0 => ima zglob
# ###################################################

zglob = np.array(([1, 1],
                  [1, 1],
                  [1, 1],
                  [1, 1],
                  [1, 1],
                  [1, 1],
                  [1, 1],
                  [1, 1],
                  [1, 1],
                  [1, 1]))

# ###################################################
# Brojanje stepeni slobode kretanja
# bssk - broj stepeni slobode kretanja
# ru - rubni uslovi
# ###################################################

bssk = 0
ru = np.zeros((be, bsskpe), dtype="int")

# ###################################################
# optnc - opterećenje na čvoru
# optne - opterećenje na elementu
# optnc = np.zeros((bce, bsskpe)) - inicijalizacija nulte matrice
# optnc[0, [3, 4]] = [50, -100] - opterećenje u čvoru 1
# Fx, Fy, M - redoslijed sila
# ###################################################

optnc = np.zeros((be, bsskpe))
optnc[0, [3]] = [10]
optnc[1, [0]] = [10]
optnc[1, [4]] = [-15]
optnc[2, [1]] = [-15]
optnc[5, [4]] = [-10]
optnc[6, [1]] = [-10]
optnc[7, [4]] = [-10]
optnc[8, [1]] = [-10]
optnc[8, [3]] = [5]
optnc[9, [0]] = [5]

# ###################################################
# pzd - pomjeranje za dijagram
# ###################################################

pzd = np.zeros((be, 6))
pzd[1, [3]] = 1


# ###################################################
# mp - moment plastičnosti
# mp = 1000 * np.ones((be, bcpe))
# ###################################################

mp = 48 * np.ones((be, 2))
mp[[5], [0, 1]] = [96, 96]
mp[[6], [0, 1]] = [96, 96]
mp[[7], [0, 1]] = [96, 96]
mp[[8], [0, 1]] = [96, 96]

# ################################################
# ############# KRAJ UNOSA PODATAKA ##############
# ################################################
