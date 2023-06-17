#############################################################################
#                                                                           #
#         RECONNAISSANCE DE LETTRES MANUSCRITES => APPRENTISSAGE            #
#                                                                           #
# Utilisation du Dataset EMINST:                                            #
#       https://www.tensorflow.org/datasets/catalog/emnist                  #
#       /!\ la documentation fait référence à 37 catégories alors qu'il y   #
#           en a seulement 26 car majuscules et minuscules sont regroupées  #
#                                                                           #
#############################################################################

# Importation des modules
import tensorflow as tf              # exploitation du réseau de neurones
import tensorflow_datasets as tfds   # dataset avec les lettres manuscrites
import numpy as np                   # manipulation de tableaux

#----------------------------------------------------------------------------
# Chargement des données du Dataset EMNIST/LETTERS 
#  => 4 tableaux de type ndarray (Numpy) avec des valeurs entières
#----------------------------------------------------------------------------
(x_train,y_train), (x_test,y_test) = tfds.as_numpy(tfds.load(
     'emnist/letters',       # sélection du dataset avec les lettres
     data_dir="D:/temp/emnist_data/",         # emplacement pour charger le dataset sur disque
     split=['train','test'], # utilisation des données d'apprentissage et test
     as_supervised=True,     # pour obtenir un type 'tuple' ald 'dataset'
     batch_size=-1))         # données stockées dans un seul lot de données
  
#----------------------------------------------------------------------------
# Changements de format pour exploitation
#----------------------------------------------------------------------------
# EMNIST ne mémorise pas les images dans le sens habituel
# ==> il est nécessaire de faire une symétrie horizontale et une rotation 
x_train = x_train.reshape(88800, 28, 28)
x_test  = x_test.reshape (14800, 28, 28)
for i in range(88800): x_train[i]=np.fliplr(np.rot90(x_train[i],k=-1))
for i in range(14800): x_test [i]=np.fliplr(np.rot90(x_test [i],k=-1))
# les valeurs associées aux pixels sont des entiers entre 0 et 255
#  => transformation en valeurs réelles entre 0.0 et 1.0
x_train, x_test = x_train / 255.0, x_test / 255.0
# Les données de sortie sont des entiers correspondant aux lettres à identifier
#  => transformation en vecteurs booléens pour une classification en 26 valeurs
y_train = tf.keras.utils.to_categorical(y_train-1, 26)
y_test  = tf.keras.utils.to_categorical(y_test -1, 26)

#----------------------------------------------------------------------------
# DESCRIPTION du modèle Perceptron multicouches (MLP)
#  => 1 couche cachée avec 200 neurones
#----------------------------------------------------------------------------
# Création d'un réseau multicouches
MonReseau = tf.keras.Sequential()
# Description de la couche d'entrée avec la mise à plat des images
MonReseau.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# Description de la couche cachée avec 200 neurones
MonReseau.add(tf.keras.layers.Dense(units=200, activation='relu'))
# Description de la couche de sortie avec 26 catégories
MonReseau.add(tf.keras.layers.Dense(units=26, activation='softmax'))

#----------------------------------------------------------------------------
# COMPILATION du réseau 
#  => configuration de la procédure pour l'apprentissage
#----------------------------------------------------------------------------
MonReseau.compile(optimizer='adam',                # algo d'apprentissage
                  loss='categorical_crossentropy', # mesure de l'erreur
                  metrics=['accuracy'])            # mesure du taux de succès

#----------------------------------------------------------------------------
# APPRENTISSAGE du réseau
#  => calcul des paramètres du réseau à partir des exemples
#----------------------------------------------------------------------------
MonReseau.fit(x=x_train,     # données d'entrée pour l'apprentissage
              y=y_train,     # sorties désirées associées aux données d'entrée
              batch_size=20, # utilisation de lots avec 20 images
              epochs=10,     # nombre de cycles d'apprentissage 
              validation_data=(x_test,y_test)) # données de validatioon

# Sauvegarde du réseau après apprentissage
MonReseau.save('MonReseau.h5')