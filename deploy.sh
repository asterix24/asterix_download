#!/bin/bash

#hugo --cleanDestinationDir --printI18nWarnings --debug --log
hugo --printI18nWarnings --debug --printMemoryUsage --printPathWarnings --printUnusedTemplates -v --forceSyncStatic --buildFuture --minify


rsync -zvrah --delete public/  caiusbonus:/home/asterix/blog/
