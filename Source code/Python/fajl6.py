# Autor: Jasmin Grbo

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

bc = 8
be = 8
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
               [0, 10],
               [0, 20],
               [10, 20],
               [20, 20],
               [20, 10],
               [10, 10],
               [20, 0]))

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
               [5, 6],
               [6, 1],
               [5, 7]))

# ###################################################
# kmipp - karakteristike materijala i poprečnog presjeka
# pe = np.array(([3e7, 24e-2, 72e-4],   (E, A, I) -> element 0
#                [3e7, 24e-2, 72e-4]))  (E, A, I) -> element 1
# ###################################################

kmipp = np.array(([3e7, 1, 1],
                  [3e7, 1, 1],
                  [3e7, 1, 1],
                  [3e7, 1, 1],
                  [3e7, 1, 1],
                  [3e7, 1, 1],
                  [3e7, 1, 1],
                  [3e7, 1, 1]))

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
pru[7, [3, 4, 5]] = [0, 0, 0]

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
optnc[0, [3]] = [0.9]
optnc[6, [1, 3]] = [-1, 0.9]
optnc[1, [0, 3]] = [0.9, 0.9]
optnc[2, [0, 4]] = [0.9, -1]
optnc[3, [1]] = [-1]
optnc[5, [4]] = [-1]

# ###################################################
# pzd - pomjeranje za dijagram
# ###################################################

pzd = np.zeros((be, 6))
pzd[3, [3]] = 1

# ###################################################
# mp - moment plastičnosti
# mp = 1000 * np.ones((be, bcpe))
# ###################################################

mp = 200 * np.ones((be, 2))

# ################################################
# ############# KRAJ UNOSA PODATAKA ##############
# ################################################
