import pandas as pd
import numpy as np


chat_id = 628156322 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    time = 10
    errors = np.random.exponential(scale=1, size=n) - 21
    v_real = x - errors
    a = np.mean(v_real) / time
    return a
