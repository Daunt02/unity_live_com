#[unity-live.com](https://unity-live.com) | [dash](https://unity-live.com/dashboard/) | [docs](https://unity-live.com/dashboard/docs/) | [repo](https://github.com/nerdfiles/unity_live_com) | [reqs](unity_live_com/blob/master/.requirements) | [lic](unity_live_com/blob/master/LICENSE)

This repo contains development code for http://unity-live.com, Jah Jah G., 
a Houston-based artist, musician, traveler.

##Install

    $ pyenv install 2.7.6
    $ pyenv local 2.7.6
    $ pyenv virtualenv unity_live_com
    $ pip install -r .requirements
    $ python manage.py syncdb --all
    $ python manage.py collectstatic
    $ python manage.py runserver

###Precautions

This stack’s .requirements do not work in Python3-land. Minimal testing done 
with pyenv across a few Pythons (2.7.7 and 3.4.0).

##Project

1. https://trello.com/b/sHauBCcP/unity-live-com

##TODO

1. Run analytics on CSS to reduce payload, redundancy (poorly used ``@mixins``),  
   and unused selectors.
2. http://unity-live.com/static/imagestore/c9c63061-48a4-4a28-9f19-9fcac24599e1.jpg  
   Fix ``urls.py`` and workflow for generating static resources.
