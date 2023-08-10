from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator
from .form import PersonForm,PatientForm,MedecinForm,ConsultationForm,PrescriptionForm,Rendez_vsForm,SignupForm
from .models import Patient,Medecin,Consultation,Prescription,Rendez_vs
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

def inscription(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            return redirect('index')  
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu') 
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'index.html', {'error_message': error_message})
    else:
        return render(request, 'index.html')



def menu(request):
    return render(request,'menu.html')


def person_form_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()
    return render(request, 'persons/person_form.html', {'form': form})
def success_view(request):
    return render(request, 'persons/success.html')



def patient_form_view(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patient.html', {'form': form})
def patient_list_view(request):
    patients = Patient.objects.all()
    paginator = Paginator(patients, 5)  # Nombre de patients par page
    page_number = request.GET.get('page')
    patients = paginator.get_page(page_number)
    context = {'patients': patients}
    return render(request, 'patients/patient_list.html', context)

def modifier_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_modifier.html', {'form': form})

def supprimer_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/patient_supprimer.html', {'patient': patient})



def medecin_form_view(request):
    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medecin_list')
    else:
        form = MedecinForm()
    return render(request, 'medecins/medecin.html', {'form': form})
def medecin_list_view(request):
    medecins = Medecin.objects.all()
    paginator = Paginator(medecins, 5) 
    page_number = request.GET.get('page')
    medecins = paginator.get_page(page_number)
    context = {'medecins': medecins}
    return render(request, 'medecins/medecin_list.html', context)

def details_medecin(request, medecin_id):
    medecin = get_object_or_404(Medecin, pk=medecin_id)
    return render(request, 'medecins/medecin_details.html', {'medecin': medecin})

def modifier_medecin(request, medecin_id):
    medecin = get_object_or_404(Medecin, pk=medecin_id)
    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            return redirect('medecin_list')
    else:
        form = MedecinForm(instance=medecin)
    return render(request, 'medecins/medecin_modifier.html', {'form': form})

def supprimer_medecin(request, medecin_id):
    medecin = get_object_or_404(Medecin, pk=medecin_id)
    if request.method == 'POST':
        medecin.delete()
        return redirect('medecin_list')
    return render(request, 'medecins/medecin_supprimer.html', {'medecin': medecin})


def consultation_form_view(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultation_list')
    else:
        form = ConsultationForm()
    return render(request, 'consultations/consultation.html', {'form': form})
def consultation_list_view(request):
    consultations = Consultation.objects.all()
    paginator = Paginator(consultations, 5) 
    page_number = request.GET.get('page')
    consultations = paginator.get_page(page_number)
    return render(request, 'consultations/consultation_list.html', {'consultations': consultations,})

def details_consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    return render(request, 'consultations/consultation_details.html', {'consultation': consultation})

def modifier_consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('consultation_list')
    else:
        form = ConsultationForm(instance=consultation)
    return render(request, 'consultations/consultation_modifier.html', {'form': form})

def supprimer_consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    if request.method == 'POST':
        consultation.delete()
        return redirect('consultation_list')
    return render(request, 'consultations/consultation_supprimer.html', {'consultation': consultation})


def prescription_form_view(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/prescription.html', {'form': form})
def prescription_list_view(request):
    prescriptions = Prescription.objects.all()
    paginator = Paginator(prescriptions, 5) 
    page_number = request.GET.get('page')
    prescriptions = paginator.get_page(page_number)
    context = {'prescriptions': prescriptions}
    return render(request, 'prescriptions/prescription_list.html', context)

def modifier_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm(instance=prescription)
    return render(request, 'prescriptions/prescription_modifier.html', {'form': form})

def supprimer_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    if request.method == 'POST':
        prescription.delete()
        return redirect('prescription_list')
    return render(request, 'prescriptions/prescription_supprimer.html', {'prescription': prescription})


def rendez_vs_form_view(request):
    if request.method == 'POST':
        form = Rendez_vsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rendez_vs_list')
    else:
        form = Rendez_vsForm()
    return render(request, 'rendez_vs/rendez_vs.html', {'form': form})

def rendez_vs_list_view(request):
    rendez_vs = Rendez_vs.objects.all()
    paginator = Paginator(rendez_vs, 5) 
    page_number = request.GET.get('page')
    rendez_vs = paginator.get_page(page_number)
    context = {'rendez_vs': rendez_vs}
    return render(request, 'rendez_vs/rendez_vs_list.html', context)

def modifier_rendez_vs(request, rendez_vs_id):
    rendez_vs = get_object_or_404(Rendez_vs, pk=rendez_vs_id)
    if request.method == 'POST':
        form = Rendez_vsForm(request.POST, instance=rendez_vs)
        if form.is_valid():
            form.save()
            return redirect('rendez_vs_list')
    else:
        form = Rendez_vsForm(instance=rendez_vs)
    return render(request, 'rendez_vs/rendez_vs_modifier.html', {'form': form})

def supprimer_rendez_vs(request, rendez_vs_id):
    rendez_vs = get_object_or_404(Rendez_vs, pk=rendez_vs_id)
    if request.method == 'POST':
        rendez_vs.delete()
        return redirect('rendez_vs_list')
    return render(request, 'rendez_vs/rendez_vs_supprimer.html', {'rendez_vs': rendez_vs})

def accueil(request):
    return render(request, 'accueil.html')




