---
title: "Trip wallet"
author: "Norma Korošec, Luka Vidic"
date: "16 april 2018"
output: html_document
abstract: "Aplikacija je namenjena vodenju financ za skupine prijateljev, ki se skupaj odpravijo na počitnice."
---

# Trip wallet / Potovalna denarnica

Potovalna denarnica je spletna aplikacija, ki uporabnikom omogoča pravično deljenje stroškov, ki nastanejo na potovanju.


## Baza podatkov

Za bazo podatkov uporabljava PostgreSQL, glede na naravo aplikacije pa začetnih podatkov ni, saj se kreirajo sproti.

## 

## Vzorčni izlet

2 prijatelja, Tine in Jošt se odločita, da bosta odšla na potovanje v Grčijo. Ker se zavedata stvarnosti in vesta, da je težko vedno imeti dovolj drobiža, da vsak prispeva točno polovico, se odločita, da bosta uporabila Potovalno denarnico, ki bo namesto njiju preračunala, da si bosta pravično razdelila stroške potovanja. Zato se najprej oba registrirata.

|ime|priimek|rojstnidan|telefon|email|username|userid|
|---|---|---|---|---|---|---|
|Tine|Kovačič|3/3/1996|"031211010"|tince@gmail.com|Tinče|ia3bb96g|
|Jošt|Dolenc|2/1/1998|"051245963"|jost33@neki.si|jostD|j3k4aa9k|

Dogovorita se, da Tine poišče in plača letalske karte, Jošt pa prenočišče.

|tip|znesek|placal|udelezeni|oznaka|id_transakcije|prejemnik|
|---|---|---|---|---|---|---|
|nakup|550|ia3bb96g|ia3bb96g|letalske karte|1002345|eDreams|
|nakup|550|ia3bb96g|j3k4aa9k|letalske karte|1002345|eDreams|
|nakup|250|j3k4aa9k|j3k4aa9k|hotel|1002346|GreekHotels|
|nakup|250|j3k4aa9k|ia3bb96g|hotel|1002346|GreekHotels|

Ko prideta v Atene, naročila taksi od letališča do hotela in po napornem letu si najprej malo odpočijeta. Potem se odločita, da si bosta zvečer v prijetni spomladni noči ogledala Atensko Akropolo in Dionizovo gledališče. Za večerjo se odločita, da bosta poskusila tradicionalno grško hrano in seveda lokalno grško pivo.

|tip|znesek|placal|udelezeni|oznaka|id_transakcije|prejemnik|
|---|---|---|---|---|---|---|
|nakup|30|ia3bb96g|ia3bb96g|taksi|1002347|taksist|
|nakup|30|ia3bb96g|j3k4aa9k|taksi|1002347|taksist|

V soboto srečata še eno skupino Slovencev, med katerimi je en dober Joštov prijatelj po imenu Andrej. Vsi skupaj preživijo dan, si ogledajo živalski vrt, potem pa se prijatelj pridruži Tinetu in Joštu in skupaj potujejo naprej, saj so ugotovili, da se z istim letalom vračajo domov.

Naslednji dan Jošta okradejo. Zato se Tine in Andrej odločita, da bosta prijatelju pomagala in sicer tako, da bojo skupaj na ulici peli in igrali na kitaro, ki so si jo izposodili pri naključnih stanovalcih v Atenah. Celo popoldne so igrali in zaslužili 73,50€, Tine in Andrej se odločita, da ves denar pustita Joštu. 

|tip|znesek|placal|udelezeni|oznaka|id_transakcije|prejemnik|
|---|---|---|---|---|---|---|
|donacija|73,50|donator|ia3bb96g|igranje kitare|1002348|j3k4aa9k|
|donacija|73,50|donator|j3k4aa9k|igranje kitare|1002348|j3k4aa9k|
|donacija|73,50|donator|andrej|igranje kitare|1002348|j3k4aa9k|

Kljub še nekaterim drugim zapletom se izlet dobro konča, vsi srečno prispejo domov. Nepozaben izlet v Grčijo vsem ostane v lepem spominu.
