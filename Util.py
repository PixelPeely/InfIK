import numpy as np

def linearTransformation(v, m):
    size = len(v)
    if (size != len(m)):
        print(f"Illegal vector and matrix sizes for transformation! (v={size}, m={len(m)})")
        return None
    return np.array([sum([v[i] * m[j][i] for i in range(size)]) for j in range(size)])