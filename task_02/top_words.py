import string
import requests
import matplotlib.pyplot as plt
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor


def load_text(url):
    """Load text from URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise Exception(f"Failed to download text from {url}: {e}")


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def mapper(word):
    return word, 1


def shuffle(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()


def reducer(key_values):
    key, values = key_values
    return key, sum(values)


def map_reduce(text):
    text = remove_punctuation(text)
    words = text.split()

    with ThreadPoolExecutor() as executor:
        mapped_values = list(executor.map(mapper, words))

    shuffled_values = shuffle(mapped_values)

    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reducer, shuffled_values))

    return dict(reduced_values)


def visualize_top_words(word_counts, top_n=10):
    """Visualize top words by frequency"""
    try:
        sorted_word_counts = sorted(
            word_counts.items(), key=lambda x: x[1], reverse=True
        )[:top_n]
        words, counts = zip(*sorted_word_counts)

        plt.figure(figsize=(10, 5))

        plt.barh(words, counts)

        plt.xlabel("Frequency")

        plt.ylabel("Words")

        plt.title("Top 10 Most Frequent Words\nEDWARD CARPENTER: MY DAYS AND DREAMS")

        plt.xticks(rotation=15)
        plt.yticks(rotation=15)

        plt.gca().invert_yaxis()

        plt.tight_layout()

        plt.show()

    except Exception as e:
        raise Exception(f"Error occurred while visualizing top words: {e}")


def main(url):
    try:
        text = load_text(url)
        if text:
            result = map_reduce(text)

            visualize_top_words(result)

    except Exception as e:
        raise Exception(f"Error occurred in main function: {e}")


if __name__ == "__main__":
    url = "https://www.gutenberg.org/cache/epub/78612/pg78612.txt"

    main(url)