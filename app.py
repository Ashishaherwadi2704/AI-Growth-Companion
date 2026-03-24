# # from flask import Flask, request, jsonify, render_template
# # import sqlite3
# # from datetime import datetime
# # from google import genai

# # app = Flask(__name__)

# # # ------------------ GEMINI SETUP ------------------
# # client = genai.Client(api_key="AIzaSyD0HqNbfa1dMZmtaMpOekE5hh5VRYlWVfQ")

# # # ------------------ DATABASE ------------------
# # def init_db():
# #     conn = sqlite3.connect('database.db')
# #     c = conn.cursor()

# #     c.execute('''
# #     CREATE TABLE IF NOT EXISTS chat_history (
# #         chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         user_message TEXT,
# #         bot_response TEXT,
# #         timestamp DATETIME
# #     )
# #     ''')

# #     conn.commit()
# #     conn.close()

# # init_db()

# # # ------------------ AI RESPONSE ------------------
# # def generate_response(user_input):
# #     try:
# #         response = client.models.generate_content(
# #             model="gemini-2.0-flash",  # ✅ latest working model
# #             contents=f"""
# # You are an AI Personal Growth Companion.

# # Rules:
# # - Give short (2–3 lines) helpful advice
# # - Focus on goals, habits, productivity, motivation
# # - If unrelated, gently guide back to self-improvement

# # User: {user_input}
# # """
# #         )

# #         # Safe response handling
# #         if hasattr(response, "text") and response.text:
# #             return response.text.strip()
# #         else:
# #             return "Try asking about goals, habits, or productivity."

# #     except Exception as e:
# #         print("ERROR:", e)
# #         return f"Error: {str(e)}"

# # # ------------------ ROUTES ------------------
# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# # @app.route('/chat', methods=['POST'])
# # def chat():
# #     user_input = request.json['message']
# #     print("User:", user_input)

# #     response = generate_response(user_input)
# #     print("Bot:", response)

# #     # Save chat
# #     conn = sqlite3.connect('database.db')
# #     c = conn.cursor()
# #     c.execute(
# #         "INSERT INTO chat_history (user_message, bot_response, timestamp) VALUES (?, ?, ?)",
# #         (user_input, response, datetime.now())
# #     )
# #     conn.commit()
# #     conn.close()

# #     return jsonify({'response': response})

# # # ------------------ RUN ------------------
# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
# import bcrypt
# from flask import Flask, redirect, request, jsonify, render_template
# import sqlite3
# from datetime import datetime
# from groq import Groq

# app = Flask(__name__)
# app.secret_key = "mysecretkey123"

# # ------------------ LOGIN MANAGER SETUP ---------
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

# # ------------------ USER SETUP ------------------
# class User(UserMixin):
#     def __init__(self, id):
#         self.id = id
# @login_manager.user_loader
# def load_user(user_id):
#     return User(user_id)

# # ------------------ GROQ SETUP ------------------

# # ------------------ DATABASE ------------------
# # def init_db():
# #     conn = sqlite3.connect('database.db')
# #     c = conn.cursor()

# #     c.execute('''
# #     CREATE TABLE IF NOT EXISTS chat_history (
# #         chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         user_message TEXT,
# #         bot_response TEXT,
# #         timestamp DATETIME
# #     )
# #     ''')

# #     conn.commit()
# #     conn.close()

# # init_db()
# # def init_db():
# #     conn = sqlite3.connect('database.db')
# #     c = conn.cursor()

# #     # Users table
# #     c.execute('''
# #     CREATE TABLE IF NOT EXISTS users (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         username TEXT UNIQUE,
# #         password TEXT
# #     )
# #     ''')

# #     # Chat history
# #     c.execute('''
# #     CREATE TABLE IF NOT EXISTS chat_history (
# #         chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         user_id INTEGER,
# #         user_message TEXT,
# #         bot_response TEXT,
# #         timestamp DATETIME
# #     )
# #     ''')

# #     conn.commit()
# #     conn.close()

# # # ------------------ AI RESPONSE ------------------
# # def generate_response(user_input):
# #     try:
# #         chat = client.chat.completions.create(
# #             model="llama-3.1-8b-instant",
# #             messages=[
# #                 {
# #                     "role": "system",
# #                     "content": "You are an AI Personal Growth Companion. Give short helpful advice about productivity, habits, and motivation."
# #                 },
# #                 {
# #                     "role": "user",
# #                     "content": user_input
# #                 }
# #             ]
# #         )

# #         return chat.choices[0].message.content.strip()

# #     except Exception as e:
# #         print("ERROR:", e)
# #         return f"Error: {str(e)}"
# def init_db():
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()

#     # USERS TABLE
#     c.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE,
#         password TEXT
#     )
#     ''')

#     # CHAT HISTORY TABLE
#     c.execute('''
#     CREATE TABLE IF NOT EXISTS chat_history (
#         chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER,
#         user_message TEXT,
#         bot_response TEXT,
#         timestamp DATETIME
#     )
#     ''')

#     conn.commit()
#     conn.close()

# # ------------------ ROUTES ------------------
# @app.route('/register', methods=['GET','POST'])
# def register():

#     if request.method == "POST":

#         username = request.form['username']
#         password = request.form['password']

#         hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#         conn = sqlite3.connect('database.db')
#         c = conn.cursor()

#         c.execute("INSERT INTO users (username,password) VALUES (?,?)",
#                   (username, hashed))

#         conn.commit()
#         conn.close()

#         return "User registered successfully"

#     return render_template("register.html")

# @app.route('/login', methods=['GET','POST'])
# def login():

#     if request.method == "POST":

#         username = request.form['username']
#         password = request.form['password']

#         conn = sqlite3.connect('database.db')
#         c = conn.cursor()

#         c.execute("SELECT id,password FROM users WHERE username=?",(username,))
#         user = c.fetchone()

#         conn.close()

#         if user and bcrypt.checkpw(password.encode('utf-8'), user[1]):

#             login_user(User(user[0]))
#             return redirect("/")

#         return "Invalid login"

#     return render_template("login.html")

# @app.route('/')
# @login_required
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json['message']
#     print("User:", user_input)

#     response = generate_response(user_input)
#     print("Bot:", response)

#     # Save chat
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
#     c.execute(
#     "INSERT INTO chat_history (user_id, user_message, bot_response, timestamp) VALUES (?, ?, ?, ?)",
#     (current_user.id, user_input, response, datetime.now().isoformat())
# )
#     conn.commit()
#     conn.close()

#     return jsonify({'response': response})

# @app.route('/history')
# @login_required
# def history():

#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()

#     c.execute("SELECT user_message,bot_response FROM chat_history WHERE user_id=?",
#               (current_user.id,))

#     chats = c.fetchall()

#     conn.close()

#     return jsonify(chats)

# # ------------------ RUN ------------------
# if __name__ == '__main__':
#     app.run(debug=True)

# _______________________________________Main__________________________________________
from flask import Flask, request, jsonify, render_template, redirect, session
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
import sqlite3
import bcrypt
from datetime import datetime
import os
import re
import logging
from groq import Groq

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Session configuration for automatic logout
from datetime import timedelta
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)  # 1 hour session
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# ------------------ LOGGING ------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ------------------ LOGIN MANAGER ------------------

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# ------------------ USER CLASS ------------------

class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# ------------------ AI PROVIDERS ------------------

class AIProvider:
    def __init__(self):
        self.groq_client = None
        
        if Config.GROQ_API_KEY and Config.GROQ_API_KEY != 'your_groq_api_key_here' and Config.GROQ_API_KEY.startswith('gsk_'):
            try:
                self.groq_client = Groq(api_key=Config.GROQ_API_KEY)
                logger.info("Groq client initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Groq client: {e}")
        else:
            logger.warning("Groq API key not configured or invalid format")
            
        # Log status
        if not self.groq_client:
            logger.error("Groq provider not configured! Please set up GROQ_API_KEY in .env file")
    
    def generate_response(self, user_input):
        """Generate response using Groq"""
        
        logger.info(f"AIProvider.generate_response called with input: {user_input[:100]}...")
        
        # Validate input
        if not user_input or len(user_input.strip()) == 0:
            logger.warning("Empty input received")
            return "Please tell me what's on your mind."
            
        if len(user_input) > Config.MAX_MESSAGE_LENGTH:
            logger.warning(f"Input too long: {len(user_input)} chars")
            return "Your message is quite long! Could you be more brief?"
        
        # Check if client exists
        if not self.groq_client:
            logger.error("Groq client not initialized!")
            return "AI service not configured. Please check your API key."
        
        # Use Groq
        try:
            logger.info("Making Groq API request...")
            chat = self.groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an AI Personal Growth Companion. Give short helpful advice about productivity, habits and motivation. Be encouraging and specific."
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )
            response = chat.choices[0].message.content.strip()
            logger.info(f"Groq API successful: {response[:100]}...")
            return response
        except Exception as e:
            logger.error(f"Groq API failed: {type(e).__name__}: {str(e)}", exc_info=True)
            error_str = str(e).lower()
            
            if "429" in error_str or "rate" in error_str:
                return "Rate limit exceeded. Please wait a moment before trying again."
            elif "quota" in error_str or "exceeded" in error_str:
                return "API quota exceeded. Please check your Groq account."
            elif "connection" in error_str or "network" in error_str:
                return "Connection error. Please check your internet and try again."
            elif "authentication" in error_str or "unauthorized" in error_str:
                return "API authentication failed. Please check your API key."
            else:
                logger.error(f"Returning generic error: {str(e)}")
                return "Sorry, I'm having trouble connecting right now. Please try again!"

ai_provider = AIProvider()

# ------------------ CONFIGURATION CHECK ------------------

@app.route('/api-status')
def api_status():
    """Check API configuration status"""
    status = {
        'groq': {
            'configured': bool(Config.GROQ_API_KEY and Config.GROQ_API_KEY != 'your_groq_api_key_here'),
            'valid_format': bool(Config.GROQ_API_KEY and Config.GROQ_API_KEY.startswith('gsk_')),
            'client_initialized': bool(ai_provider.groq_client)
        }
    }
    return jsonify(status)


# ------------------ DATABASE ------------------

def init_db():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # USERS TABLE
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password BLOB
    )
    ''')

    # CHAT HISTORY
    c.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        user_message TEXT,
        bot_response TEXT,
        timestamp DATETIME
    )
    ''')

    conn.commit()
    conn.close()


init_db()


# ------------------ AI RESPONSE ------------------

def generate_response(user_input):
    return ai_provider.generate_response(user_input)


# ------------------ REGISTER ------------------

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        # Validation
        if not username or len(username) < 3:
            return "Username must be at least 3 characters"
            
        if not password or len(password) < 6:
            return "Password must be at least 6 characters"
            
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return "Username can only contain letters, numbers, and underscores"

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        try:

            c.execute(
                "INSERT INTO users (username,password) VALUES (?,?)",
                (username, hashed)
            )

            conn.commit()

        except:
            return "Username already exists"

        conn.close()

        return redirect("/login")

    return render_template("register.html")


# ------------------ LOGIN ------------------

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        # Basic validation
        if not username or not password:
            return "Please enter both username and password"

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute(
            "SELECT id,password FROM users WHERE username=?",
            (username,)
        )

        user = c.fetchone()

        conn.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[1]):

            login_user(User(user[0]))
            return redirect("/")

        return "Invalid login"

    return render_template("login.html")


# ------------------ LOGOUT ------------------

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    
    # Handle beacon requests differently
    if request.method == 'POST' and request.form.get('logout') == 'true':
        return '', 200  # Return empty response for beacon requests
    
    return redirect("/login")


# ------------------ HOME ------------------

@app.route('/')
@login_required
def home():

    return render_template("index.html")


# ------------------ CHAT API ------------------

@app.route('/chat', methods=['POST'])
@login_required
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            logger.error("Chat error: No message in request")
            return jsonify({'error': 'Message is required'}), 400
            
        user_input = data['message'].strip()
        
        if not user_input:
            logger.error("Chat error: Empty message")
            return jsonify({'error': 'Message cannot be empty'}), 400
            
        if len(user_input) > Config.MAX_MESSAGE_LENGTH:
            logger.error(f"Chat error: Message too long ({len(user_input)} chars)")
            return jsonify({'error': f'Message too long (max {Config.MAX_MESSAGE_LENGTH} characters)'}), 400

        logger.info(f"User {current_user.id}: {user_input[:50]}...")

        response = generate_response(user_input)
        logger.info(f"Bot response: {response[:50]}...")
        
        # Check if response indicates error
        if "trouble connecting" in response or "not configured" in response:
            logger.error(f"AI Provider Error: {response}")
            return jsonify({'error': 'AI service unavailable', 'details': response}), 503

        # Save to database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO chat_history (user_id, user_message, bot_response, timestamp) VALUES (?, ?, ?, ?)",
            (current_user.id, user_input, response, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()

        return jsonify({'response': response})
        
    except Exception as e:
        logger.error(f"Chat endpoint error: {str(e)}", exc_info=True)
        return jsonify({'error': 'Something went wrong. Please try again.', 'details': str(e)}), 500


# ------------------ CHAT HISTORY ------------------

@app.route('/history')
@login_required
def history():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Get paginated history
        page = request.args.get('page', 1, type=int)
        per_page = 20
        offset = (page - 1) * per_page
        
        c.execute("""
            SELECT user_message, bot_response, timestamp 
            FROM chat_history 
            WHERE user_id = ?
            ORDER BY timestamp DESC 
            LIMIT ? OFFSET ?
        """, (current_user.id, per_page, offset))
        
        chats = c.fetchall()
        
        # Get total count
        c.execute("SELECT COUNT(*) FROM chat_history WHERE user_id = ?", (current_user.id,))
        total = c.fetchone()[0]
        
        conn.close()
        
        return jsonify({
            'chats': [{'user': msg, 'bot': resp, 'time': ts} for msg, resp, ts in chats],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'pages': (total + per_page - 1) // per_page
            }
        })
        
    except Exception as e:
        logger.error(f"History error: {e}")
        return jsonify({'error': 'Could not load history'}), 500


# ------------------ RUN SERVER ------------------

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)