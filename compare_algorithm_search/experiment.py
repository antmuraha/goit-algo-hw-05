import timeit
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def read_file(filename: str):
    with open(f"compare_algorithm_search/data/{filename}.txt", "r") as file:
        # Read the entire contents of the file into a string
        file_content = file.read()
        return file_content


def run_experiment():
    article_1 = read_file("article_1")
    article_2 = read_file("article_2")
    texts = [(1, article_1), (2, article_2)]
    existing_substring = "прийма"
    fictional_substring = "Профілюванням"
    substrings = [(True, existing_substring), (False, fictional_substring)]
    results = []

    for substring in substrings:
        for text in texts:
            index = text[0]
            result_boyer_moore_time = timeit.timeit(
                lambda: boyer_moore_search(text[1], substring[1]), number=10)

            result_kmp_search_time = timeit.timeit(
                lambda: kmp_search(text[1], substring[1]), number=10)

            result_rabin_karp_time = timeit.timeit(
                lambda: rabin_karp_search(text[1], substring[1]), number=10)

            results.append([
                index,
                len(text[1]),
                substring,
                result_boyer_moore_time,
                result_kmp_search_time,
                result_rabin_karp_time,
            ])

    return results


def plot_results(results):
    algorithms = ['Boyer-Moore', 'KMP', 'Rabin-Karp']
    existing_times = [0, 0, 0]
    fictional_times = [0, 0, 0]

    # Aggregate times for each algorithm based on substring type
    for row in results:
        if row[2][0]:  # Existing substring
            for i, time in enumerate(row[3:6]):
                existing_times[i] += time / 2  # Average across articles
        else:  # Fictional substring
            for i, time in enumerate(row[3:6]):
                fictional_times[i] += time / 2  # Average across articles

    # Create bar chart
    x = np.arange(len(algorithms))  # the label locations
    width = 0.4  # the width of the bars

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, existing_times,
                    width, label='Existing Substring')
    rects2 = ax.bar(x + width/2, fictional_times,
                    width, label='Fictional Substring')

    ax.set_xlabel('Search Algorithms')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title(
        'Execution Time by Algorithm and Substring Type (average across articles)')
    ax.set_xticks(x)
    ax.set_xticklabels(algorithms)
    ax.legend()

    # Add values above the bars
    def add_labels(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.5f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    add_labels(rects1)
    add_labels(rects2)

    fig.tight_layout()
    plt.show()


def main():
    results = run_experiment()
    headers = [
        "Article №",
        "Text size",
        "Substring (exiting/fictional)",
        "Boyer-Moore (s)",
        "KMP (s)",
        "Rabin-Karp (s)"
    ]
    print("\nComparison of Search Algorithms:\n")
    print(tabulate(results, headers=headers, floatfmt=".6f"))
    plot_results(results)


if __name__ == "__main__":
    main()
