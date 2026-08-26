import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("zomato.csv")
print("Total rows and columns:", data.shape[0])

print(data.head(9))

print(data.columns.tolist())
print(data.isnull().sum())
print(data.dtypes)
print("\n")

data = data.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1)
data = data.dropna(subset='rate (out of 5)',)
datd = data.dropna(subset='avg cost (two people)')
print("\n")

print(data.head(9))
print(data.shape)
print(data.isnull().sum())

print('\n',data['rate (out of 5)'].describe())
print("\n")
print(data['avg cost (two people)'].describe())
print("\n")

data['avg cost (two people)'] = data['avg cost (two people)'].fillna(data['avg cost (two people)'].median())
print(data.isnull().sum())
print("\n")

area_ratings = data.groupby('area')['rate (out of 5)'].mean().sort_values(ascending=False).head(10)
print("\n",area_ratings)

plt.figure(figsize=(10, 6))
area_ratings.plot(kind='barh', color='steelblue')
plt.xlabel('Average Rating')
plt.ylabel('Area')
plt.title('Top 10 Areas in Bengaluru by Average Restaurant Rating')
plt.gca().invert_yaxis()  # highest rating at top
plt.tight_layout()
plt.savefig('top_areas_rating.png', dpi=150)
plt.show()

online_rating = data.groupby('online_order')['rate (out of 5)'].mean()
print(online_rating)

plt.figure(figsize=(6, 5))
online_rating.plot(kind='bar', color=['coral', 'steelblue'])
plt.xlabel('Online Order Available')
plt.ylabel('Average Rating')
plt.title('Average Rating: Online Order vs No Online Order')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('online_order_rating.png', dpi=150)
plt.show()

print("\n")
fav_cuisine = data['cuisines type'].str.split(', ').explode().value_counts().head(10)
print(fav_cuisine)  
print("\n")
top_cuisine = fav_cuisine.index.tolist()
print(top_cuisine)

plt.figure(figsize= (9,6))
fav_cuisine.plot(kind= 'barh', color = 'coral')
plt.xlabel('Number of restaurants')
plt.ylabel('Cuisine Type')
plt.title('Top 10 Cuisines ordered in Bengaluru')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top_10_cuisines.png', dpi = 150)
plt.show()

print("\n")
cuisine_rating = {}
for cuisine in top_cuisine:
    cnt = data['cuisines type'].str.contains(cuisine, na = False)
    avg_rating = data[cnt]['rate (out of 5)'].mean()
    cuisine_rating[cuisine] = avg_rating
    
cuisine_rating_seies = pd.Series(cuisine_rating).sort_values(ascending = False)
print(cuisine_rating_seies)

plt.figure(figsize = (9,7))
cuisine_rating_seies.plot(kind = 'barh', color = 'mediumpurple')
plt.xlabel('Average Rating')
plt.ylabel('Cuisine types')
plt.title('Average rating of top cuisines ordered in Bengaluru')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('avg_rating_of_cuisines.png', dpi = 150)
plt.show()

plt.figure(figsize = (9,7))
plt.scatter(data['avg cost (two people)'], data['rate (out of 5)'], alpha = 0.3, color = 'steelblue')
plt.xlabel('Average cost for 2 people')
plt.ylabel('Rating')
plt.title('Average cost vs rating for Bengaluru restaurants')
plt.tight_layout()
plt.savefig('cost_vs_rating_for_2_people')
plt.show()
