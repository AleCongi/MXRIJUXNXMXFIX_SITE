 
### Instruction:

1. Install your venv
```
    python -m venv venv
```

2. Activate your venv
```
    venv\Scripts\activate
```

3. Install dependencies
```
    pip install -r requirements.txt
```

4. Run the server
``` 
    python manage.py runserver
```

EXTRA: 
Every time you modify models, you need to migrate them 
```
    python manage.py makemigrations --merge
    python manage.py migrate
```



You can access to the application in the same network with the ip of your pc and the port    
```
    python manage.py YOURIP:8000 runserver
```