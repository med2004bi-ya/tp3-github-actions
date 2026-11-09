
import pytest
from unittest.mock import Mock

from app.moderation import decider


# Test 1 : si le message est un spam, il faut le bloquer
def test_decider_spam():
    modele = Mock()
    modele.predict.return_value = "spam"

    resultat = decider(modele, "Offre miracle")

    assert resultat == "bloquer"

    modele.predict.assert_called_once_with("Offre miracle")


# Test 2 : si le message est normal, il faut l'autoriser
def test_decider_normal():
    modele = Mock()
    modele.predict.return_value = "normal"

    resultat = decider(modele, "Bonjour, comment allez-vous ?")

    assert resultat == "autoriser"

    modele.predict.assert_called_once_with(
        "Bonjour, comment allez-vous ?"
    )


# Test 3 : vérifier la propagation d'une erreur 
def test_decider_erreur_modele():
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")

    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Offre miracle")
