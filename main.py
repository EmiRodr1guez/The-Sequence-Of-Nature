from flask import Flask, render_template, request
import requests
import smtplib
import numpy as np
from scipy.fft import *
from scipy.io import wavfile
# from matplotlib import pyplot as plt

# USE YOUR OWN n-point LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
EMAIL_PW = "fsvpycyanhuwfvfi"
EMAIL = "phantomdanny9@gmail.com"
app = Flask(__name__)


# This is the function that is called to analyze the frequency of the given song
def freq(file, start_time, end_time):

    # Open the file and convert to mono
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass

    # Return a slice of the data from start_time to end_time
    dataToRead = data[int(start_time * sr / 1000): int(end_time * sr / 1000) + 1]

    # Fourier Transform
    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)

    # Uncomment these to see the frequency spectrum as a plot
    # plt.plot(xf, np.abs(yf))
    # plt.show()

    # Get the most dominant frequency and return it
    idx = np.argmax(np.abs(yf)) # type: ignore
    computed_freq = xf[idx]
    return computed_freq




# Home/Main page route, ideally where the song will be uploaded
@app.route("/", methods=["GET", "POST"])
def get_all_posts() -> str:
    if request.method == "POST":
        # Handle the form submission here, and call the freq function
        computed_freq = freq(file=request.files["wav_file"], start_time=0, end_time=3)
        return render_template("result.html", computed_freq=computed_freq)
    return render_template("index.html", all_posts=posts)

# Route for about page
@app.route("/about")
def about() -> str:
    return render_template("about.html")

# A route for a contact page if we'll implement this feature
@app.route("/contact", methods=["GET", "POST"])
def contact() -> str:
    if request.method == "GET":
        return render_template("contact.html", message="Contact Me")
    else:
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", message="Successfully sent your message!")

# Function to contact developers through email
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, EMAIL_PW)
        connection.sendmail(from_addr=email, to_addrs=EMAIL, msg=email_message)

# Flask server instantiation
if __name__ == "__main__":
    app.run(debug=True, port=5001)