from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('signup/', views.inscription, name='signup'),
    path ('index/', views.index, name='index'),
    path('menu/', views.menu, name='menu'),


    path('person_form/', views.person_form_view, name='person_form'),
    path('success/', views.success_view, name='success'),

    path('patient/', views.patient_form_view, name='patient'),
    path('patient_list/',views.patient_list_view, name='patient_list' ),
    path('patient/modifier/<int:patient_id>/', views.modifier_patient, name='modifier_patient'),
    path('patient/supprimer/<int:patient_id>/', views.supprimer_patient, name='supprimer_patient'),

    path('medecin/', views.medecin_form_view, name='medecin'),
    path('medecin_list/',views.medecin_list_view, name='medecin_list' ),
    path('medecin/modifier/<int:medecin_id>/', views.modifier_medecin, name='modifier_medecin'),
    path('medecin/supprimer/<int:medecin_id>/', views.supprimer_medecin, name='supprimer_medecin'),
    
    path('consultation/',views.consultation_form_view, name='consultation' ),
    path('consultation_list/',views.consultation_list_view, name='consultation_list' ),
    path('consultation/modifier/<int:consultation_id>/', views.modifier_consultation, name='modifier_consultation'),
    path('consultation/supprimer/<int:consultation_id>/', views.supprimer_consultation, name='supprimer_consultation'),

    path('prescription/',views.prescription_form_view, name='prescription' ),
    path('prescription_list/',views.prescription_list_view, name='prescription_list' ),
    path('prescription/modifier/<int:prescription_id>/', views.modifier_prescription, name='modifier_prescription'),
    path('prescription/supprimer/<int:prescription_id>/', views.supprimer_prescription, name='supprimer_prescription'),

    path('rendez_vs/',views.rendez_vs_form_view, name='rendez_vs' ),
    path('rendez_vs_list/',views.rendez_vs_list_view, name='rendez_vs_list' ),
    path('rendez_vs/modifier/<int:rendez_vs_id>/', views.modifier_rendez_vs, name='modifier_rendez_vs'),
    path('rendez_vs/supprimer/<int:rendez_vs_id>/', views.supprimer_rendez_vs, name='supprimer_rendez_vs'),

    
]
