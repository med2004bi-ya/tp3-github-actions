    
import pytest
from app.livraison import frais_livraison

def test_livraison_panier_ordinaire():
    # Arrange
    montant = 120
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25


def test_livraison_panier_299():
    assert frais_livraison(299) == 25


def test_livraison_panier_300():
    assert frais_livraison(300) == 0


def test_livraison_panier_301():
    assert frais_livraison(301) == 0


def test_livraison_panier_zero():
    assert frais_livraison(0) == 25


def test_livraison_montant_negatif():
    with pytest.raises(ValueError):
        frais_livraison(-1)



        