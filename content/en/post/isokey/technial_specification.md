+++
author = "asterix"
title = "IsoKey Technical Specification"
date = "2022-03-30"
description = "Isokey keyboard technical specification"
draft = true
tags = [
    "isokey",
    "keyboard",
    "technical",
    "specification"
]
+++

# Overview
---

The IsoKey keyboard is a 105-key ISO "stadard" keyboard, where the keys are aligned,
arranged in a grid.

 The main features are:

* [120 Keys](#keys).
* 14 extra programmable keys
* [XDA Keycap profile](#keycaps)
* Split space
* Enter ISO!
* [Replaceable CPU module](#cpu)
* Fully programmable with [qmk firmware](https://github.com/asterix24/qmk_firmware)
* 4 programmable RGB leds
* Programmable led engine
* EEProm memory to save configuration
* USB type-C
* Plexigrass chassis painted with acrylic varnish
* Laser cut aluminum frame


{{< figure src="/images/isokey_all.png" width=100% class="image-right image-board image-bg-light" >}}

## Keys
---

{{< figure src="/images/isokey-extra11.png" width=20% class="image-right image-board image-bg-light" >}}

The keyboard is based on a standard 105-key ISO layout, and to add more
functionality more keys have been added for a total of 120.

Thanks to the flexibility of the [qmk firmware](https://github.com/asterix24/qmk_firmware) you can
can map all keys of the keyboard at will, besides this qmk manages multiple layouts. The layouts can be activated by programmed keys and/or key sequences.

{{< figure src="/images/isokey-extra1.png" width=25% class="image-left image-board image-bg-light" >}}

The IsoKey has extra keys put on the left side of the keyboard. The intent is to give the
possibility for the user to be able to define macros and/or additional features that can be
can be activated using the left hand, in this way in the right hand you can keep on the
mouse.

{{< figure src="/images/gateron.png" width=20% class="image-right image-board image-bg-light" >}}

IsoKey is a mechanical keyboard with switches are cherry type and, in the specific case the keyboard mounts the [Gaterorn Brown](https://www.gateron.co/products/gateron-switch-set?variant=39452443214031), which are clicky and not noisy.

The Gateron are one of the many clones that are on the market of cherry mx, but with a cost
very competitive 0,3&euro; compared to ~1&euro; of the cherry... the difference is not much, but
if you consider that there are 120 keys.. the saving is evident.

## Keycaps
---

{{< figure src="/images/isokey13.png" width=40% class="image-left image-board image-bg-light" >}}

Keycaps have XDA profile that are based on DSAs this profile that are flat, and do not have distiptions for lines. This greatly simplifies
the creation of isometric layouts. Fortunately there are more manufacturers of these types of keycaps and this simplifies a bit
the availability on the market ... with assortment of colors, sizes, and not least all the prices ...

## CPU
---

{{< figure src="/images/isokey12.png" width=50% class="image-right image-board image-bg-light" >}}

The heart of the keyboard was done by the module: [WeAct Black Pill V2.0](https://stm32-base.org/boards/STM32F411CEU6-WeAct-Black-Pill-V2.0.html)

This is a module based on an STM32F4 from ST. The module has the advantage of being
cheap and what's more the CPU supports DFU bootloader....

The use of an external module is a deliberate thing, yes for aesthetic reasons, but also to
give the possibility to the user to replace it at will.

In addition to the module, the keyboard also provides on the main board an eeprom memory
and the driver for the LEDs.
The LED driver is an intelligent type, in the sense that you can program sequences and have them executed by the driver's engine.
make them execute the engine of the driver in a completely autonomous way, without intervention of the
CPU.

## Backshell
---

{{< figure src="/images/milling_ok1.png" width=30% class="image-left image-board image-bg-light" >}}

To reduce costs, some parts of the keyboard were made from salvaged parts.
In this specific case, the Backshell was made with a sheet of Plexiglass
15mm thick, hollowed with the milling cutter to allow the housing of electronics and the frame that supports.
The frame that supports the switches is a laser-cut aluminum plate.
