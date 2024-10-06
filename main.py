# INF601 - Advanced Programming in Python
# Sira Drame
# Mini Project 2
import pandas as pd
import matplotlib.pyplot as plt
import os


def load_data(file_path='North America Restaurants.csv'):
    """Load the restaurant data from a CSV file."""
    return pd.read_csv(file_path, index_col=0, parse_dates=True)


def plot_restaurant_counts(df):
    """Plot the number of restaurants by cuisine type."""
    # Count the occurrences of each cuisine type
    counts = df['cuisines'].value_counts()  # Update to use the 'cuisines' column
    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar')
    plt.title('Number of Restaurants by Cuisine Type')
    plt.xlabel('Cuisine Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Ensure the charts directory exists
    os.makedirs('charts', exist_ok=True)
    plt.savefig('charts/restaurant_counts.png')
    plt.show()


if __name__ == '__main__':
    restaurants = load_data()  # Load the data
    print(restaurants.columns)  # Print the column names to check
    print(restaurants.head())  # Print the first few rows of the DataFrame
    plot_restaurant_counts(restaurants)  # Generate and show the plot
