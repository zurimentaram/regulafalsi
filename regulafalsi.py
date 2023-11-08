import math
import numpy as np


def f(x):
    f = math.pow(x, 2) - 6 * x + 5
    return f


def regulaFalsi(a, b, toleransi, n):
    i = 0
    fa = f(a)

    print("-------------------------------------------------------------------------------------------------------")
    print("%-20s %-20s %-20s %-20s %-20s" % ("n", "a", "b", "x", "f(x)/toleransi"))
    print("-------------------------------------------------------------------------------------------------------")

    # Dilakukan iterasi sampai dengan n yang diinginkan
    while (i <= n):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fx = f(x)
        i += 1

        # Jika f(x) = 0 atau akar telah ditemukan program akan berhenti.
        # Jika |f(x)| < angka toleransi program akan berhenti. Artinya nilai toleransi/error telah dicapai.
        if (fx == 0 or np.abs(f(x)) < toleransi):
            print(f"\nNilai x didapatkan pada saat iterasi ke {i - 1}, dengan nilai x = {round(x)}")
            break
        # Jika tidak maka iterasi akan terus berjalan sampai keadaan di atas.
        else:
            print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, a, b, x, f(x)))

        # Syarat metode tertutup, pada kasus ini Regula Falsi
        if (fa * fx > 0):
            a = x
        else:
            b = x
    return


regulaFalsi(3, 6, 0.001, 10)