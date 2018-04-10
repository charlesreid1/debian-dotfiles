#!/bin/bash 
#
# task-
# aspell
# firefox
# fonts
# hunspell
# libreoffice-help
# manpages
# myspell
# xfonts
# wbrazilian/catalan/bulgarian/etc

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

apt-get remove -y xiterm+thai

apt-get remove -y                            \
        task-amharic                         \
        task-amharic-desktop                 \
        task-arabic                          \
        task-arabic-desktop                  \
        task-asturian                        \
        task-asturian-desktop                \
        task-basque                          \
        task-basque-desktop                  \
        task-belarusian                      \
        task-belarusian-desktop              \
        task-bengali                         \
        task-bengali-desktop                 \
        task-bosnian                         \
        task-bosnian-desktop                 \
        task-brazilian-portuguese            \
        task-brazilian-portuguese-desktop    \
        task-bulgarian                       \
        task-bulgarian-desktop               \
        task-catalan                         \
        task-catalan-desktop                 \
        task-chinese-s                       \
        task-chinese-s-desktop               \
        task-chinese-t                       \
        task-chinese-t-desktop               \
        task-croatian                        \
        task-croatian-desktop                \
        task-cyrillic                        \
        task-cyrillic-desktop                \
        task-czech                           \
        task-czech-desktop                   \
        task-danish                          \
        task-danish-desktop                  \
        task-desktop                         \
        task-dutch                           \
        task-dutch-desktop                   \
        task-dzongkha-desktop                \
        task-esperanto                       \
        task-esperanto-desktop               \
        task-estonian                        \
        task-estonian-desktop                \
        task-finnish                         \
        task-finnish-desktop                 \
        task-french                          \
        task-french-desktop                  \
        task-galician                        \
        task-galician-desktop                \
        task-georgian-desktop                \
        task-german                          \
        task-german-desktop                  \
        task-gnome-desktop                   \
        task-greek                           \
        task-greek-desktop                   \
        task-gujarati                        \
        task-gujarati-desktop                \
        task-hebrew                          \
        task-hebrew-desktop                  \
        task-hebrew-gnome-desktop            \
        task-hindi                           \
        task-hindi-desktop                   \
        task-hungarian                       \
        task-hungarian-desktop               \
        task-icelandic                       \
        task-icelandic-desktop               \
        task-indonesian-desktop              \
        task-irish                           \
        task-irish-desktop                   \
        task-italian                         \
        task-italian-desktop                 \
        task-japanese                        \
        task-japanese-desktop                \
        task-japanese-gnome-desktop          \
        task-kannada-desktop                 \
        task-kazakh                          \
        task-kazakh-desktop                  \
        task-khmer                           \
        task-khmer-desktop                   \
        task-korean                          \
        task-korean-desktop                  \
        task-korean-gnome-desktop            \
        task-kurdish                         \
        task-kurdish-desktop                 \
        task-laptop                          \
        task-latvian                         \
        task-latvian-desktop                 \
        task-lithuanian                      \
        task-lithuanian-desktop              \
        task-macedonian                      \
        task-macedonian-desktop              \
        task-malayalam                       \
        task-malayalam-desktop               \
        task-malayalam-gnome-desktop         \
        task-marathi                         \
        task-marathi-desktop                 \
        task-nepali-desktop                  \
        task-northern-sami                   \
        task-northern-sami-desktop           \
        task-norwegian                       \
        task-norwegian-desktop               \
        task-persian                         \
        task-persian-desktop                 \
        task-polish                          \
        task-polish-desktop                  \
        task-portuguese                      \
        task-portuguese-desktop              \
        task-punjabi                         \
        task-punjabi-desktop                 \
        task-romanian                        \
        task-romanian-desktop                \
        task-russian                         \
        task-russian-desktop                 \
        task-serbian                         \
        task-serbian-desktop                 \
        task-sinhala-desktop                 \
        task-slovak                          \
        task-slovak-desktop                  \
        task-slovenian                       \
        task-slovenian-desktop               \
        task-south-african-english-desktop   \
        task-spanish                         \
        task-spanish-desktop                 \
        task-swedish                         \
        task-swedish-desktop                 \
        task-tagalog                         \
        task-tamil                           \
        task-tamil-desktop                   \
        task-tamil-gnome-desktop             \
        task-telugu                          \
        task-telugu-desktop                  \
        task-telugu-gnome-desktop            \
        task-thai                            \
        task-thai-desktop                    \
        task-thai-gnome-desktop              \
        task-turkish                         \
        task-turkish-desktop                 \
        task-ukrainian                       \
        task-ukrainian-desktop               \
        task-uyghur-desktop                  \
        task-vietnamese-desktop              \
        task-welsh                           \
        task-welsh-desktop                   \
        task-xhosa-desktop                   



apt-get remove -y                             \
        aspell-am                             \
        aspell-ar                             \
        aspell-ar-large                       \
        aspell-bg                             \
        aspell-bn                             \
        aspell-ca                             \
        aspell-cs                             \
        aspell-cy                             \
        aspell-da                             \
        aspell-de                             \
        aspell-de-1901                        \
        aspell-de-alt                         \
        aspell-el                             \
        aspell-eo                             \
        aspell-es                             \
        aspell-et                             \
        aspell-eu                             \
        aspell-eu-es                          \
        aspell-fa                             \
        aspell-fr                             \
        aspell-ga                             \
        aspell-gl-minimos                     \
        aspell-gu                             \
        aspell-he                             \
        aspell-hi                             \
        aspell-hr                             \
        aspell-hu                             \
        aspell-is                             \
        aspell-it                             \
        aspell-kk                             \
        aspell-ku                             \
        aspell-lt                             \
        aspell-lv                             \
        aspell-ml                             \
        aspell-mr                             \
        aspell-nl                             \
        aspell-no                             \
        aspell-pa                             \
        aspell-pl                             \
        aspell-pt-br                          \
        aspell-pt-pt                          \
        aspell-ro                             \
        aspell-ru                             \
        aspell-sk                             \
        aspell-sl                             \
        aspell-sv                             \
        aspell-ta                             \
        aspell-te                             \
        aspell-tl                             \
        aspell-uk



apt-get remove -y                             \
        firefox-esr-l10n-ar                   \
        firefox-esr-l10n-ast                  \
        firefox-esr-l10n-bg                   \
        firefox-esr-l10n-bn-bd                \
        firefox-esr-l10n-bn-in                \
        firefox-esr-l10n-bs                   \
        firefox-esr-l10n-ca                   \
        firefox-esr-l10n-cs                   \
        firefox-esr-l10n-cy                   \
        firefox-esr-l10n-da                   \
        firefox-esr-l10n-de                   \
        firefox-esr-l10n-el                   \
        firefox-esr-l10n-en-za                \
        firefox-esr-l10n-eo                   \
        firefox-esr-l10n-es-ar                \
        firefox-esr-l10n-es-cl                \
        firefox-esr-l10n-es-es                \
        firefox-esr-l10n-es-mx                \
        firefox-esr-l10n-et                   \
        firefox-esr-l10n-eu                   \
        firefox-esr-l10n-fa                   \
        firefox-esr-l10n-fi                   \
        firefox-esr-l10n-fr                   \
        firefox-esr-l10n-ga-ie                \
        firefox-esr-l10n-gl                   \
        firefox-esr-l10n-gu-in                \
        firefox-esr-l10n-he                   \
        firefox-esr-l10n-hi-in                \
        firefox-esr-l10n-hr                   \
        firefox-esr-l10n-hu                   \
        firefox-esr-l10n-id                   \
        firefox-esr-l10n-is                   \
        firefox-esr-l10n-it                   \
        firefox-esr-l10n-ja                   \
        firefox-esr-l10n-kk                   \
        firefox-esr-l10n-km                   \
        firefox-esr-l10n-kn                   \
        firefox-esr-l10n-ko                   \
        firefox-esr-l10n-lt                   \
        firefox-esr-l10n-lv                   \
        firefox-esr-l10n-mk                   \
        firefox-esr-l10n-ml                   \
        firefox-esr-l10n-mr                   \
        firefox-esr-l10n-nb-no                \
        firefox-esr-l10n-nl                   \
        firefox-esr-l10n-nn-no                \
        firefox-esr-l10n-pa-in                \
        firefox-esr-l10n-pl                   \
        firefox-esr-l10n-pt-br                \
        firefox-esr-l10n-pt-pt                \
        firefox-esr-l10n-ro                   \
        firefox-esr-l10n-ru                   \
        firefox-esr-l10n-si                   \
        firefox-esr-l10n-sk                   \
        firefox-esr-l10n-sl                   \
        firefox-esr-l10n-sq                   \
        firefox-esr-l10n-sr                   \
        firefox-esr-l10n-sv-se                \
        firefox-esr-l10n-ta                   \
        firefox-esr-l10n-te                   \
        firefox-esr-l10n-th                   \
        firefox-esr-l10n-tr                   \
        firefox-esr-l10n-uk                   \
        firefox-esr-l10n-vi                   \
        firefox-esr-l10n-zh-cn                \
        firefox-esr-l10n-zh-tw



apt-get remove -y                             \
        fonts-bpg-georgian                    \
        fonts-deva                            \
        fonts-deva-extra                      \
        fonts-dzongkha                        \
        fonts-gargi                           \
        fonts-gujr                            \
        fonts-gujr-extra                      \
        fonts-guru                            \
        fonts-guru-extra                      \
        fonts-lohit-beng-assamese             \
        fonts-lohit-beng-bengali              \
        fonts-lohit-deva                      \
        fonts-lohit-gujr                      \
        fonts-lohit-guru                      \
        fonts-lohit-knda                      \
        fonts-lohit-mlym                      \
        fonts-lohit-taml                      \
        fonts-lohit-taml-classical            \
        fonts-lohit-telu                      \
        fonts-mlym                            \
        fonts-nakula                          \
        fonts-sahadeva                        \
        fonts-samyak-deva                     \
        fonts-samyak-gujr                     \
        fonts-samyak-mlym                     \
        fonts-samyak-taml                     \
        fonts-sipa-arundina                   \
        fonts-telu-extra                      \
        fonts-thai-tlwg                       \
        fonts-tlwg-garuda                     \
        fonts-tlwg-garuda-ttf                 \
        fonts-tlwg-kinnari                    \
        fonts-tlwg-kinnari-ttf                \
        fonts-tlwg-laksaman                   \
        fonts-tlwg-laksaman-ttf               \
        fonts-tlwg-loma                       \
        fonts-tlwg-loma-ttf                   \
        fonts-tlwg-mono                       \
        fonts-tlwg-mono-ttf                   \
        fonts-tlwg-norasi                     \
        fonts-tlwg-norasi-ttf                 \
        fonts-tlwg-purisa                     \
        fonts-tlwg-purisa-ttf                 \
        fonts-tlwg-sawasdee                   \
        fonts-tlwg-sawasdee-ttf               \
        fonts-tlwg-typewriter                 \
        fonts-tlwg-typewriter-ttf             \
        fonts-tlwg-typist                     \
        fonts-tlwg-typist-ttf                 \
        fonts-tlwg-typo                       \
        fonts-tlwg-typo-ttf                   \
        fonts-tlwg-umpush                     \
        fonts-tlwg-umpush-ttf                 \
        fonts-tlwg-waree                      \
        fonts-tlwg-waree-ttf                  \
        fonts-ukij-uyghur                     \
        fonts-unikurdweb



apt-get remove -y                             \
        xfonts-thai                           \
        xfonts-thai-etl                       \
        xfonts-thai-manop                     \
        xfonts-thai-nectec                    \
        xfonts-thai-poonlap                   \
        xfonts-thai-vor                       \
        xfonts-unifont                        \
        xfonts-utils



apt-get remove -y                                \
           hunspell-ar                           \
           hunspell-be                           \
           hunspell-ca                           \
           hunspell-de-at                        \
           hunspell-de-ch                        \
           hunspell-de-de                        \
           hunspell-eu                           \
           hunspell-eu-es                        \
           hunspell-fr                           \
           hunspell-fr-classical                 \
           hunspell-gl-es                        \
           hunspell-hu                           \
           hunspell-it                           \
           hunspell-kk                           \
           hunspell-kmr                          \
           hunspell-ko                           \
           hunspell-lt                           \
           hunspell-ml                           \
           hunspell-ne                           \
           hunspell-ro                           \
           hunspell-se                           \
           hunspell-sl                           \
           hunspell-sr                           \
           hunspell-sv-se                        \
           hunspell-th                           \
           hunspell-vi



apt-get remove -y                             \
        libreoffice-help-ca                   \
        libreoffice-help-cs                   \
        libreoffice-help-da                   \
        libreoffice-help-de                   \
        libreoffice-help-dz                   \
        libreoffice-help-el                   \
        libreoffice-help-es                   \
        libreoffice-help-et                   \
        libreoffice-help-eu                   \
        libreoffice-help-fi                   \
        libreoffice-help-fr                   \
        libreoffice-help-gl                   \
        libreoffice-help-hi                   \
        libreoffice-help-hu                   \
        libreoffice-help-it                   \
        libreoffice-help-ja                   \
        libreoffice-help-km                   \
        libreoffice-help-ko                   \
        libreoffice-help-nl                   \
        libreoffice-help-pl                   \
        libreoffice-help-pt                   \
        libreoffice-help-ru                   \
        libreoffice-help-sk                   \
        libreoffice-help-sl                   \
        libreoffice-help-sv                   \
        libreoffice-help-zh-cn                \
        libreoffice-help-zh-tw



apt-get remove -y                             \
        manpages-de                           \
        manpages-dev                          \
        manpages-es                           \
        manpages-fr                           \
        manpages-fr-extra                     \
        manpages-hu                           \
        manpages-it                           \
        manpages-ja                           \
        manpages-ja-dev                       \
        manpages-pl                           \
        manpages-pl-dev                       \
        manpages-pt                           \
        manpages-tr                           \
        manpages-zh



apt-get remove -y                            \
        myspell-bg                           \
        myspell-ca                           \
        myspell-cs                           \
        myspell-da                           \
        myspell-el-gr                        \
        myspell-eo                           \
        myspell-es                           \
        myspell-et                           \
        myspell-ga                           \
        myspell-he                           \
        myspell-hr                           \
        myspell-it                           \
        myspell-ku                           \
        myspell-lt                           \
        myspell-lv                           \
        myspell-nb                           \
        myspell-nl                           \
        myspell-nn                           \
        myspell-pl                           \
        myspell-pt-br                        \
        myspell-pt-pt                        \
        myspell-ru                           \
        myspell-sk                           \
        myspell-sl                           \
        myspell-sv-se                        \
        myspell-th                           \
        myspell-uk



apt-get remove -y                             \
        xfonts-thai                           \
        xfonts-thai-etl                       \
        xfonts-thai-manop                     \
        xfonts-thai-nectec                    \
        xfonts-thai-poonlap                   \
        xfonts-thai-vor                       \
        wbrazilian                            \
        wbulgarian                            \
        wcatalan                              \
        wdanish                               \
        wdutch                                \
        wfrench                               \
        witalian                              \
        wngerman                              \
        wnorwegian                            \
        wpolish                               \
        wportuguese                           \
        wspanish                              \
        wswedish 

apt -y autoremove
