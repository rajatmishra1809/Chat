# app.py
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client (Replace with your API key)
client = OpenAI(api_key='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')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    try:
        # Create chat completion with OpenAI's new API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        
        # Extract the AI's response
        ai_response = response.choices[0].message.content
        
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
