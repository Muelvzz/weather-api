from flask import Flask, render_template, redirect, url_for, request
import requests
import json

app = Flask(__name__)
API_KEY = "84ab1dfa4bef78418d9185402b63e99f"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/city", methods=["GET", "POST"])
def show_weather():
    if request.method == "POST":

        city_title = request.form.get("city")
        API_CALL = f"https://api.openweathermap.org/data/2.5/weather?q={city_title}&appid={API_KEY}"

        response = requests.get(API_CALL)
        weather_data = response.json()

        return render_template("show_weather.html", city = city_title, weather_data=weather_data)
    
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)