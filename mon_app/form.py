from django import forms
from .models import Person,Patient,Medecin,Consultation,Prescription,Rendez_vs

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'email','matricule','age')

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ('first_name', 'last_name', 'email','matricule','adress_Pro','specialite')

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('patient','medecin','diagnostic')

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('ordonnance','analyse','radiologie','consultation')

class Rendez_vsForm(forms.ModelForm):
    class Meta:
        model = Rendez_vs
        fields = ('libelle','datePrevu','patient','medecin')

class SignupForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=150)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)