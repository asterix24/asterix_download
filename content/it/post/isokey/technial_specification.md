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

# Overview

Let's see the main feature of isometric keyboard:

* [120 Switches](#switches)
* 14 Programmable extra keys
* [XDA Keycap profile](#keycaps)
* Splitted space key
* Iso Enter!
* [CPU on pluggable module](#cpu)
* Fully customized whit [qmk firmware](https://github.com/asterix24/qmk_firmware)
* 4 RGB led programmable
* Led Engine programmable
* EEProm memory for user configuration
* USB type-C
* Plexiglass chassis red painted
* Aluminium laser cutted key frame


{{< figure src="/images/isokey_all.png" width=100% class="image-right image-board image-bg-light" >}}

## Switches

{{< figure src="/images/isokey-extra11.png" width=20% class="image-right image-board image-bg-light" >}}

The Isokey is based on a 105 iso layout, and to add more functionality, the layout was extended to 120 switches.
All keys are programmable via [qmk firmware](https://github.com/asterix24/qmk_firmware), that allow the user to define custom layers. The layers are multi-levels and we can switch between layers by pressing one programmated key. The user defines its key maps on layers and because they are stacked, you could define only few keys, that replace the base map ones.
{{< figure src="/images/isokey-extra1.png" width=25% class="image-left image-board image-bg-light" >}}

The Isokey also has extra keys placed on the left of the keyboard and above the arrow keys. This is because the user could hold the mouse with right hand, and have the left hand free to use a pre-set macro for his preferite apps.


{{< figure src="/images/gateron.png" width=20% class="image-right image-board image-bg-light" >}}

The Isokey board is a mechanical keyboard, and the switches are cherry basesed. That means you could use all clones of cherry keys. In my case I used the [Gaterorn Brown](https://www.gateron.co/products/gateron-switch-set?variant=39452443214031), that are clicky and noise-less.
Other than that, the Gateron is less expensive than cherry, when I bought it I paid about 0,3&euro; for Gateron when for a cherry the price was about ~1&euro;.. so when we buy 120 switch the price is less expensive..


## Keycaps


{{< figure src="/images/isokey13.png" width=40% class="image-left image-board image-bg-light" >}}

Keycaps are a wide argument.. I will do separate post..
The main problem that I found when choosing the keycaps was the availability.. This is because the majority of selled keyboards haven't an isometric layout, so that heavily affects the choice. Another problem was the price.. obvious when we want design or custom .. the price will grow..  
So, after hours spent searching for a keycap, I chose the XDA profile. The XDA profile is a DSA profile, but with more height. The other advantage of these keycaps is that they are flat, and don't have a row profile. Fortunately, there is more than one company that made these keys,  so I found colored caps without labels on and all sizes..

Chosen keycaps I could start to draw my layout..


## CPU

{{< figure src="/images/isokey12.png" width=70% class="image-right image-board image-bg-light" >}}

My daily job is to design and develop embedded systems.. making a keyboard is not hard for me..

.. first I define the layout and keyboard shape, and then I start to make the pcbs that hold switches and cpu.
The CPU module I chose to leave out of the main plate, so If you want you can change it with different micro or architecture you can do it. I saw on internet you could find all kind of module powerfully or with strange feature, so I decided to use on of this, in particular: [WeAct Black Pill V2.0](https://stm32-base.org/boards/STM32F411CEU6-WeAct-Black-Pill-V2.0.html), this module is based on a STM32F4 microcontroller of ST. I like it, because it has some useful features, like the embedded DFU.. (I will write a post on it..)
Together with the cpu module, on plate I also put an eeprom ic, and the led driver. The led driver could be programm to do led effects, without any cpu cycle. The eeprom memory needs to keep the user configuration, like the extra key value, or other things, like the keystroke number.

## Backshell

{{< figure src="/images/milling_ok1.png" width=30% class="image-left image-board image-bg-light" >}}

The mechanical part of the keyboard was built using waste material, in particular for the backshell I used a sheet of plexiglas, and for the plate I used an aluminium foil.

The backshell was milled and profiled, and the plate was laser cutted. The plate was left without any paint, but the backshell was painted with red acrylic water based paint.




