# Nom de votre Projet

openwisk guide

## Installation
```sh
wsk action create script_1 script_1.js
wsk action create script_2 script_2.py
wsk action create script_3 script_3.php
wsk action create render render_browser.js

wsk action create sequence_1 --sequence script_1,script_2,script_3
wsk action create sequence_web --sequence script_1,script_2,script_3,render --web true

wsk action invoke sequence_1 -r
wsk action invoke sequence_web -r
wsk action get seqeunce_web --url
```
-

## Utilisation

il faut créer les actions, ensuite créer les sequences dont l'un est exposé sur le web via l'url défini lors de la configuration de openwisk.
