from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from CLASSES.class_game_flask import Game

# import pdb; pdb.set_trace()

app = Flask(__name__)
app.secret_key = "whore"
app.permanent_session_lifetime = timedelta(seconds=30)

game = Game()


@app.route("/", methods=["GET", "POST"])
def main_menu():
    if request.method == "POST":
        session.permanent = True
        command = request.form["command"]
        game.start_menu(command)
        session["name"] = game.player.name
        return redirect(url_for("gameplay"))
    return render_template("main_menu.html")


@app.route("/Game", methods=["GET", "POST"])
def gameplay():
    if not game.current_location:
        return redirect(url_for("main_menu"))
    else:
        if request.method == "POST":
            command = request.form["command"]
            flash(game.run_game(command))
        return render_template("gameplay.html", content=game.current_location.enter_message())


@app.route("/Location")
def location():
    if not game.current_location:
        return redirect(url_for("main_menu"))
    else:
        return render_template("location.html", name=game.current_location.name_reference)


@app.route("/Player")
def player():
    if not game.current_location:
        return redirect(url_for("main_menu"))
    else:
        return render_template("player.html", name=game.player.name,
                               occupation=game.player.occupation,
                               story=game.player.my_story(),
                               )


if __name__ == "__main__":
    app.run(debug=True)
