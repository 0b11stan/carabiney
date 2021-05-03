# Carabiney

Un script python tout simple pour télécharger ses ronéos, toutes ses ronéos
depuis le [site des carabins de bordeaux](https://www.carabinsbordeaux.fr/).

## Usage

Installer les dépendances:
```bash
pip install -r requirements.txt
```

Télécharger tout les pdf dans le dossier local (`$PWD/roneos/`):
```bash
./carabiney.py
```

Générer un pdf depuis tout les sous pdf (nécessite l'outil `pdfunite`):
```bash
pdfunite $(ls ./roneos/) mycompilation.pdf
```

## Demo

![demo](./demo.gif)
