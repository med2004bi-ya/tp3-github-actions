
import pytest
from unittest.mock import patch

from app.surveillance import surveiller


# Test 1 : taux supérieur à 0.10
def test_surveillance_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:

        resultat = surveiller(0.15)

        assert resultat == "alerte"

        notifier.assert_called_once_with("Taux eleve")


# Test 2 : taux inférieur à 0.10
def test_surveillance_taux_normal():
    with patch("app.surveillance.envoyer_notification") as notifier:

        resultat = surveiller(0.05)

        assert resultat == "ok"

        notifier.assert_not_called()


# Test 3 : taux exactement égal à 0.10
def test_surveillance_seuil_exact():
    with patch("app.surveillance.envoyer_notification") as notifier:

        resultat = surveiller(0.10)

        assert resultat == "ok"

        notifier.assert_not_called()


# Test 4 : simulation d'une panne du service (Bonus)
def test_surveillance_erreur_notification():
    with patch("app.surveillance.envoyer_notification") as notifier:

        notifier.side_effect = RuntimeError("Service non disponible")

        with pytest.raises(RuntimeError, match="Service non disponible"):
            surveiller(0.15)

        notifier.assert_called_once_with("Taux eleve")
