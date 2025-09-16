from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
app = Flask(__name__)

# Load CSV for popular based recommendation engine
books_df = pd.read_csv("./top_50_df_final.csv")
books_df["avg_ratings"] = books_df["avg_ratings"].round(2)

# files for recommendation engine
pivot = pickle.load(open('pivot.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))

# recommendation engine
def book_recommendation(book_name):
    #index fetch
    index = np.where(pivot.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key = lambda x: x[1], reverse=True)[1:6]
    recommended_books = []
    for item in (similar_items):
        data = []
        temp_df = books[books['Book-Title'] == pivot.index[item[0]]]
        data.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        data.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        data.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        recommended_books.append(data)
    return recommended_books


@app.route('/')
def index():
    # Pick top 10 books by num_ratings
    top_books = books_df.sort_values("num_ratings", ascending=False).head(10).to_dict(orient="records")
    return render_template('index.html', books=top_books)

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=["POST"]) # get method
def recommend():
    user_input = request.form.get('user_input')
    rb = book_recommendation(user_input)
    return render_template('recommend.html', data=rb)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)