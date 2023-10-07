 
### Istruzioni:
1. Installare un ambiente virtuale dentro la cartella del progetto
```
    python -m venv venv
```
2. Attivare l'ambiente virtuale (controllare di essere nella cartella giusta)
```
    cd .\MangaDB\
```
```
    venv\Scripts\activate
```

3. Avviare il server
``` 
    python manage.py runserver
```

EXTRA: 
! Ricordarsi di effettuare le migrazioni (nel caso di aggiornamenti al db)
(senza --merge la prima volta)
```
    ./manage.py makemigrations --merge 
    python manage.py migrate
```

! Ricordarsi di installare le librerie e dipendenze necessarie !
```
    pip install -r requirements.txt
```
Avviare il server per la visione da altri dispositivi connessi alla stessa rete
    Inserire il proprio IP in ALLOWED_HOSTS nel file settings.py (MangaDB\MangaDB\settings.py)    
```
    python manage.py TUOIP:8000 runserver
```