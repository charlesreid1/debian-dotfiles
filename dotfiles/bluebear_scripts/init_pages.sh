#!/bin/bash

repos="bots/b-apollo
bots/b-captain-hook
bots/b-ginsberg
bots/b-milton
bots/boring-mind-machine
bots/b-rainbow-mind-machine
docker/d-gitea
docker/d-mediawiki
docker/d-mysql
docker/d-nginx-charlesreid1
docker/d-nginx-subdomains
charlesreid1/dont-sudo-pip
docker/d-phpmyadmin
docker/d-python-files
docker/d-python-helium
bots/embarcadero-mind-machine
charlesreid1/git-commit-ectomy
charlesreid1/github-heroku-attack-rabbits
charlesreid1/git-subway-maps
charlesreid1/how-do-i-heroku
charlesreid1/how-do-i-pandoc
charlesreid1/how-do-i-pelican
charlesreid1/how-do-i-pyenv
charlesreid1/how-do-i-snakemake
bots/papyrus-mind-machine
docker/pod-bots
docker/pod-charlesreid1
docker/pod-webhooks
bots/rainbow-mind-machine
bots/russian-rainbow-mind-machine
charlesreid1/scurvy-knave-theme
charlesreid1/search-demo-mkdocs-material
charlesreid1/translate-yer-docs
bots/uncle-archie
charlesreid1/wisko-manual
"

for i in $repos; do

    repourl="https://git.charlesreid1.com/${i}"

    r=`echo ${i} | sed 's+.*\/\(.*\)$+\1+'`

    echo "Now cloning repo ${r} = ${i}"

    sudo -H -u charles git -C /www/pages.charlesreid1.com/htdocs \
        clone \
        --recursive \
        --separate-git-dir=git.${r} \
        -b gh-pages \
        ${repourl} ${r}
done

#git.b-apollo
#git.b-captain-hook
#git.b-ginsberg
#git.b-milton
#git.boring-mind-machine
#git.b-rainbow-mind-machine
#git.d-gitea
#git.d-mediawiki
#git.d-mysql
#git.d-nginx-charlesreid1
#git.d-nginx-subdomains
#git.dont-sudo-pip
#git.d-phpmyadmin
#git.d-python-files
#git.d-python-helium
#git.embarcadero-mind-machine
#git.git-commit-ectomy
#git.github-heroku-attack-rabbits
#git.git-subway-maps
#git.how-do-i-heroku
#git.how-do-i-pandoc
#git.how-do-i-pelican
#git.how-do-i-pyenv
#git.how-do-i-snakemake
#git.papyrus-mind-machine
#git.pod-bots
#git.pod-charlesreid1
#git.pod-webhooks
#git.rainbow-mind-machine
#git.russian-rainbow-mind-machine
#git.scurvy-knave-theme
#git.search-demo-mkdocs-material
#git.translate-yer-docs
#git.uncle-archie
#git.waxing-gibbous-mind-machine
#git.wisko-manual
