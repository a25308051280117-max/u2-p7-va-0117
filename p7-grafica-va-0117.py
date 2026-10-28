import numpy as np
import matplotlib.pyplot as plt
#Matias Lopez NC 0117
no_lista=[1,2,3,17,48]
califa_ml=[20,30,80,100,90]
califa_va=[70,90,60,80,100]
plt.plot(no_lista,califa_ml,label="califa ML")
plt.plot(no_lista,califa_va,label="califa VA")
plt.title("calificaciones materias 0117")
plt.xlabel("numero de lista")
plt.ylabel("calificacion")

plt.legend()
plt.show()