import os
import numpy as np
import matplotlib.pyplot as plt

random_state = 42
n_samples = 500
n_features = 2
n_components = 3

np.random.seed(random_state)

probs = np.array([0.1, 0.6, 0.3])
means = np.array([[-1., 1.], [0., 1.], [-0.5, 0.5]])
cov = 0.01 * np.eye(n_features)
sizes = np.random.multinomial(1, probs, size=n_samples).sum(axis=0)

X = np.concatenate([np.random.multivariate_normal(mean, cov, size)
                    for mean, size in zip(means, sizes)])

plt.scatter(*X.T)
plt.tight_layout()

path = "../images/"
plt.savefig(os.path.join(path, "gmm.pdf"))
