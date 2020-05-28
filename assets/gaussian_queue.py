import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(1., 4., num=1000)
sf = norm.sf(x)

low = (1. / x - 1. / x ** 3) / (2 * np.pi) ** 0.5 * np.exp(- x ** 2 / 2)
high = 1. / (x * (2 * np.pi) ** 0.5) * np.exp(- x ** 2 / 2)

plt.plot(x, sf, lw=3)
plt.plot(x, low, lw=3)
plt.plot(x, high, lw=3)
plt.xlabel("x")
plt.legend([
    r"$1 - \Phi(x)$", 
    r"$\left(\frac{1}{x} - \frac{1}{x^3}\right) \frac{1}{\sqrt{2\pi}} e^{-x^2 / 2}$",
    r"$\frac{1}{x \sqrt{2\pi}} e^{-x^2 / 2}$"
], fontsize=16)
plt.tight_layout()
path = "../images/"
plt.savefig(os.path.join(path, "gaussian_queue.pdf"))
