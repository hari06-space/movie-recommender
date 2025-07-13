import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("IMDb_Top_1000.csv")
df.dropna(inplace=True)

# Combine text features
def combine_features(row):
    return f"{row['Genre']} {row['Star1']} {row['Star2']} {row['Star3']} {row['Director']}"

df['combined'] = df.apply(combine_features, axis=1)

# Vectorize
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['combined']).toarray()

similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie_name):
    movie_name = movie_name.lower()
    if movie_name not in df['Series_Title'].str.lower().values:
        print("❌ Movie not found in database.")
        return
    
    index = df[df['Series_Title'].str.lower() == movie_name].index[0]
    distances = list(enumerate(similarity[index]))
    similar_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    
    print(f"\n🎬 Movies similar to '{df.iloc[index]['Series_Title']}':")
    for i in similar_movies:
        print(f"✅ {df.iloc[i[0]]['Series_Title']}")

# Take input
movie = input("Enter a movie name: ")
recommend(movie)
