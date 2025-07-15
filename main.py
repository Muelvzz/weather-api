from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/city", methods=["GET", "POST"])
def show_weather():
    if request.method == "POST":
        city_title = request.form.get("city")
        return render_template("show_weather.html", city = city_title)
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)