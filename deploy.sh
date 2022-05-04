#!/bin/bash

hugo

rsync -zvrah --delete public/  caiusbonus:/home/asterix/blog/
