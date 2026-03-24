# 🤖 AI Growth Companion

A modern web application for personal growth and productivity, powered by AI. Features a beautiful chat interface with conversation history and multiple AI provider support.

## ✨ Features

- **Modern UI/UX**: Clean, responsive design with smooth animations
- **Multiple AI Providers**: Support for Groq API with automatic fallback handling
- **Chat History**: Paginated conversation history with sidebar view
- **Real-time Features**: Typing indicators, character count, toast notifications
- **Security**: User authentication, input validation, secure password hashing
- **Keyboard Shortcuts**: Ctrl+H for history, Enter to send, Escape to close sidebar
- **Error Handling**: Graceful API error handling with user-friendly messages
- **Mobile Responsive**: Works perfectly on desktop and mobile devices
- **Automatic Logout**: Secure session management with page close detection

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Groq API key (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ashishaherwadi2704/AI-Growth-Companion.git
   cd "AI Growth Companion"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API key:
   ```env
   GROQ_API_KEY=gsk_your_groq_api_key_here
   FLASK_SECRET_KEY=your_random_secret_key_here_32_chars
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the app**
   Open http://localhost:5000 in your browser

### Get API Keys

1. **Groq (Recommended)**
   - Sign up at https://console.groq.com
   - Get your API key from the dashboard
   - Free tier: 30 requests/minute

## 📁 Project Structure

```
AI Growth Companion/
├── app.py              # Main Flask application
├── config.py           # Configuration management
├── .env.example         # Environment variables template
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .gitignore         # Git ignore rules
├── static/            # Static assets
│   ├── style.css      # Modern CSS with variables
│   └── script.js      # ES6+ JavaScript
└── templates/         # HTML templates
    ├── index.html     # Main chat interface
    ├── login.html     # Login page
    └── register.html  # Registration page
```

## 🎨 UI Features

- **Modern Design**: Clean interface with smooth animations and transitions
- **Dark Mode Ready**: CSS variables for easy theming
- **Responsive Layout**: Adapts to all screen sizes
- **Interactive Elements**: Hover effects, loading states, micro-interactions
- **Accessibility**: Semantic HTML, keyboard navigation, ARIA labels

## 🔒 Security Features

- **Password Hashing**: bcrypt with salt for secure password storage
- **Input Validation**: Server-side validation for all user inputs
- **XSS Protection**: HTML escaping for user-generated content
- **CSRF Protection**: Built-in Flask CSRF protection
- **Session Management**: Secure session handling with Flask-Login
- **Automatic Logout**: Page close detection for session cleanup

## 🤖 AI Integration

### Supported Providers
1. **Groq** (Primary)
   - Model: `llama-3.1-8b-instant`
   - Fast responses, good free tier
   - Automatic retry on errors

### Error Handling
- Automatic provider fallbacks
- Graceful degradation on API errors
- Rate limit detection and handling
- User-friendly error messages

## 📱 Usage

1. **Register/Login**: Create an account or sign in
2. **Chat**: Type messages and get AI responses
3. **History**: View past conversations with the history button
4. **Keyboard Shortcuts**: 
   - `Enter`: Send message
   - `Ctrl+H`: Toggle history sidebar
   - `Escape`: Close sidebar

## 🛠️ Development

### Running in Development Mode
```bash
export FLASK_ENV=development
python app.py
```

### Database Management
View chat history:
```bash
python view_history.py
```

### Adding New Features
- Add new routes in `app.py`
- Update templates in `templates/`
- Modify styles in `static/style.css`
- Extend JavaScript in `static/script.js`

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Check `.env` file configuration
   - Verify API key validity
   - Check API quota limits

2. **Database Issues**
   - Delete `database.db` to reset
   - Check file permissions

3. **Import Errors**
   - Run `pip install -r requirements.txt`
   - Check Python version (3.8+)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For issues and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the API documentation for your chosen provider

---

Built with ❤️ using Flask, modern JavaScript, and AI APIs
