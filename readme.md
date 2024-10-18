
# Attendance management

### Windows

#### 1. Clone the repository:
```bash
git clone https://github.com/ratnapalshende/asm.git
cd asm
```

#### 2. Create a virtual environment:
```bash
python -m venv venv
```

#### 3. Activate the virtual environment:
```bash
venv\Scripts\activate
```

#### 4. Install the dependencies:
```bash
pip install -r requirements.txt
```

#### 5. Set up the Django project:
- Make migrations:
  ```bash
  python manage.py makemigrations
  ```
- Apply migrations:
  ```bash
  python manage.py migrate
  ```

#### 6. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

#### 7. Run the development server:
```bash
python manage.py runserver
```

The project should now be running on [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Linux

#### 1. Clone the repository:
```bash
git clone https://github.com/ratnapalshende/asm.git
cd asm
```

#### 2. Create a virtual environment:
```bash
python3 -m venv venv
```

#### 3. Activate the virtual environment:
```bash
source venv/bin/activate
```

#### 4. Install the dependencies:
```bash
pip install -r requirements.txt
```

#### 5. Set up the Django project:
- Make migrations:
  ```bash
  python manage.py makemigrations
  ```
- Apply migrations:
  ```bash
  python manage.py migrate
  ```

#### 6. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

#### 7. Run the development server:
```bash
python manage.py runserver
```

The project should now be running on [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

Feel free to adjust the repository link, project description, and any specific instructions as needed!
