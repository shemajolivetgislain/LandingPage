# LandingPage

## Step 1: Create virtual Environments

python3 -m venv en

## Step 2: Activate virtual Environment

<!-- In Linux -->
source ./env/bin/activate

<!-- in Windows -->
source ./env/scripts/activate.bat

## Step 3: install packages from requirements

pip install requirements.txt


## Step 4: run migrations
python manage.py migrate

## Step 5: Create Super User Account
python manage.py createsuperuser

## step6: run server
python manage.py runserver


## step7: urls navigations

<!-- for admin site -->
-http://127.0.0.1:8000/admin
-http://127.0.0.1:8000/api/v1/about/
-http://127.0.0.1:8000/api/v1/mission/
-http://127.0.0.1:8000/api/v1/vision/
-http://127.0.0.1:8000/api/v1/objective/
