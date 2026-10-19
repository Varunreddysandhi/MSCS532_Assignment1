def insertion_sort_descending(values):
    """Sort a list in place from largest to smallest."""
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1

        # Shift smaller elements one position to the right.
        while j >= 0 and values[j] < key:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = key

    return values


def main():
    numbers = [12, 5, 19, 3, 12, 8]

    print("Original list:", numbers)
    insertion_sort_descending(numbers)
    print("Sorted list:", numbers)


if __name__ == "__main__":
    main()