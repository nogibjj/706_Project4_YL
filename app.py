from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

movies_df = pd.read_csv("movie.csv", on_bad_lines="skip")

@app.route("/")
def index():
    return "Welcome to MovieRec"

@app.route("/recommend", methods=["GET"])
def recommend():
    title = request.args.get("Movie_Title")
    director = request.args.get("Director")
    column, query = ("Movie_Title", title) if title else ("Director", director)

    if query:
        recommended_movies = movies_df[
            movies_df[column].str.contains(query, case=False, na=False, regex=False)
        ].head(5)
        return jsonify(recommended_movies.to_dict(orient="records"))
    
    error_msg = "Please provide a movie title or a director's name for recommendation"

    return jsonify({"error": error_msg}), 400

if __name__ == "__main__":
    app.run(debug=True)