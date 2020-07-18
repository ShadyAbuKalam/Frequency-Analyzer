from frequency_analyzer import ArabicAlphaFrequencyAnalyzer


if __name__ == "__main__":
    file_path = "Quran" #Not provided in the repository.
    print("Analyzing file {0}".format(file_path))
    file = open(file_path, 'r', encoding='UTF-8')
    freq_analyzer = ArabicAlphaFrequencyAnalyzer()

    for line in file.readlines():
        freq_analyzer.process_text(line)
    total_chars_counted,statistics = freq_analyzer.compute_statistics()
    print("Total chars count {0}".format(total_chars_counted))

    # Print the statistics sorted in a descending order
    d_view = [(v, k) for k, v in statistics.items()]
    d_view.sort(reverse=True)  # natively sort tuples by first element
    for v,k in d_view:
        print("{0} : {1}".format(k,v))
