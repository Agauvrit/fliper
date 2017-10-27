FLIP

* Langage : Python

* Résumé du projet :

Ce projet à pour but de pouvoir générer une suite de mouvements afin de résoudre une combinaison donnée pour un Rubik's Cube

* Contributeurs au projet :
Jérémy BERNIER
Aurélien GAUVRIT
Jules MARECAILLE
Vincent COTINEAU
Thomas PICARD
Arthur DAILLAND
Guillaume FERRAND

---------------------------------------------------------------------------------------------------------------------------------------------------

Le fichier Rubik.py contient la classe qui modélise le cube et les opérations qu'on peut effectuer dessus.

Il contient notamment une méthode afficherRubik() qui permet d'afficher le cube dans la console ainsi qu'une méthode afficher2D() qui ouvre une fenetre
qui contient un affichage graphique en 2D du cube.

---------------------------------------------------------------------------------------------------------------------------------------------------

3 méthodes de résolution sont disponibles dans ce Projet:

-La méthode de Résolution classique, c'est à dire la méthode la plus simple utilisé par les humains pour résoudre le cube.

-La méthode de Petrus, c'est une méthode avancée utilisé pour résoudre le cube avec le moins de mouvement possible.

-La méthode de Fridrich, c'est une méthode qui donne de très bon résultat quand à la quantité de mouvement à utiliser.

----------------------------------------------------------------------------------------------------------------------------------------------------

Resolution Classique :

La résolution classique est stockée dans le fichier ResolutionClassique.py

L'appel se fait de la manière suivante :

Solution = ChoixClassique(cube)

La fonction ResoudreClassique prend en paramètre une chaîne de 54 caractère modélisant le cube;
Elle retourne une liste des mouvements à effectuer pour modifier le cube de sa permutation initiale à la permutation résolue.

-----------------------------------------------------------------------------------------------------------------------------------------------------

Resolution de Petrus :

la résolution de petrus est stockée dans le fichier ResolutionPetrus.py

L'appel se fait de la manière suivante :

Solution = ChoixPetrus(cube)

La fonction ResoudrePetrus prend en paramètre une chaîne de 54 caractère modélisant le cube;
Elle retourne une liste des mouvements à effectuer pour modifier le cube de sa permutation initiale à la permutation résolue.

------------------------------------------------------------------------------------------------------------------------------------------------------

Resolution de Friedrich

La résolution du cube avec la méthode dite "de Friedrich" est stockée dans le fichier ResolutionFridrich.py

L'appel se fait de la manière suivante :

Solution = ChoixFridrich(cube)

La fonction ResoudreFridrich prend en paramètre une chaîne de 54 caractère modélisant le cube;
elle retourne une liste des mouvements à effectuer pour modifier le cube depuis sa permutation initiale à la permutation résolue.