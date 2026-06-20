# System zarządzania zadaniami domowymi

## Spis treści

1. Opis projektu
2. Funkcjonalności
3. Technologie
4. Instalacja
5. Uruchomienie aplikacji

## Opis projektu

Aplikacja internetowa stworzona w Django zgodnie ze wzorcem architektonicznym MVC. System umożliwia zarządzanie zadaniami domowymi przypisanymi do uczniów i przedmiotów.
<img width="1470" height="702" alt="Zrzut ekranu 2026-06-20 o 16 08 16" src="https://github.com/user-attachments/assets/4d22ab1a-25fe-4704-81f9-5dcd3400ebb0" />
<img width="1469" height="858" alt="Zrzut ekranu 2026-06-20 o 16 08 02" src="https://github.com/user-attachments/assets/69121fa1-72ca-474f-b29c-1b97d09849f1" />


## Funkcjonalności

* Wyświetlanie listy zadań
* Dodawanie nowych zadań
* Edycja istniejących zadań
* Usuwanie zadań
* Wyszukiwanie zadań po opisie
* Walidacja formularzy
* Panel administratora
* Relacje między modelami

## Modele

### Homework

* opis zadania
* termin wykonania
* status

### Subject

* nazwa przedmiotu

### Student

* imię
* nazwisko

## Technologie

* Python
* Django
* SQLite
* Bootstrap 5

## Instalacja

Utworzenie środowiska wirtualnego:

python3 -m venv venv

Aktywacja środowiska:

source venv/bin/activate

Instalacja zależności:

pip install -r requirements.txt

## Uruchomienie aplikacji

Migracje:

python manage.py migrate

Uruchomienie serwera:

python manage.py runserver

Aplikacja będzie dostępna pod adresem:

http://127.0.0.1:8000

Panel administratora:

http://127.0.0.1:8000/admin





