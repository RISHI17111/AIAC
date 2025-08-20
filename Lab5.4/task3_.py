# Simple product recommendation based on user search history

# Sample product categories and recommendations
product_recommendations = {
    "soap": ["Shampoo", "Body Wash", "Hand Sanitizer"],
    "mobile": ["Mobile Case", "Screen Protector", "Earphones"],
    "toys": ["Board Games", "Action Figures", "Puzzles"],
    "games": ["Game Console", "Video Games", "Game Accessories"],
}

def recommend_products(search_term):
    search_term = search_term.lower()
    if search_term in product_recommendations:
        print(f"Based on your search for '{search_term}', you might also like:")
        for item in product_recommendations[search_term]:
            print(f"- {item}")
    else:
        print("Sorry, we have no recommendations for that search term.")

def main():
    search_term = input("Enter a product you searched for: ")
    recommend_products(search_term)

if __name__ == "__main__":
    main()