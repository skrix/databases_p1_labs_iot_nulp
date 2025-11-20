# Sixt Car Rental API

Flask REST API for car rental management system with MySQL database.

## Setup

1. **Create virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
```

4. **Initialize database**
```bash
mysql -u root -p < database.sql
```

5. **Run application**
```bash
python app.py
```

API available at: **http://localhost:5000**
