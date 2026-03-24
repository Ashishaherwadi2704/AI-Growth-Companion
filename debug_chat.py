#!/usr/bin/env python3
"""
Debug chat endpoint to find exact error
"""

import requests
import json

def test_chat_endpoint():
    print("Testing chat endpoint...")
    
    # First, let's test if the app is actually running
    try:
        response = requests.get('http://localhost:5000/api-status')
        if response.status_code == 200:
            print("App is running")
            print(f"API Status: {response.json()}")
        else:
            print(f"App not responding properly: {response.status_code}")
            return
    except Exception as e:
        print(f"Cannot connect to app: {e}")
        print("Make sure the app is running with: python app.py")
        return
    
    # Test without authentication (should fail with 401 or 302)
    try:
        response = requests.post(
            'http://localhost:5000/chat',
            json={'message': 'Hello'},
            headers={'Content-Type': 'application/json'},
            allow_redirects=False
        )
        print(f"\nWithout auth - Status: {response.status_code}")
        if response.status_code != 401 and response.status_code != 302:
            print(f"Unexpected response: {response.text}")
        else:
            print("Correctly rejected unauthenticated request")
    except Exception as e:
        print(f"Request failed: {e}")
    
    print("\n" + "="*50)
    print("DIAGNOSIS:")
    print("1. If you see 'App is running' above, your API is working")
    print("2. The error 'Sorry, I'm having trouble connecting' means:")
    print("   - You're not logged into the web app")
    print("   - OR there's a session/authentication issue")
    print("3. SOLUTION: Go to http://localhost:5000/login and login properly")

if __name__ == "__main__":
    test_chat_endpoint()
