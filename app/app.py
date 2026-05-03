from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def generate_itinerary(destination, days, budget, style):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"""Create a detailed {days}-day travel itinerary for {destination}.
Budget level: {budget}
Travel style: {style}
Format it day by day with morning, afternoon and evening activities."""

    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", 
                            headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]

@app.route("/", methods=["GET", "POST"])
def index():
    itinerary = None
    if request.method == "POST":
        destination = request.form.get("destination")
        days = request.form.get("days")
        budget = request.form.get("budget")
        style = request.form.get("style")
        itinerary = generate_itinerary(destination, days, budget, style)
    return render_template("index.html", itinerary=itinerary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)