import numpy as np
import matplotlib.pyplot as plt
from math import pi
from matplotlib.animation import PillowWriter

x = np.linspace(-3 * pi, 3 * pi)
y = x * np.cos(x)
z = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('y=xcos(x), z=sin(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot(x, y, z, c='violet')
plt.show()