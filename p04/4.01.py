import typing
import numpy as np
import pandas as pd
     
def stratified_k_split(
    D: pd.DataFrame,
    k: int
):
    # TODO
    pass

def unzip(x: list[tuple]):
    # TODO
    pass

# pseudo-code
def cross_val(
    a: function,
    hs: dict,
    D: pd.DataFrame,
    m: function
) -> float:
    predicted_x_y = np.ndarray()
    for X_train, y_train, X_valid, y_valid in stratified_k_split(D, 5):
        model = a.fit(X_train, y_train, **hs) # hs puede definir probabilidades sobre los hyperparametros
        predicted_x_y.append((model.predict(X_valid), y_valid))
    predicted, y = unzip(predicted)
    return m(predicted, y)

# pseudo-code
def grid_search(
    X: list[tuple[function, dict]], 
    D: pd.DataFrame, 
    m: function,
) -> tuple[function, dict, float]:
    a_max = None
    hs_max = None
    v_max = -np.inf
    for a, hs in X:
        v = cross_val(a, hs, D, m)
        if v > v_max:
            a_max = a
            hs_max = hs
            v_max = v
    return a_max, hs_max, v_max

# pseudo-code
def randomized_search(
    X: list[tuple[function, dict]], 
    D: pd.DataFrame, 
    m: function,
    n: int
) -> tuple[function, dict, float]:
    a_max = None
    hs_max = None
    v_max = -np.inf
    for a, hs in X:
        vs = np.ndarray()
        for _ in range(n):
            vs.append(cross_val(a, hs, D, m))
        # tomamos el promedio de los intentos
        # podriamos hacer otra cosa
        v = vs.mean()
        if v > v_max:
            a_max = a
            hs_max = hs
            v_max = v
    return a_max, hs_max, v_max
