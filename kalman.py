import math
import random
from typing import List

def _matmul(A: List[List[float]], x: List[float]) -> List[float]:
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]

def generate_noisy_data(A: List[List[float]], x: List[float], vals: int, sigma: float) -> List[List[float]]:
    """Generate noisy position measurements without external dependencies."""
    data = [[0.0, 0.0] for _ in range(vals)]
    state = x[:]
    for i in range(vals):
        state = _matmul(A, state)
        rnd1 = random.random()
        rnd2 = random.random()
        data[i][0] = state[0] + sigma * math.sqrt(-2.0 * math.log(rnd1)) * math.sin(2.0 * math.pi * rnd2)
        rnd1 = random.random()
        rnd2 = random.random()
        data[i][1] = state[1] + sigma * math.sqrt(-2.0 * math.log(rnd1)) * math.sin(2.0 * math.pi * rnd2)
    return data
