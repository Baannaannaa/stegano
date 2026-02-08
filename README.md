# Steganographie d’images (Pillow)

Ce script cache une image `.jpg` dans une autre en utilisant les bits de poids faible (4 bits) des canaux RGB, puis permet de la récupérer. [web:1]

## Prérequis
- Python 3
- Pillow : `pip install pillow`

## Dossiers attendus
Le programme attend **exactement 1** fichier `.jpg` dans chaque dossier :
image_de_base/image_visible/
image_de_base/image_cache/
image_a_decoder/

## Utilisation
1. Mets une image dans `image_de_base/image_visible/` et une autre dans `image_de_base/image_cache/`.
2. Lance : `python ton_script.py` → génère `code.jpg`.
3. Mets `code.jpg` dans `image_a_decoder/`.
4. Relance : `python ton_script.py` → génère `decode.jpg`.

## Sorties
- `code.jpg` : image “visible” contenant l’image cachée.
- `decode.jpg` : image cachée reconstruite (qualité réduite car seulement 4 bits/canal).