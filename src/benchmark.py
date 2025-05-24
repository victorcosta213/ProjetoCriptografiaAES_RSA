import time
import numpy as np

def medir_tempo(func, *args, repeticoes=200):
    tempos = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        func(*args)
        fim = time.perf_counter()
        tempos.append(fim - inicio)

    if not tempos:
        return 0, 0

  
    limite = np.percentile(tempos, 95)
    tempos_filtrados = [t for t in tempos if t <= limite]

    return np.mean(tempos_filtrados), np.std(tempos_filtrados)
