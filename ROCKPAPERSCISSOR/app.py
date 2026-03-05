from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ["rock","paper","scissor"]

@app.route("/", methods=["GET","POST"])
def game():

    result = ""
    computer = ""
    player = ""

    if request.method == "POST":

        player = request.form["choice"]
        computer = random.choice(choices)

        if player == computer:
            result = "Draw"

        elif(
            (player=="rock" and computer=="scissor") or
            (player=="scissor" and computer=="paper") or
            (player=="paper" and computer=="rock")
        ):
            result = "You Win"

        else:
            result = "Computer Wins"

    return render_template("index.html",result=result,computer=computer,player=player)

if __name__ == "__main__":
    app.run(debug=True)