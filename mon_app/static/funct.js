$(document).ready(function() {
    $('.btn-supprimer').click(function() {
        var medecinId = $(this).data('id');
        
        // Envoyer une requête AJAX pour supprimer la consultation
        $.ajax({
            url: 'http://127.0.0.1:8000/medecin/supprimer/'+ medecinId,
            type: 'POST',
            success: function(response) {
                // Mettre à jour l'affichage ou rediriger vers la liste des consultations
            },
            error: function(xhr, errmsg, err) {
                // Gérer les erreurs
            }
        });
    });

    $('.btn-modifier').click(function() {
        var medecinId = $(this).data('id');
        
        // Rediriger vers la page de modification de la consultation
        window.location.href = '/medecin/' + medecinId + '/modifier/';
    });
});