from flask import Flask, redirect, url_for

app = Flask(__name__)
a = True
@app.route("/")
def home():
  return '<h1>Graphic novel analysis in Maus.<h1> <font size="-1">Graphic novels are the most flexible storytelling form. They must present us with well crafted and light shining text, for the art is too descriptive of the surroundings for the emotion to remain unexplored. They must present us with stunning, and demonstrating visuals, for time must be created for dialogue.</font>'

@app.route("/<name>")
def user(name):
  return f"leave {name}"

@app.route("/admin")
def admin():
  if a:
    return 'nice'
  return redirect(url_for("home"))

@app.route("/menu")
def menu():
  return "just kidding we dont have lobster."
if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = 8000)
