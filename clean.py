import os
import shutil

# Chemin vers le dossier à vider
folder_path = './output'

# Vérifie si le dossier existe
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # Supprime tous les fichiers et sous-dossiers
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Supprime le fichier
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Supprime le dossier
        except Exception as e:
            print(f'Erreur lors de la suppression de {file_path}: {e}')
    print(f'{file_path} a été supprimé avec succès.')
else:
    print(f'Le dossier {folder_path} n\'existe pas ou n\'est pas un dossier.')