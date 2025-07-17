from flask import Flask, render_template, redirect, url_for, request, abort
import requests
from datetime import datetime

app = Flask(__name__)
API_KEY = "84ab1dfa4bef78418d9185402b63e99f"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/city", methods=["GET", "POST"])
def show_weather():
    if request.method == "POST":

        try:
            city_title = request.form.get("city").title()
            API_CALL = f"https://api.openweathermap.org/data/2.5/forecast?q={city_title}&appid={API_KEY}&units=metric"

            response = requests.get(API_CALL)
            weather_data = response.json()

            hourly_forecast = []
            for i in range(8):
                forecast = weather_data['list'][i]

                time_str = forecast['dt_txt']
                time_obj = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
                formatted_time = time_obj.strftime('%I:%M %p')

                hourly_forecast.append({
                    'time': formatted_time,
                    'temp': forecast['main']['temp'],
                    'description' : forecast['weather'][0]['description'],
                    'icon' : forecast['weather'][0]['icon']
                })

            return render_template("show_weather.html", 
                                   city=city_title, 
                                   hourly_forecast=hourly_forecast, current_forecast=hourly_forecast[0])
        
        except (ValueError, TypeError, KeyError):
            return render_template("error.html")
    
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)