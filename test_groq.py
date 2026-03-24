#!/usr/bin/env python3
"""
Test Groq API directly
"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def test_groq():
    print("Testing Groq API...")
    
    api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key:
        print("ERROR: No GROQ_API_KEY found")
        return False
    
    if api_key == 'your_groq_api_key_here':
        print("ERROR: Using placeholder key")
        return False
    
    try:
        client = Groq(api_key=api_key)
        
        print("Sending test message...")
        chat = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI Personal Growth Companion. Give short helpful advice about productivity, habits and motivation. Be encouraging and specific."
                },
                {
                    "role": "user",
                    "content": "Hello"
                }
            ]
        )
        
        response = chat.choices[0].message.content.strip()
        print(f"SUCCESS! Response: {response}")
        return True
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    test_groq()
