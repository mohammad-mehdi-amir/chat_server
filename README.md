# 🗨️ Real-time Chat Application

This is a real-time chat application built with **Django**, **Django Channels**, and **WebSockets**, allowing multiple users to communicate live. Users can see each other's online status, and the app fully supports dark mode styling using Bootstrap.

---

## 🚀 Features

- Real-time messaging (WebSocket-based)
- Online users list updated dynamically
- User-friendly interface 
- Automatic removal of users from the online list when disconnected
- **Activity logs saved to a local file (`chat_log.txt`)**

---

## ⚙️ Technologies Used

- Python 3.11+
- Django 5.x
- Django Channels
- Channels Redis
- Bootstrap 5

---

## 💡 How It Works

1️⃣ Users first enter their **username** on the home page.  
2️⃣ After clicking "Join Chat", they are redirected to the chat room.  
3️⃣ The username is used for both messages and online users list.  
4️⃣ When a user disconnects (closes the page), their name is automatically removed from the list.
5️⃣ **All user activities (joining, leaving, sending messages) are saved to `chat_log.txt` with timestamps.**

---

## 🛠️ Installation

Clone the repository

```bash
git clone <your-repo-url>
cd project_2
```
Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Make sure you have Redis installed and running:
```bash
brew install redis
brew services start redis
# or simply
redis-server
```

⚡ Run the server
```bash
python manage.py migrate
python manage.py runserver
```
🌐 Access the app

Go to http://127.0.0.1:8000/ and enter a username to start chatting!

🛡️ License

This project is open-source and free to use.









