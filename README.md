# 🏥 Système de gestion des urgences hospitalières

> Application en ligne de commande (POO) pour enregistrer, prioriser et suivre les patients d'un service d'urgences.

## 🎯 Le projet

Ce projet modélise la gestion d'un service d'urgences hospitalier : chaque patient est enregistré avec un niveau de priorité (de 1 = non urgent à 5 = urgence vitale), et le système permet de trier automatiquement la file d'attente pour prioriser les cas les plus critiques.

## 🧱 Architecture (POO)

| Classe | Rôle |
|---|---|
| `Patient` | Représente un patient (nom, âge, priorité) et sait décrire sa priorité en texte |
| `GestionUrgences` | Gère la liste des patients : ajout, recherche, suppression, modification, affichage trié |

## ✨ Fonctionnalités

- Ajouter un patient (avec validation de la priorité entre 1 et 5)
- Afficher la liste des patients triée par priorité décroissante
- Rechercher un patient par nom
- Supprimer un patient
- Modifier les informations d'un patient existant

## 🩹 Correctif apporté

Dans la fonction `modifier_patient()`, la priorité était assignée au patient **avant** d'être validée : en cas de saisie invalide (ex : 8), le message d'erreur s'affichait mais le patient restait quand même modifié avec la valeur incorrecte. La validation est maintenant effectuée **avant** toute assignation (méthode `_demander_priorite_valide`, qui redemande la saisie tant qu'elle n'est pas comprise entre 1 et 5), pour garantir que l'objet ne se retrouve jamais dans un état invalide.

## 🚀 Utilisation

```bash
python urgences.py
```

```
--- Système de gestion des urgences hospitalières ---
1. Ajouter un patient
2. Afficher la liste des patients
3. Rechercher un patient
4. Supprimer un patient
5. Mettre à jour un patient
6. Quitter
```

## 🛠️ Stack technique

`Python` `POO` (classes, encapsulation, tri par clé avec `lambda`)

---

*Projet personnel - Bachelor Cybersécurité, module Programmation Python (POO).*
