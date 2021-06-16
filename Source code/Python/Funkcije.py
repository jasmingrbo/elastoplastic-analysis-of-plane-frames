# Autor: Jasmin Grbo

from fajl6 import *
from math import sin, cos, atan
import matplotlib.pyplot as plt
import time


def unikatno_2D(x, y):

    """

    :param x:
    :param y:
    :return:
    """

    for i in range(x):
        for j in range(2):
            if y == pe[i, j]:
                return False
    return True


def pozicija_2D(x, y):

    """

    :param x:
    :param y:
    :return:
    """

    for i in range(x):
        for j in range(2):
            if pe[x, y] == pe[i, j]:
                return i, j


def pozicija2_2D(x, y):

    """

    :param x:
    :param y:
    :return:
    """

    for i in range(x + 1, be):
        for j in range(2):
            if pe[x, y] == pe[i, j]:
                return i, j
    return True, True


def brojanje_2D():

    """

    :return:
    """

    global bssk, pru, ru

    for i in range(be):
        for j in range(2):
            if i == 0:
                if j == 0:
                    for k in range(3):
                        if pru[i, k] != 0:
                            bssk += 1
                            ru[i, k] = bssk
                else:
                    for k in range(3, 6):
                        if pru[i, k] != 0:
                            bssk += 1
                            ru[i, k] = bssk
            elif unikatno_2D(i, pe[i, j]):
                if j == 0:
                    for k in range(3):
                        if pru[i, k] != 0:
                            bssk += 1
                            ru[i, k] = bssk
                else:
                    for k in range(3, 6):
                        if pru[i, k] != 0:
                            bssk += 1
                            ru[i, k] = bssk
            else:
                a, b = pozicija_2D(i, j)
                if j == 0 and b == 0:
                        for k in range(3):
                            if k == 2:
                                if zglob[i, j] == 0:
                                    bssk += 1
                                    ru[i, k] = bssk
                                elif zglob[a, b] == 1:
                                    ru[i, k] = ru[a, k]
                                elif zglob[a, b] == 0:
                                    for l in range(be - a):
                                        a, b = pozicija2_2D(a, b)
                                        if a:
                                            break
                                        elif i == a:
                                            continue
                                        elif zglob[a, b] != 0:
                                            if a > i:
                                                bssk += 1
                                                ru[i, k] = bssk
                                                break
                                            elif b == 0:
                                                ru[i, k] = ru[a, k]
                                                break
                                            else:
                                                ru[i, k] = ru[a, k + 3]
                                                break
                                    if i == a or zglob[a, b] == 0:
                                        bssk += 1
                                        ru[i, k] = bssk
                            else:
                                ru[i, k] = ru[a, k]
                elif j == 0 and b == 1:
                        for k in range(3):
                            if k == 2:
                                if zglob[i, j] == 0:
                                    bssk += 1
                                    ru[i, k] = bssk
                                elif zglob[a, b] == 1:
                                    ru[i, k] = ru[a, k + 3]
                                elif zglob[a, b] == 0:
                                    for l in range(be - a):
                                        a, b = pozicija2_2D(a, b)
                                        if a:
                                            break
                                        elif i == a:
                                            continue
                                        elif zglob[a, b] != 0:
                                            if a > i:
                                                bssk += 1
                                                ru[i, k] = bssk
                                                break
                                            elif b == 0:
                                                ru[i, k] = ru[a, k]
                                                break
                                            else:
                                                ru[i, k] = ru[a, k + 3]
                                                break
                                    if i == a or zglob[a, b] == 0:
                                        bssk += 1
                                        ru[i, k] = bssk
                            else:
                                ru[i, k] = ru[a, k + 3]
                elif j == 1 and b == 0:
                        for k in range(3, 6):
                            if k == 5:
                                if zglob[i, j] == 0:
                                    bssk += 1
                                    ru[i, k] = bssk
                                elif zglob[a, b] == 1:
                                    ru[i, k] = ru[a, k - 3]
                                elif zglob[a, b] == 0:
                                    for l in range(be - a):
                                        a, b = pozicija2_2D(a, b)
                                        if a:
                                            break
                                        elif i == a:
                                            continue
                                        elif zglob[a, b] != 0:
                                            if a > i:
                                                bssk += 1
                                                ru[i, k] = bssk
                                            elif b == 0:
                                                ru[i, k] = ru[a, k - 3]
                                                break
                                            else:
                                                ru[i, k] = ru[a, k]
                                                break
                                    if i == a or zglob[a, b] == 0:
                                        bssk += 1
                                        ru[i, k] = bssk
                            else:
                                ru[i, k] = ru[a, k - 3]
                else:
                        for k in range(3, 6):
                            if k == 5:
                                if zglob[i, j] == 0:
                                    bssk += 1
                                    ru[i, k] = bssk
                                elif zglob[a, b] == 1:
                                    ru[i, k] = ru[a, k]
                                elif zglob[a, b] == 0:
                                    for l in range(be - a):
                                        a, b = pozicija2_2D(a, b)
                                        if a:
                                            break
                                        elif i == a:
                                            continue
                                        elif zglob[a, b] != 0:
                                            if a > i:
                                                bssk += 1
                                                ru[i, k] = bssk
                                            elif b == 0:
                                                ru[i, k] = ru[a, k - 3]
                                                break
                                            else:
                                                ru[i, k] = ru[a, k]
                                                break
                                    if i == a or zglob[a, b] == 0:
                                        bssk += 1
                                        ru[i, k] = bssk
                            else:
                                ru[i, k] = ru[a, k]


def mkeulks_2D(i):

    """

    :param i:
    :return:
    """

    # Vađenje čvorova elementa
    cvor1 = pe[i, 0]
    cvor2 = pe[i, 1]

    # Vađenje koordinata X i Y čvora 1 i 2
    x1 = kc[cvor1, 0]
    x2 = kc[cvor2, 0]
    y1 = kc[cvor1, 1]
    y2 = kc[cvor2, 1]

    # Proračun dužine elementa
    L = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Vađenje karakteristika materijala i poprečnog presjeka
    E = kmipp[i, 0]
    A = kmipp[i, 1]
    I = kmipp[i, 2]
    EI = E * I

    # Formiranje matrice krutosti elementa u lokalnom koordinatnom sistemu
    return ((12 * EI) / L ** 3) * np.array(([(A * L ** 2) / (12 * I), 0, 0, -(A * L ** 2) / (12 * I), 0, 0],
                                            [0, 1, L / 2, 0, -1, L / 2],
                                            [0, L / 2, L ** 2 / 3, 0, -L / 2, L ** 2 / 6],
                                            [-(A * L ** 2) / (12 * I), 0, 0, (A * L ** 2) / (12 * I), 0, 0],
                                            [0, -1, -L / 2, 0, 1, -L / 2],
                                            [0, L / 2, L ** 2 / 6, 0, -L / 2, L ** 2 / 3]))


def mt_2D(i):

    """

    :param i:
    :return:
    """

    # Vađenje čvorova elementa
    cvor1 = pe[i, 0]
    cvor2 = pe[i, 1]

    # Vađenje koordinata X i Y čvora 1 i 2
    x1 = kc[cvor1, 0]
    x2 = kc[cvor2, 0]
    y1 = kc[cvor1, 1]
    y2 = kc[cvor2, 1]

    # Proračun ugla koji element zatvara sa globalnom X-osom
    if x2 - x1 == 0:
        if y2 > y1:
            alfa = 2 * atan(1)
        else:
            alfa = -2 * atan(1)
    elif x2 - x1 < 0:
        if y2 - y1 == 0:
            alfa = 4 * atan(1)
        elif y2 < y1:
            alfa = (4 * atan(1) + atan((y1 - y2) / (x1 - x2)))
    else:
        alfa = atan((y2 - y1) / (x2 - x1))

    # Formiranje matrice transformacije
    return np.array(([cos(alfa), -sin(alfa), 0, 0, 0, 0],
                     [sin(alfa), cos(alfa), 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0],
                     [0, 0, 0, cos(alfa), -sin(alfa), 0],
                     [0, 0, 0, sin(alfa), cos(alfa), 0],
                     [0, 0, 0, 0, 0, 1]))


def lv_2D(i):

    """

    :param i:
    :return:
    """

    # Formiranje lokacijskog vektora
    return np.array(([ru[i, 0]],
                     [ru[i, 1]],
                     [ru[i, 2]],
                     [ru[i, 3]],
                     [ru[i, 4]],
                     [ru[i, 5]]), dtype="int")


def gvsoonc_2D(gvs):

    """

    :param gvs:
    :return:
    """

    # Petlja za proračun globalnog vektora sila od opterećenja na čvoru
    for i in range(be):
        for j in range(bsskpe):
            if ru[i, j] != 0:
                gvs[ru[i, j] - 1] = optnc[i, j]
    return gvs


def gmks_2D(gmks):

    """

    :param gmks:
    :return:
    """

    # Petlja za asembliranje globalne matrice krutosti sistema
    for i in range(be):
        mkeulks = mkeulks_2D(i)
        mt = mt_2D(i)
        mkeugks = np.dot(mt, np.dot(mkeulks, np.transpose(mt)))
        lv = lv_2D(i)
        for j in range(bsskpe):
            if lv[j] != 0:
                for k in range(bsskpe):
                    if lv[k] != 0:
                        gmks[lv[j] - 1, lv[k] - 1] += mkeugks[j, k]
    return gmks


def gmks_i_gvs_2D():

    """

    :return:
    """

    # Asembliranje globalnog vektora sila
    gvs = gvsoonc_2D(np.zeros((bssk, 1)))

    # Asembliranje globalne matrice krutosti sistema
    gmks = gmks_2D(np.zeros((bssk, bssk)))

    return gmks, gvs


def mnpulks_i_sulks_2D(gvnp):

    """

    :param gvnp:
    :return:
    """

    # Inicijalizacija nultih matrica
    # sulks - sile u lokalnom koordinatnom sistemu
    # mnpugks - matrica nepoznatih pomjeranja u globalnom koordinatnom sistemu
    # mnpulks - matrica nepoznatih pomjeranja u lokalnom koordinatnom sistemu
    sulks = np.zeros((be, bsskpe))
    mnpugks = np.zeros((be, bsskpe))
    mnpulks = np.zeros((be, bsskpe))

    # Petlja za proračun sulks i mnpulks
    for i in range(be):
        mkeulks = mkeulks_2D(i)
        mt = mt_2D(i)
        mkeugks = np.dot(mt, np.dot(mkeulks, np.transpose(mt)))
        lv = lv_2D(i)

        for j in range(bsskpe):
            if lv[j] != 0:
                mnpugks[i, j] = gvnp[lv[j] - 1]

        # Vektor čvornih sila elementa u globalnom koordinatnom sistemu
        vcseugks = np.dot(mkeugks, np.transpose(mnpugks[i, :]))

        # Vektor čvornih sila u lokalnom koordinatnom sistemu
        vcseulks = np.dot(np.transpose(mt), vcseugks)

        # Matrica sila u lokalnom koordinatnom sistemu
        sulks[i, :] = vcseulks

        # Matrica nepoznatih pomjeranja u lokalnom koordinatnom sistemu
        mnpulks[i, :] = np.dot(np.transpose(mt), np.transpose(mnpugks[i, :]))

    return mnpulks, sulks


def dijagram_2D(uFO, mnpulks):

    """

    :param uFO:
    :param mnpulks:
    :return:
    """

    global aFO, aPOM

    zastava = False

    for i in range(be):
        for j in range(6):
            if pzd[i, j] == 1:
                aFO.append(uFO)
                mt = mt_2D(i)
                mnpugks = np.dot(mt, np.transpose(mnpulks[i, :]))
                aPOM.append(mnpugks[j] * 1000)
                zastava = True
                break
        if zastava:
            break


def plot_2D(aPOM, aFO):

    plt.plot(aPOM, aFO, "k-o", lw=1.5, mec="k", mfc="r", mew=0.85, ms=4.5)
    plt.xlabel("Ux [mm]", fontsize=10)
    plt.ylabel("FO [kN]", fontsize=10)
    plt.tick_params(labelsize=10)
    plt.show()


def proracun_pz_tpr_2D():

    """

    :return:
    """

    vrijeme = time.time()
    print("Proračun počeo: " + time.strftime("%d.%m.%Y") + " u " + time.strftime("%H:%M:%S"))
    print("-----------------------------------------")

    global pru, bssk, ru, zglob, ite, uFGO, aFO, aPOM

    # Format ispisa
    np.set_printoptions(precision=5, linewidth=300, suppress=True)

    # TODO otvaranje fajla za ipis

    # Brojanje slobodnih stepeni slobode kretanja
    brojanje_2D()

    # Pozivanje funkcije za formiranje globalne matrice krutosti sistema i globalnog vektora sila
    gmks, gvs = gmks_i_gvs_2D()

    # Inicijalizacija početnih varijabli za petlju koja proračunava faktor graničnog opterećenja
    cm = np.zeros((be, 2))
    uFGO = 0
    rgmks = bssk
    ite = 0
    umnpulks = np.zeros((be, 6))
    cntm = np. zeros((be, 6))
    FO = np.zeros((be, 2))
    cmi = np.zeros((be, 2))
    ocm = np.zeros((be, 2))
    aFO = [0]
    aPOM = [0]

    # Petlja za proračun faktora graničnog opterećenja
    while rgmks >= bssk:
        # Dodavanje iteracije
        ite += 1

        # Rješavanje jednačine K u = F
        gvnp = np.linalg.solve(gmks, gvs)

        # Proračun sila i pomjeranja na elementima
        mnpulks, sulks = mnpulks_i_sulks_2D(gvnp)

        # Proračun matrice faktora opterećenja
        def mfo():

            """

            :return:
            """

            for i in range(be):
                for j in range(2):
                    cmi[i, j] = sulks[i, 3 * j + 2]
                    if (cmi[i, j] > 0 and cm[i, j] > 0) or (cmi[i, j] < 0 and cm[i, j] < 0):
                        ocm[i, j] = mp[i, j] - abs(cm[i, j])
                    elif (cmi[i, j] > 0 > cm[i, j]) or (cmi[i, j] < 0 < cm[i, j]):
                        ocm[i, j] = mp[i, j] + abs(cm[i, j])
                    elif cmi[i, j] == 0 and cm[i, j] == 0:
                        if pru[i, 3 * j + 2] == 1 or pru[i, 3 * j + 2] == 0:
                            ocm[i, j] = mp[i, j]
                        else:
                            ocm[i, j] = 0
                    elif cmi[i, j] == 0 and cm[i, j] != 0:
                        ocm[i, j] = mp[i, j] - abs(cm[i, j])
                    elif cmi[i, j] != 0 and cm[i, j] == 0:
                        if ite == 1:
                            ocm[i, j] = mp[i, j]
                        else:
                            ocm[i, j] = mp[i, j] - abs(cmi[i, j])
                    if ocm[i, j] < 1e-10:
                        ocm[i, j] = 0
                    if ocm[i, j] == 0:
                        FO[i, j] = 0
                    elif cmi[i, j] == 0:
                        FO[i, j] = np.inf
                    else:
                        FO[i, j] = ocm[i, j] / abs(cmi[i, j])

        mfo()

        # Određivanje minimalnog faktora iteracije
        mFGO = np.min(FO[np.nonzero(FO)])

        # Akumuliranje
        cm += mFGO * cmi
        umnpulks += mFGO * mnpulks
        cntm += mFGO * sulks
        uFGO += mFGO

        # Petlja za promjenu rubnih uslova
        for i in range(be):
            for j in range(2):
                if FO[i, j] == mFGO:
                    if pru[i, 3 * j + 2] == 0:
                        pru[i, 3 * j + 2] = 1
                    else:
                        zglob[i, j] = 0

        # Plotanje čvora
        dijagram_2D(uFGO, umnpulks)

        # Resetovanje bssk i ru
        bssk = 0
        ru = np.zeros((be, bsskpe), dtype="int")

        # Novo brojanje slobodnih stepeni slobode
        brojanje_2D()

        # Nova gmks i gvs
        gmks, gvs = gmks_i_gvs_2D()

        # Proračun ranga nove globalne matrice krutosti sistema za provjeru while petlje
        rgmks = np.linalg.matrix_rank(gmks)

    print("Proračun završio: " + time.strftime("%d.%m.%Y") + " u " + time.strftime("%H:%M:%S"))
    print("Trajanje proračuna: {}s".format(round(time.time() - vrijeme, 4)))

    # Plotanje dijagrama
    plot_2D(aPOM, aFO)
