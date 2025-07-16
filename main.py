from flask import Flask, render_template, redirect, url_for, request, abort
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

        try:
            city_title = request.form.get("city").capitalize()
            API_CALL = f"https://api.openweathermap.org/data/2.5/weather?q={city_title}&appid={API_KEY}&units=metric"

            response = requests.get(API_CALL)
            weather_data = response.json()

            longitude = weather_data["coord"]["lon"]
            latitude = weather_data["coord"]["lat"]
            description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]

            return render_template("show_weather.html", city=city_title,lon=longitude,lat=latitude,des=description,temp=temperature)
        
        except (ValueError, TypeError, KeyError):
            return render_template("error.html")
    
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)