# Copyright (c) 2020 Marco Mangan <marco.mangan@gmail.com>
# License: BSD 3 clause

import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from dyrapy.datasets import load_ouvidoria

print('Open file...')
data = load_ouvidoria()

bp = data.boxplot()
bp.set_title('Número de dias previstos e realizados, com variação entre previsto e realizado (delta).')

scatter_matrix(data[['previsto', 'realizado', 'delta']])

plt.show()
