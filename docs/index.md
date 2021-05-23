## Why?

![TonuINO in a Toniebox - Front]({{ site.url }}/TonUINO-in-a-Toniebox/assets/IMG_20210523_100616_320.png)

I love the simplicity and ruggedized/soft enclosure of [Toniebox](https://tonies.de/toniebox/). However, as a closed system it has some drawbacks like the limited playtime per tonie not to mention the price per tonie and the price of the base system.

On the other hand, [tonUINO](https://www.tonuino.de/) seems to provide the perfect alternative for hobbyists with a soldering iron and some knowledge of electronics.

So the idea was born to build a [tonUINO](https://www.tonuino.de/) inside the enclosure of a [Toniebox](https://tonies.de/toniebox/). I bought a malfunctioning box on ebay put it in a drawer and - almost a year later ¯\\_(ツ)_/¯ - started to implement the idea. 


## Features

The box builds on the three button version of [tonUINO](https://www.tonuino.de/), using the "ears" as Volume down/previous Track and Volume up/next Track. Play/Pause has been added as a little push button along with a power switch.

The box runs on its own with a built in LiPo battery and a charging battery shield. 

Charging and transfering files to the SD-Card is possible through a single micro USB port at the bottom opening of the box.

## What's inside

To get the best formfactor possible, I used the official PCB with jumper wires to establish connections.

- the Toniebox, hollowed out except for the speaker and the ear-buttons
- a power switch
- a pause/play push button
- the official TonUINO PCB
- an Arduino nano
- the DFPlayer with a 32 GB SDcard
- an RC522 sensor board
- a 18650 battery
- the WAVGAT D1 mini battery shield

Want to see more?
- [A look inside](https://kateiren.github.io/TonUINO-in-a-Toniebox/lookinside)
- [Some scripts to help managing SD card content](https://kateiren.github.io/TonUINO-in-a-Toniebox/final%20thoughts)
