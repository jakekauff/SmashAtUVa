from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='css')

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/get-tournaments")
def get_tournaments():
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM tournament ")  # LIMIT 1000000")
    output = cursor_obj.fetchall()

    cursor_obj.execute("SELECT * FROM player ")
    player = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-tournaments.html", tournament=output, player=player)


@app.route("/tournament/<int:TourneyNum>")
def class_(TourneyNum):
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"SELECT * FROM tournament WHERE TourneyNum = {TourneyNum} LIMIT 1")
    tournament_info = cursor_obj.fetchone()

    cursor_obj.execute(f"SELECT ComputingID FROM player_attendance WHERE TourneyNum = {TourneyNum}")
    attendance = cursor_obj.fetchall()

    if tournament_info is None:
        return "Tournament not found"

    connection_obj.close()

    return render_template("tournament.html", tournament_info=tournament_info, attendance=attendance)#, users=users)
@app.route("/get-players")
def get_players():
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM player")  # LIMIT 1000000")
    output = cursor_obj.fetchall()

    characters = []
    info = []
    for i in output:
        thisInfo = []
        num = int(i[5])
        cursor_obj.execute(f"SELECT * FROM characters WHERE CharacterNumber = {num}")  # LIMIT 1000000")
        output2 = cursor_obj.fetchall()
        logo = output2[0][1].lower() + ".png"
        urlforthis = url_for('static', filename=logo)
        output2.append(urlforthis)
        thisInfo.append(i)
        thisInfo.append(output2)
        info.append(thisInfo)

        #print(thisInfo)
    connection_obj.close()
    #print(info)
    return render_template("get-players.html", player=info, characters=characters)


@app.route("/player/<string:PlayerID>")
def player_(PlayerID):
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"SELECT * FROM player WHERE ComputingID = \"{PlayerID}\" LIMIT 1")


    player_info = cursor_obj.fetchone()

    if player_info is None:
        return "player not found"

    cursor_obj.execute(f"SELECT TourneyNum FROM player_attendance WHERE ComputingID = \"{PlayerID}\"")
    attendance = cursor_obj.fetchall()

    cursor_obj.execute(f"SELECT * FROM game WHERE Winner = \"{PlayerID}\"")
    wins = cursor_obj.fetchall()

    cursor_obj.execute(f"SELECT * FROM game WHERE Loser = \"{PlayerID}\"")
    losses = cursor_obj.fetchall()

    cursor_obj.execute(f"SELECT * FROM characters WHERE CharacterNumber = ( SELECT CharacterNumber FROM player WHERE ComputingID = \"{PlayerID}\" )")
    characters = cursor_obj.fetchall()

    #cursor_obj.execute(f"SELECT * FROM tournament WHERE TourneyNum IN ( SELECT user_id FROM user_class_reln WHERE class_id = {tournament_info[0]} )")
    #users = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("player.html", player_info=player_info, attendance=attendance, wins=wins, losses=losses, characters=characters)#, users=users)

@app.route("/tournament/player/<string:PlayerID>")
def tournamentplayer_(PlayerID):
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"SELECT * FROM player WHERE ComputingID = \"{PlayerID}\" LIMIT 1")
    player_info = cursor_obj.fetchone()

    if player_info is None:
        return "player not found"

    #cursor_obj.execute(f"SELECT * FROM tournament WHERE TourneyNum IN ( SELECT user_id FROM user_class_reln WHERE class_id = {tournament_info[0]} )")
    #users = cursor_obj.fetchall()
    cursor_obj.execute(f"SELECT TourneyNum FROM player_attendance WHERE ComputingID = \"{PlayerID}\"")
    attendance = cursor_obj.fetchall()

    cursor_obj.execute(f"SELECT * FROM game WHERE Winner = \"{PlayerID}\"")
    wins = cursor_obj.fetchall()

    cursor_obj.execute(f"SELECT * FROM game WHERE Loser = \"{PlayerID}\"")
    losses = cursor_obj.fetchall()
    cursor_obj.execute(f"SELECT * FROM characters WHERE CharacterNumber = ( SELECT CharacterNumber FROM player WHERE ComputingID = \"{PlayerID}\")")
    characters = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("player.html", player_info=player_info, attendance=attendance, wins=wins, losses=losses, characters=characters)#, users=users)

@app.route("/get-games")
def get_games():
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM game ")  # LIMIT 1000000")
    output = cursor_obj.fetchall()

    cursor_obj.execute("SELECT * FROM player ")
    player = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-games.html", game=output, player=player)

@app.route("/character")
def character():
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM characters ")
    output = cursor_obj.fetchall()
    output2 = []
    for i in output:
        print(i)
        thisOutput = []
        thisOutput.append(i)

        logo = i[1].lower() + ".png"
        urlforthis = url_for('static', filename=logo)
        thisOutput.append(urlforthis)
        print(thisOutput)
        output2.append(thisOutput)
    print(output2)
    connection_obj.close()

    return render_template("character.html", character=output2)
@app.route("/game/<int:GameID>")
def game_(GameID):
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"SELECT * FROM game WHERE GameID = {GameID} LIMIT 1")
    game_info = cursor_obj.fetchone()

    if game_info is None:
        return "Tournament not found"


    connection_obj.close()

    return render_template("game.html", game_info=game_info)
@app.route("/player/game/<int:GameID>")
def playergame_(GameID):
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"SELECT * FROM game WHERE GameID = {GameID} LIMIT 1")
    game_info = cursor_obj.fetchone()

    if game_info is None:
        return "Tournament not found"

    connection_obj.close()

    return render_template("game.html", game_info=game_info)

@app.route("/about")
def get_about():
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM club_officer ORDER BY OfficerID DESC ")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("about.html", officer_info=output)

if __name__ == '__main__':
    app.run(debug=True)

