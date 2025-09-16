# Book Recommendation System

A simple book recommendation system built with Flask (Python), HTML, and CSS. It helps users discover popular books and get personalized suggestions.

<img width="1920" height="905" alt="Website Look" src="https://github.com/user-attachments/assets/e0eb55bd-c2f8-4604-8042-df07b625a65d" />

## Features
- Popularity-based recommendations
- Collaborative filtering
- Web interface for easy use

## Tech Structure
```
Book Recommendation System
│
├── Frontend
│   ├── HTML
│   └── CSS (static/style.css)
│
├── Backend
│   └── Python
│       └── Flask (Web Framework)
│
├── Recommendation Algorithms
│   ├── Popularity-based Recommender
│   └── Collaborative Filtering
│
├── Data Science Stack
│   ├── Jupyter Notebook (book_recommender_system.ipynb)
│   │   ├── pandas, numpy (Data Processing)
│   │   └── pickle (Model & Data Serialization)
│   └── CSV Data Files
│       ├── Dataset BRS/Books.csv
│       ├── Dataset BRS/Users.csv
│       └── Dataset BRS/Ratings.csv
│
├── Outputs
│   ├── top_50_df_final.csv (Popular Books Export)
│   ├── pivot.pkl, books.pkl, similarity_score.pkl (Serialized Models/Data)
│
└── Build & Run
    ├── Develop recommendation logic in Jupyter Notebook
    ├── Export processed data/models as .csv/.pkl
    ├── Use Flask to serve recommendations via web
    └── Display results with HTML/CSS frontend
```

## Getting Started
1. Clone the repository.
2. Install dependencies:  
   ```
   pip install -r requirements.txt
   ```
3. Run the app:  
   ```
   python app.py
   ```
4. Open your browser and go to `http://localhost:5000`.

## Data
- Place your book, user, and rating CSV files in the `Dataset BRS` folder.

## License
MIT
