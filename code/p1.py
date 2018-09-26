#!/usr/bin/env python2.7

import matplotlib.pyplot as plt
import numpy as np
import os
script_dir = os.path.dirname(__file__)
image_file = os.path.join(script_dir, '../images/p1.png')


xs = np.linspace(-5, 5, 100)
ys = xs**2 - 1
plt.plot(xs, ys)
plt.savefig(image_file, dpi=300)