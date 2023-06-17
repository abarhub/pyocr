#############################################################################
#                                                                           #
#                RECONNAISSANCE DE LETTRES MANUSCRITES => DEMO              #
#                                                                           #
#############################################################################

# Importation des modules
from PIL import ImageGrab,ImageChops # traitements sur les images
import tensorflow as tf              # exploitation du réseau de neurones
import tkinter as tk                 # interface graphique

# Chargement du réseau de neurones à utiliser
MonReseau = tf.keras.models.load_model('MonReseau.h5')

# Création de la fenêtre principale (Window Root)
W_Root=tk.Tk()
W_Root.title('Reconnaissance de lettres manuscrites')
W_Root.resizable(False,False)       # Non redimensionnable
W_Root.configure(bg="darkgrey")     # Fond gris de la fenêtre

# Mémorisation de la position de la souris lors d'un clic gauche
def Fct_ClicSouris(event):
  global X0,Y0
  X0,Y0 = event.x,event.y

# Tracé d'un trait lors d'un mouvement de souris avec clic gauche enfoncé
def Fct_MvtClicSouris(event):
  global X0,Y0
  x1,y1 = event.x,event.y
  C_Dessin.create_line(X0,Y0,x1,y1,width=20,capstyle='round',fill='black')
  X0,Y0 = x1,y1

# Action associée au bouton B_Reconnaitre
def Fct_Reconnaitre():
  # Coordonnées et dimensions de l'image complète dans la zone Canvas
  x,y = C_Dessin.winfo_rootx(),C_Dessin.winfo_rooty()
  w,h = C_Dessin.winfo_width(),C_Dessin.winfo_height()
  # Copie de l'image, conversion au format N&B et inversion positive/négative
  ImgPIL = ImageGrab.grab(bbox=(x+2,y+2,x+w-2,y+h-2))
  ImgPIL = ImageChops.invert(ImgPIL.convert('L'))
  # Sélection dans l'image d'une zone carrée englobante avec le caractère centré
  (xMin,yMin,xMax,yMax) = ImgPIL.getbbox()
  Taille = min(400, 1.2*max(xMax-xMin,yMax-yMin))
  dx,dy = (Taille-(xMax-xMin))//2,(Taille-(yMax-yMin))//2
  ImgPIL = ImgPIL.crop((xMin-dx,yMin-dy,xMax+dx,yMax+dy))
  # Transformation de l'image au format attendu en entrée du réseau de neurones
  ImgArray=tf.keras.utils.img_to_array(ImgPIL.resize((28,28)))/255
  # Calcul et affichage de la conclusion 
  S = MonReseau.predict(tf.expand_dims(ImgArray,axis=0),verbose=0)[0]
  L_Conclusion["text"] = '{} / {}'.format(chr(65+S.argmax()),chr(97+S.argmax()))
  L_Confiance ["text"] = 'Confiance: {:.2f} %'.format(100*S.max())

# Action associée au bouton B_Effacer
def Fct_Effacer():
  C_Dessin.delete(tk.ALL)
  L_Conclusion['text'] = '?'
  L_Confiance ['text'] = 'Confiance: ?'

# Zone pour dessiner la lettre à identifier
C_Dessin = tk.Canvas(W_Root,width=400,height=400,bg='white',cursor='dot')
C_Dessin.pack(side=tk.LEFT,padx=10,pady=10) 
# Action associée à la détection d'un clic gauche de souris dans le widget
C_Dessin.bind('<Button-1>', Fct_ClicSouris)
# Action associée à la détection d'un mouvement de la souris avec clic enfoncé
C_Dessin.bind('<B1-Motion>', Fct_MvtClicSouris)

# Bouton pour effacer la zone d'écriture
B_Effacer = tk.Button(W_Root,font=('Arial',16,'bold'),
                      text="EFFACER",
                      command=Fct_Effacer) 
B_Effacer.pack(ipady=10,padx=10,pady=10,expand=True,fill=tk.X)

# Cadre pour délimiter la zone de reconnaissance
F_Reco = tk.Frame(bg='white',bd=3,relief='ridge')
F_Reco.pack(padx=10,pady=10,expand=True,fill=tk.X)

# Bouton pour lancer la reconnaissance
B_Reconnaitre = tk.Button(F_Reco,font=('Arial',16),
                          text="Reconnaître",
                          command=Fct_Reconnaitre)
B_Reconnaitre.pack(ipadx=10,padx=15,pady=15,expand=True,fill=tk.X)

# Label pour afficher le résultat de la reconnaissance
L_Conclusion = tk.Label(F_Reco,font=('Arial',50,'bold'),bg='white', 
                        text='?')
L_Conclusion.pack(pady=10,expand=True)

# Label pour afficher la confiance dans la reconnaissance
L_Confiance = tk.Label(F_Reco,font=('Arial',12,'italic'),bg='white',
                       text='Confiance : ?')
L_Confiance.pack(pady=10,expand=True)

# Bouton pour sortir de l'application
B_Quitter = tk.Button(W_Root,font=('Arial',16,'bold'),
                      text='QUITTER',
                      command=W_Root.destroy)
B_Quitter.pack(ipady=10,padx=10,pady=10,expand=True,fill=tk.X)

# Gestion de la fenêtre principale
W_Root.mainloop()