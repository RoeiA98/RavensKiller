from flask import Flask, request, jsonify

app = Flask(__name__)
# app.run(host="127.0.0.1", port=8080, debug=True)

# Fake database (in memory for now)
leaderboard = {}


@app.route("/save_score", methods=["POST"])
def save_score():
    """Save player score to the leaderboard."""
    data = request.json
    username = data.get("username")
    score = data.get("score")

    if not username or score is None:
        return jsonify({"error": "Invalid data"}), 400

    # Update the leaderboard
    leaderboard[username] = max(leaderboard.get(username, 0), score)
    return jsonify({"message": "Score saved successfully!"})


@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    """Get the leaderboard as a sorted list."""
    sorted_leaderboard = sorted(
        leaderboard.items(), key=lambda x: x[1], reverse=True
    )
    return jsonify(sorted_leaderboard)


if __name__ == "__main__":
    app.run(debug=True)
