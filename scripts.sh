#!/bin/bash

npm run dev
python manage.py runserver_plus --cert-file /home/msche/koshka/ssl/koshka.pem --key-file /home/msche/koshka/ssl/private.pem 0.0.0.0:8000