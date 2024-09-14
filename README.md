# 1. Create virtual environment

python3 -m venv .venv

# 2. Activate virtual environment

. .venv/bin/activate

# 3. Install dependencies

pip install -r requirements.txt

# 4. Run server

python3 manage.py runserver 0.0.0.0:8000
