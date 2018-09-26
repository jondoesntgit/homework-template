#!/usr/bin/env python2.7

import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

import os
script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir, '../logs/p2.log')
data_file = os.path.join(script_dir, '../data/sample.csv')
image_file = os.path.join(script_dir, '../images/p2.png')

logging.basicConfig(filename=log_file, filemode='w', level=logging.DEBUG)

df = pd.read_csv(data_file)

xs = df.x.values
ys = df.y.values

m, b = np.polyfit(xs, ys, 1)
plt.plot(xs, ys, 'o')

logging.info("m = %.2f, b = %.2f" % (m, b))

fit_x = np.linspace(0, 5)
fit_y = m * fit_x + b
plt.plot(fit_x, fit_y, ls='dashed')

plt.savefig(image_file, dpi=300)