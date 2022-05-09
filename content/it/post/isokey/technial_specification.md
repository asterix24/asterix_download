+++
author = "asterix"
title = "IsoKey Tecnical Specification"
date = "2022-03-30"
description = "Isokey keyboard technical specification"
draft = false
tags = [
    "isokey",
    "keyboard",
    "technical",
    "specification"
]
+++

# Panoramica

La tastiera IsoKey è una tastiera "stadard" ISO 105 tasti, dove i tasti sono allineati e
disposti a griglia e le principali caratteristiche sono:

* [120 Tasti](#tasti)
* 14 tasti extra prgrammabili
* [XDA Keycap profile](#keycaps)
* Spazio diviso
* Enter ISO!
* [Modulo CPU sostituibilie](#cpu)
* Completamente programmabile con [qmk firmware](https://github.com/asterix24/qmk_firmware)
* 4 RGB led programmbili
* Led Engine programmabili
* Memoria EEProm per salvare la configurazione
* USB type-C
* Chassis in plexigrass verniciata con vernicia acrilica
* Frame in alluminio tagliato a laser


{{< figure src="/images/isokey_all.png" width=100% class="image-right image-board image-bg-light" >}}

---

## Tasti

{{< figure src="/images/isokey-extra11.png" width=20% class="image-right image-board image-bg-light" >}}

La tastiera è basata su un layout standard ISO a 105 tasti e per aggiungere più
funzionalità sono stati aggiungi più tasti, fino a 120.

Grazie alla flessibilità del [qmk firmware](https://github.com/asterix24/qmk_firmware) si
possono mappare a piacimento tutti i tasti della tastiera, oltre a questo qmk gestisce più layout. I layout si possono attivare tramite tasti progrmmati e/o sequenze di tasti.

{{< figure src="/images/isokey-extra1.png" width=25% class="image-left image-board image-bg-light" >}}

La IsoKey ha dei tasti in più messi sulla sinistra della tastiera. Questo per dare la
possibilità l'utente di potere definire delle macro e/o funzionalità aggiuntive che si
possono attivre usando la mano sinistra, in questo modo nella mano destra si può tenere il
mouse.

{{< figure src="/images/gateron.png" width=20% class="image-right image-board image-bg-light" >}}

IsoKey è una tastiera meccanica con switch sono di tipo cherry e, nel caso specifico la tastiera monta i [Gaterorn Brown](https://www.gateron.co/products/gateron-switch-set?variant=39452443214031), che sono clicky e non rumorosi.

I Gateron sono uno dei tanti cloni che si trovano sul mercato dei cherry mx, con un costo
molto competitivo 0,3&euro; rispetto a ~1&euro; dei cherry.. la differenza non è molto, ma
se considerando che ci sono 120 tasti.. il riparmio è evidente.

---

## Keycaps

{{< figure src="/images/isokey13.png" width=40% class="image-left image-board image-bg-light" >}}

I keycaps hanno profilo XDA che sono basati sui DSA questo profilo che sono piatti, e non hanno distizioni per righe. Questo semplifica molto
la realizzazione di layout. Fortunamente ci sono più produttori di questi tipo di tasti e
si riescono a trovare sul mercato a prezzi abbordabili, colori e dimensioni assortite.

---

## CPU

{{< figure src="/images/isokey12.png" width=70% class="image-right image-board image-bg-light" >}}

Il cuore della tastiera è stato affidato al modulino: [WeAct Black Pill V2.0](https://stm32-base.org/boards/STM32F411CEU6-WeAct-Black-Pill-V2.0.html)

Questo è modulino basato su un STM32F4 dell'ST. Il modulino ha il vantaggio di essere
economico e cosa non da poco la cpu supporta il DFU bootloader..

L'uso di un modulino esterno è una cosa voluta, si per un motivo estetico, ma anche per
dare la possibilità di poterlo sostiture a piacimento.

Oltre al modulino, la tastiera prevede sulla scheda principale anche una memoria eeprom
che il drivere per i led.
Il driver dei led è di tipo inteligente, nel senso che si programmare delle sequenze e
farle eseguire alla engine del driver in modo del tutto autonomo, senze intervento della
CPU.

---

## Backshell

{{< figure src="/images/milling_ok1.png" width=30% class="image-left image-board image-bg-light" >}}

Per ridurre i costi, alcune parti della tastiera sono state realizzate con pezzi di
recupero. Nel caso specifico, il Backshell è stato realizzato con una lastra di plexiglass
spesso di 15mm, scavato con la fresa per consentire l'alloggiamento dell'elettronica e
del frame che sostiene gli switch.

