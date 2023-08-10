from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Patient(Person):
    matricule = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.last_name} {self.first_name} (matricule: {self.matricule}) {self.age}"

class Medecin(Person):
    matricule = models.CharField(max_length=100)
    adress_Pro = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)

class Consultation(models.Model):
      date = models.DateField(auto_now_add=True)
      heure = models.TimeField(auto_now_add=True)
      diagnostic = models.TextField()
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
      medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)

class Rendez_vs(models.Model):
      libelle = models.TextField()
      datePrevu = models.DateField()
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
      medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)

class Prescription(models.Model):
      ordonnance = models.TextField()
      analyse = models.TextField()
      radiologie = models.TextField()
      consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)






