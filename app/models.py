from django.db import models

class Image(models.Model):
    titre = models.CharField(max_length=255)  # nom de l'image
    image = models.FileField(upload_to='')  # chemin vers le fichier image
    description = models.TextField(blank=True)  # description optionnelle
    creer_a = models.DateTimeField(auto_now_add=True)  # date d'ajout

    def __str__(self):
        return self.titre
