Chronos : Taskbar
=================

## Technologies
Langages : **C, C++**
Bibliothèques : **Gtk(C), Gtkmm(C++), Libchronos**

La bibliothèque chronos permettra l'accès aux programmes en cours d'exécution sur le système.

## Objectifs
La barre des tâches devra permettre à l'utilisateur de voir tous les **programmes graphiques actuellement lancés sur son système**.
Elle devra présenter un layout simple présentant chaque processus par **une icone et un texte**

Un simple clique gauche sur un widget de programme devra le **mettre au premier plan**.
Un clique droit devra faire apparaître un **menu contextuel** permettant d'agrandir, minimiser, fermer le programme.

De même, elle sera dotée d'une vue permettant de **connaître l'heure et d'accéder à un menu déroulant** pour executer des actions (éteindre, redémarrer).

## Cahier des charges
> Temporaire

1. Mettre en place une architecture souple à base de type propre au programmes (structures/classes)
2. Créer une fenêtre principale (MainWindow).
3. La fenêtre principale sera dotée d'un layout extensible (**gridlayout**) permettant de répartir des widgets sur plusieurs rangées/colonnes
4. La largeur de la fenêtre devra être indiquée dans une constante du fichier (**#define WIDTH 800**) à titre d'exemple en attendant que la libchronos fournisse cette fonctionnalité
5. La hauteur de la fenêtre sera comprise entre **40 et 160 pixels** (temporaire)
6. Elle devra toujours être au premier plan, **centrée horizontalement et située en haut de l'écran** (temporairement)
7. Chaque cellule d'une rangée devra présenter un texte (ou un boutton)