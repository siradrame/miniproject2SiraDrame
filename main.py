# INF601 - Advanced Programming in Python
# Sira Drame
# Mini Project 2
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set font family (replace 'Arial' with an actual font you find available)
plt.rcParams['font.family'] = 'Arial'


def load_data(file_path='North America Restaurants.csv'):
    """Load the restaurant data from a CSV file."""
    return pd.read_csv(file_path, index_col=0)


def plot_restaurant_distribution_by_state(df):
    """Plot the distribution of restaurants by state."""
    state_counts = df['state'].value_counts()
    plt.figure(figsize=(12, 6))  # Adjust the figure size
    state_counts.plot(kind='bar')
    plt.title('Distribution of Restaurants by State', fontsize=16)
    plt.xlabel('State', fontsize=14)
    plt.ylabel('Number of Restaurants', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)

    # Ensure the charts directory exists
    os.makedirs('charts', exist_ok=True)
    plt.savefig('charts/restaurants_by_state.png')
    plt.show()


if __name__ == '__main__':
    restaurants = load_data()
    print(restaurants.columns)
    print(restaurants.head())
    plot_restaurant_distribution_by_state(restaurants)  # Generate and show the plot