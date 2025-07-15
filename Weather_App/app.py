from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"https://wttr.in/{city}?format=j1"

        try:
            response = requests.get(url)
            data = response.json()

            weather = {
                "location": city.title(),
                "temp_C": data['current_condition'][0]['temp_C'],
                "desc": data['current_condition'][0]['weatherDesc'][0]['value'],
                "humidity": data['current_condition'][0]['humidity'],
                "wind_kmph": data['current_condition'][0]['windspeedKmph']
            }

        except Exception as e:
            print("Error:", e)
            error = "❌ Weather data not found. Try a different city."

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)