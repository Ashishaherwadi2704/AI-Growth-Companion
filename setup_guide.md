# 🚀 Quick Setup Guide

## Issue: "Sorry, I'm having trouble connecting right now. Please try again!"

This error means the AI APIs aren't configured. Follow these steps:

### 1. Get API Keys

#### Option A: Groq (Recommended - Better Free Tier)
1. Go to https://console.groq.com
2. Sign up for a free account
3. Go to API Keys in the dashboard
4. Create a new API key
5. Copy the key (starts with `gsk_`)

#### Option B: Gemini (Alternative)
1. Go to https://ai.google.dev
2. Sign up for Google AI Studio
3. Create an API key
4. Copy the key (starts with `AIza`)

### 2. Configure Environment

1. Open the `.env` file in your project root
2. Replace the placeholder values:

```env
# Replace with your actual API keys
GROQ_API_KEY=gsk_your_actual_groq_key_here
GEMINI_API_KEY=AIzaSy_your_actual_gemini_key_here

# Generate a random secret key
FLASK_SECRET_KEY=your_random_32_character_secret_key_here
```

### 3. Generate Secret Key

Run this Python command to generate a secure secret key:

```python
import secrets
print(secrets.token_hex(32))
```

Copy the output and paste it as your `FLASK_SECRET_KEY`.

### 4. Restart the Application

```bash
# Stop the current server (Ctrl+C)
# Then restart:
python app.py
```

### 5. Test the Connection

1. Go to http://localhost:5000
2. Try sending a message like "Hello"
3. You should get a proper AI response

## 🔍 Troubleshooting

### Still Getting Errors?

1. **Check API Key Format**:
   - Groq keys start with `gsk_`
   - Gemini keys start with `AIza`

2. **Verify API Key Validity**:
   - Make sure you copied the entire key
   - Check for extra spaces or characters

3. **Check API Quotas**:
   - Groq: Check your dashboard for usage limits
   - Gemini: Free tier has daily limits

4. **Test API Key Manually**:

#### Test Groq:
```bash
curl -X POST "https://api.groq.com/openai/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.1-8b-instant",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

#### Test Gemini:
```bash
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=YOUR_GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "Hello"}]}]
  }'
```

### Common Issues

| Error | Solution |
|-------|----------|
| `429 Resource Exhausted` | API quota exceeded. Wait or upgrade plan |
| `401 Unauthorized` | Invalid API key. Check your key |
| `Connection Error` | Internet connectivity issue |
| `Import Error` | Missing dependencies. Run `pip install -r requirements.txt` |

### Debug Mode

To see detailed error messages, check the console where you're running the app. You should see logs like:

```
INFO:groq_client:Groq client initialized
WARNING:groq_client:Groq API failed: 429 Resource Exhausted
INFO:app:User 1: Hello...
```

## 📞 Need Help?

1. Check the console output for specific error messages
2. Verify your API keys are correct
3. Make sure you have internet connection
4. Try both API providers (Groq and Gemini)

## ✅ Success Checklist

- [ ] API key copied correctly
- [ ] `.env` file updated
- [ ] Secret key generated
- [ ] Application restarted
- [ ] Test message works

Once configured, your AI Growth Companion will work perfectly!
