
import pytest
from app.texte import nettoyer_texte


@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),
    ("    ", ""),
    ("BONJOUR", "bonjour"),
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu



def test_nettoyer_texte_entree_nombre():
    with pytest.raises(TypeError):
        nettoyer_texte(123)


def test_nettoyer_texte_entree_none():
    with pytest.raises(TypeError):
        nettoyer_texte(None)



def test_nettoyer_texte_autre_fois():
    texte = "  BONJOUR   monde  "

    resultat_premier = nettoyer_texte(texte)
    resultat_deuxieme = nettoyer_texte(resultat_premier)

    assert resultat_deuxieme == resultat_premier
 