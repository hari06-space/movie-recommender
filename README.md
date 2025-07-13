# 🎬 Movie Recommendation System

A simple and effective **Movie Recommendation System** built using **Python**, **Pandas**, and **Scikit-learn**.  
It suggests movies similar to your favorite by analyzing genres, cast, and directors using **cosine similarity**.

---

## 🚀 Project Highlights

- ✅ Based on **IMDb Top 1000 Movies** dataset
- ✅ Uses **content-based filtering**
- ✅ Implemented with **CountVectorizer** + **Cosine Similarity**
- ✅ Simple CLI interface (takes user input)
- ✅ Beginner-friendly code, easy to understand

---

## 📁 Dataset

- 📌 Source: [IMDb Top 1000 Movies Dataset (Kaggle)](https://www.kaggle.com/datasets/ashirwadsangwan/imdb-top-1000-movies)
- File: `IMDb_Top_1000.csv`
- Features used: `Genre`, `Star1`, `Star2`, `Star3`, `Director`, `Series_Title`

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data manipulation |
| Scikit-learn | Vectorization & similarity |
| CountVectorizer | Convert text into vectors |
| Cosine Similarity | Measure movie similarity |

---

## 🧠 How It Works

1. Dataset is loaded and cleaned
2. Features like Genre, Cast, and Director are combined
3. Text is converted into vectors using CountVectorizer
4. Cosine similarity is calculated between all movies
5. Based on input, similar movies are recommended

---

## 💻 Run It Locally

### 1. Clone or Download the Project
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
