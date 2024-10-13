import numpy as np
from scipy.optimize import linprog

# Coeficientes da função objetivo (lucros)
c = [-30, -20, -50]  # Os sinais são invertidos porque linprog minimiza

# Coeficientes das restrições
A = [
    [20, 30, 20],  # Insumo I1
    [40, 30, 10],  # Insumo I2
    [10, 50, 40]   # Insumo I3
]

# Limites superiores das restrições
b = [300, 300, 450]

# Resolver o problema usando linprog
res = linprog(c, A_ub=A, b_ub=b, method='highs')

# Verificando se a solução foi encontrada
if res.success:
    print("Solução Ótima Encontrada:")
    print(f"x1 = {res.x[0]:.2f}")
    print(f"x2 = {res.x[1]:.2f}")
    print(f"x3 = {res.x[2]:.2f}")
    print(f"Valor Máximo de Z = {-res.fun:.2f}")
else:
    print("Não foi possível encontrar uma solução.")
