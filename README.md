
# 🔐 Login & Registration Form – MERN Stack

A responsive user **Registration and Login** (Sign Up / Sign In) form built with the **MERN stack** — MongoDB, Express, React, and Node.js. Styled with **Bootstrap**.

![Login Screenshot](https://github.com/AkshataGanbote/Registration_Login_Form_MERN_Stack/assets/117456092/442bbe2d-cda7-4d5c-a156-9e9cc9b3f108)
![Register Screenshot](https://github.com/AkshataGanbote/Registration_Login_Form_MERN_Stack/assets/117456092/01b04452-4e8b-4a24-b680-28c93f2c7550)

---

## ✅ Features

- User registration with validations
- Login with authentication
- Update and delete account features
- Responsive UI using Bootstrap
- Full-stack integration using REST APIs
- Automated tests using Selenium + Pytest

---

## ⚙️ Prerequisites

Before running the project, make sure the following are installed:

- [Node.js](https://nodejs.org/en/download)
- [MongoDB](https://www.mongodb.com/try/download/community) (See installation instructions below)
- [Python 3.x](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/) (for Selenium tests)
- [pip](https://pip.pypa.io/en/stable/installation/) for installing Python packages

---

## ⚙️ Test Plan Document
Test docs can be found at following path 

- backend/docs/test_plan.pdf
---

## 📦 Project Setup

### 🖼 Frontend

```bash
cd frontend
npm install
npm run dev
```

Visit: [http://localhost:5173](http://localhost:5173)

---

### 🛠 Backend

```bash
cd backend
npm install
npm start
```

API runs on: `http://localhost:3000`

---

## Swagger
http://127.0.0.1:3001/api-docs

### 🍃 MongoDB Setup

MongoDB is required to run the backend.

#### Option 1: Use the included setup script (macOS/Linux)
```bash
./start_backend_with_mongo.sh
```

#### Option 2: Manual Installation

- **macOS** (Homebrew)
  ```bash
  brew tap mongodb/brew
  brew install mongodb-community
  brew services start mongodb/brew/mongodb-community
  ```

- **Ubuntu/Debian**
  ```bash
  sudo apt update
  sudo apt install -y mongodb
  sudo systemctl start mongodb
  ```

- MongoDB official installation guide: [https://www.mongodb.com/docs/manual/installation/](https://www.mongodb.com/docs/manual/installation/)


- **start mangodb**
  ```bash
  brew services start mongodb-community@7.0
  ```
- **stop mangodb**
  ```bash
  brew services stop mongodb-community@7.0
  ```

---

## 🧪 Running Automated Tests

### 1. Set up the Python virtual environment (only once)
```bash
python3 -m venv selenium-venv
source selenium-venv/bin/activate
pip install -r tests/requirements.txt ( Run the requirements.txt file by following the path backend/tests/requirements.txt)
```

### 2. Run Frontend & Backend (MongoDB must be running)
Make sure both are running before tests:

```bash
# In one terminal
cd frontend
npm run dev

# In another terminal
cd backend
npm start
```

### 3. Run All Tests

Go to the following path and run the pytest files : 
git/QA_Project/frontend and git/QA_Project/backend and run the below pytest command to run all the testcases

```bash
pytest -v tests/
```

---

## 🛠️ Tech Stack

| Tech        | Role          |
|-------------|---------------|
| React       | Frontend UI   |
| React Router| Page routing  |
| Bootstrap   | Styling       |
| Node.js     | Backend runtime |
| Express.js  | API framework |
| MongoDB     | NoSQL database |
| Selenium    | Test automation |
| Pytest      | Test framework |

---

## 🎉 You're all set!

Once MongoDB is running, and the frontend and backend are up, open [http://localhost:5173](http://localhost:5173) in your browser to use the app.

By
Manogna Nadimpalli
