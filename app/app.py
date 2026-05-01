import os
from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    itinerary = None
    if request.method == "POST":
        destination = request.form["destination"]
        days = request.form["days"]
        budget = request.form["budget"]
        style = request.form["style"]

        prompt = f"""
        Create a detailed {days}-day travel itinerary for {destination}.
        Budget: {budget}
        Travel style: {style}
        
        Format each day as:
        Day X:
        Morning: ...
        Afternoon: ...
        Evening: ...
        Food tip: ...
        """

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        itinerary = response.choices[0].message.content

    return render_template("index.html", itinerary=itinerary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)