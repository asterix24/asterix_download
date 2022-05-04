#!/bin/bash

hugo --cleanDestinationDir --printI18nWarnings --debug --log

rsync -zvrah --delete public/  caiusbonus:/home/asterix/blog/
