# SmartMed

Ce guide vous aide à activer le site web SmartMed en utilisant un environnement virtuel ou avec Docker Compose.

## Pré-requis
- Python installé sur votre machine  
- Pip (gestionnaire de paquets Python) installé  
- Docker et Docker Compose installés  

## Étapes pour Activer le Site

### Option 1 : Utiliser un Environnement Virtuel

#### 1. Créer un Environnement Virtuel  
Ouvrez votre terminal ou ligne de commande et exécutez la commande suivante pour créer un environnement virtuel :  

```sh
python -m venv env
```

#### 2. Activer l'Environnement Virtuel  
- **Sur Windows** :  
  ```sh
  env\Scripts\activate
  ```
- **Sur macOS et Linux** :  
  ```sh
  source env/bin/activate
  ```

#### 3. Naviguer vers le Dossier du Projet  
Changez de répertoire pour aller dans le dossier de projet :  

```sh
cd SmartMed
```

#### 4. Installer les Dépendances  
Installez toutes les dépendances listées dans le fichier `requirements.txt` :  

```sh
pip install -r requirements.txt
```

#### 5. Lancer le Serveur de Développement  
Pour démarrer le site web SmartMed :  

```sh
python manage.py runserver
```

le site devrait maintenant être accessible à l'adresse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) dans votre navigateur web.

### Option 2 : Utiliser Docker Compose

#### 1. Télécharger les Images Docker  

```sh
docker pull marwenbellili/nginx:latest
docker pull marwenbellili/smartmed:latest
```

#### 2. Créer un Fichier `docker-compose.yml`  
Ajoutez le contenu suivant dans un fichier `docker-compose.yml` :

```yaml
services:
  nginx:
    image: marwenbellili/nginx:latest  
    ports:
      - "80:80"
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/mediafiles
    depends_on:
      - smartmed
    restart: always
    deploy:
      resources:
        limits:
          memory: 4G        
        reservations:
          memory: 2G        

  smartmed:
    image: marwenbellili/smartmed:latest  
    command: sh -c "gunicorn SmartMed.wsgi:application --bind 0.0.0.0:8000"
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/mediafiles
    expose:
      - "8000"
    restart: always
    deploy:
      resources:
        limits:
          memory: 8G        
        reservations:
          memory: 4G        
    runtime: nvidia              
    environment:
      - NVIDIA_VISIBLE_DEVICES=all  

volumes:
  static_volume:
  media_volume:
```

#### 3. Démarrer les Conteneurs  
Lancez les services avec Docker Compose :

```sh
docker-compose up -d
```

Le site SmartMed devrait maintenant être accessible sur le **port 80** via votre navigateur !
