from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from CLASSES.class_game_flask import Game

# import pdb; pdb.set_trace()

app = Flask(__name__)
app.secret_key = "key"
app.permanent_session_lifetime = timedelta(minutes=50)

game = Game()
msg = "Start or Load a game to find that whore."


@app.route("/Bar")
def whore_bar():
    if not game.current_location:
        flash("Start or Load a game to enter the bar.")
        return redirect(url_for("main_menu"))
    return render_template("bar.html", name=game.player.name)


@app.route("/quit")
def quit_game():
    return render_template("quit.html")


@app.route("/", methods=["GET", "POST"])
def main_menu():
    if request.method == "POST":
        command = request.form["command"]
        if command == "Start New Game":
            game.new_game()
            return redirect(url_for("gameplay"))
        elif command == "Continue Previous Game":
            flash(game.load_file("auto_save"))
            if "auto_save" in game.show_saves():
                return redirect(url_for("gameplay"))
        elif command == "Load Game":
            return redirect(url_for("load_game"))
        elif command == "Save Game":
            return redirect(url_for("save_game"))
        elif command == "Quit Game":
            game.exit_game()
            return redirect(url_for("quit_game"))
    return render_template("main_menu.html")


@app.route("/Game", methods=["GET", "POST"])
def gameplay():
    if not game.current_location:
        flash(msg)
        return redirect(url_for("main_menu"))
    else:
        if request.method == "POST":
            command = request.form["command"]
            if command in ["items", "venues", "people"]:
                return redirect(url_for("location"))
            elif command in ["inventory", "stats", "skills"]:
                return redirect(url_for("player"))
            elif command == "Load Game":
                return redirect(url_for("load_game"))
            elif command == "Save Game":
                return redirect(url_for("save_game"))
            flash(game.run_game(command))

        return render_template("gameplay.html",
                               content=game.current_location.enter_message(),
                               location=game.current_location,
                               venues=game.venues
                               )


@app.route("/Location", methods=["GET", "POST"])
def location():
    if not game.current_location:
        flash(msg)
        return redirect(url_for("main_menu"))
    else:
        if request.method == "POST":
            command = request.form["command"]
            if command == "Load Game":
                return redirect(url_for("load_game"))
            elif command == "Save Game":
                return redirect(url_for("save_game"))
        return render_template("location.html",
                               name=game.current_location.name_reference,
                               description=game.current_location.description,
                               items_msg=game.current_location.show_items(),
                               items=game.current_location.items,
                               people_msg=game.current_location.show_people(),
                               people=game.current_location.people,
                               venues_msg=game.current_location.show_venues(),
                               venues=game.current_location.venues,
                               )


@app.route("/Player", methods=["GET", "POST"])
def player():
    if not game.current_location:
        flash(msg)
        return redirect(url_for("main_menu"))
    else:
        if request.method == "POST":
            command = request.form["command"]
            if command == "Load Game":
                return redirect(url_for("load_game"))
            elif command == "Save Game":
                return redirect(url_for("save_game"))
        return render_template("player.html",
                               name=game.player.name,
                               occupation=game.player.occupation,
                               story=game.player.my_story(),
                               inventory_msg=game.player.show_inventory(),
                               inventory=game.player.items,
                               stats=game.player.stats
                               )


@app.route("/<thing>", methods=["GET", "POST"])
def stats(thing):
    thing = thing.lower()
    if thing in game.items:
        return render_template("stats.html",
                               item=f"{thing}".title(),
                               description=game.items[f"{thing}"].show_self())
    elif thing in game.npcs:
        return render_template("stats.html",
                               item=f"{thing}".title(),
                               description=game.npcs[f"{thing}"].show_self())
    elif thing in game.venues:
        return render_template("stats.html",
                               item=f"{thing}".title(),
                               description=game.venues[f"{thing}"].show_self())


@app.route("/Save Game", methods=["GET", "POST"])
def save_game():
    if not game.current_location:
        flash("Start or Load a game to save a game...")
        return redirect(url_for("main_menu"))
    saved_games = game.show_saves()
    if request.method == "POST":
        save_name = request.form["command"].lower()
        flash(game.save_file(save_name))
    return render_template("save_game.html",
                           saved_games=saved_games,
                           i=len(saved_games)
                           )


@app.route("/Load Game", methods=["GET", "POST"])
def load_game():
    saved_games = game.show_saves()
    if request.method == "POST":
        load_name = request.form["command"].lower()
        flash(game.load_file(load_name))
        return redirect(url_for("gameplay"))
    return render_template("load_game.html",
                           saved_games=saved_games,
                           i=len(saved_games)
                           )


@app.route("/test", methods=["GET", "POST"])
def test():
    saved_games = game.show_saves()
    return render_template("test.html", content=saved_games)


if __name__ == "__main__":
    app.run(debug=True)
