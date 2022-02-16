Mejorando proyectos pasados.  
Ahora con
- django-rest-framework para las apis de comuniacion.  
- bootstrap para el frontend.  



Proyectos incluidos actualmente:
- [Psicometrica](https://github.com/Ojitos369/psicometria) - (Construyendo...)  
  

## Capturas
![apis](./img/apis.png)
![main](./img/index.png)
![test 1](./img/test_1.png)
![test 1 2](./img/test_1_2.png)
![preguntas](./img/preguntas.png)

Para probarlo:  
- Instalar las dependencias:  
    ```
    pip install -r requirements.txt
    ```
- Crea el archivo:  
    ```
    ojitos369/ojitos369/mysecret.py
    ```
    y agrega la variable SECRET_KEY  

- Para agregar los datos a la db:  
    en `python manage.py shell`  
    ejecuta los scripts de `db_info/db_scripts.py`  

- Arreglar rest framework swagger:  
    en `./venv/lib64/python3.8/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html`  
    en la linea 2 cambia  
    `{% load staticfiles %}`  
    por  
    `{% load static %}`  