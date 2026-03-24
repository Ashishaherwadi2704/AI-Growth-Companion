#!/usr/bin/env python3
"""
Setup Checker for AI Growth Companion
Run this script to verify your configuration
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """Check environment variables"""
    print("Checking Environment Configuration...\n")
    
    load_dotenv()
    
    # Check required files
    required_files = ['.env', 'config.py', 'app.py']
    for file in required_files:
        if os.path.exists(file):
            print(f"[OK] {file} exists")
        else:
            print(f"[ERROR] {file} missing")
    
    print("\nChecking API Keys...")
    
    groq_key = os.getenv('GROQ_API_KEY')
    secret_key = os.getenv('FLASK_SECRET_KEY')
    
    # Check Groq
    if groq_key:
        if groq_key == 'your_groq_api_key_here':
            print("[ERROR] Groq: Using placeholder key")
        elif groq_key.startswith('gsk_'):
            print(f"[OK] Groq: Valid format key (gsk_...{groq_key[-6:]})")
        else:
            print("[ERROR] Groq: Invalid key format (should start with 'gsk_')")
    else:
        print("[ERROR] Groq: No API key found")
    
    # Check Secret Key
    if secret_key:
        if secret_key == 'dev-secret-key-change-in-production':
            print("[WARN] Secret: Using development key (change for production)")
        elif len(secret_key) >= 32:
            print(f"[OK] Secret: Valid length ({len(secret_key)} chars)")
        else:
            print("[ERROR] Secret: Too short (should be at least 32 chars)")
    else:
        print("[ERROR] Secret: No secret key found")
    
    return bool(groq_key and groq_key.startswith('gsk_'))

def check_dependencies():
    """Check Python dependencies"""
    print("\nChecking Dependencies...")
    
    required_packages = [
        'flask',
        'flask_login', 
        'bcrypt',
        'groq',
        'python_dotenv'
    ]
    
    missing = []
    for package in required_packages:
        try:
            if package == 'flask_login':
                import flask_login
            elif package == 'python_dotenv':
                import dotenv
            else:
                __import__(package)
            print(f"[OK] {package}")
        except ImportError:
            print(f"[ERROR] {package} - MISSING")
            missing.append(package)
    
    if missing:
        print(f"\n[WARN] Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    return True

def generate_secret_key():
    """Generate a secure secret key"""
    import secrets
    return secrets.token_hex(32)

def main():
    print("AI Growth Companion Setup Checker\n")
    
    env_ok = check_environment()
    deps_ok = check_dependencies()
    
    print("\n" + "="*50)
    
    if env_ok and deps_ok:
        print("[OK] Setup looks good! Your app should work.")
        print("\nStart your app with: python app.py")
    else:
        print("[ERROR] Setup issues found. Please fix them above.")
        
        if not env_ok:
            print("\nTo fix environment issues:")
            print("1. Get API key from https://console.groq.com")
            print("2. Update your .env file with real API key")
            print("3. Generate a secret key:")
            print(f"   FLASK_SECRET_KEY={generate_secret_key()}")
        
        if not deps_ok:
            print("\nTo install dependencies:")
            print("pip install -r requirements.txt")
    
    print("\nFor detailed help, see: setup_guide.md")

if __name__ == "__main__":
    main()
