import numpy as np
import matplotlib.pyplot as plt

#les arrays sont batis avec les dimensions suivantes:
# pluie, arroseur, watson, holmes
# et chaque dimension: faux, vrai

prob_pluie=np.array([0.8,0.2]).reshape(2,1,1,1)
print("Pr(Pluie)=\n{}\n".format((prob_pluie)))

prob_arroseur=np.array([0.9,0.1]).reshape(1,2,1,1)
print("Pr(Arroseur)=\n{}\n".format((prob_arroseur)))

watson=np.array([[0.8,0.2],[0,1]]).reshape(2,1,2,1)
print("Pr(Watson|Pluie)=\n{}\n".format((watson)))

holmes=np.array([[[1,0],[0.1,0.9]],[[0,1],[0,1]]]).reshape(2,2,1,2)
print("Pr(Holmes|Pluie,arroseur)=\n{}\n".format((holmes)))

print('------------Réponses-----------')

print("a) \n{}\n".format((watson*prob_pluie).sum(0).squeeze()[1])) # prob gazon watson mouille


print("P(H)) \n{}\n".format((watson*prob_pluie).sum(0).squeeze()[1])) # prob gazon watson mouille
