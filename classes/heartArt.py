from classes.colors import bcolors
import math


def desenhar_coracao(width, height, mensagemNoMeio, simbolo):  # fiz isso pra aprender matematica na programacao :)
    m_len = len(mensagemNoMeio)
    m_y = height // 2
    m_x_start = (width - m_len) // 2
    resultado = ""
    for y in range(1, height + 1):
        l = ""
        for x in range(1, width + 1):
            xp = (x - width / 2) / (width / 8)
            yp = -(y - height / 2) / (height / 4)
            v = (xp**2 + yp**2 - 1)**3 - xp**2 * yp**3
            if y == m_y and m_x_start <= x < m_x_start + m_len:
                l += mensagemNoMeio[x - m_x_start]
            elif v <= 0:
                l += simbolo
            else:
                l += " "
        resultado += bcolors.RED + l + bcolors.ENDC + "\n"
    print(resultado)
