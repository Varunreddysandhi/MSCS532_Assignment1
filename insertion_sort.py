def insertion_sort_descending(values):
    """Sort a list in place from largest to smallest."""
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1

        while j >= 0 and values[j] < key:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = key

    return values


def run_tests():
    test_cases = [
        ([], []),
        ([7], [7]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([9, 6, 3], [9, 6, 3]),
        ([4, -2, 4, 0], [4, 4, 0, -2]),
        ([5, 5, 5], [5, 5, 5]),
    ]

    for number, (original, expected) in enumerate(test_cases, start=1):
        actual = insertion_sort_descending(original.copy())

        assert actual == expected, (
            f"Test {number} failed: expected {expected}, got {actual}"
        )

        print(f"Test {number} passed.")

    print("All 6 test cases passed.")


def main():
    numbers = [12, 5, 19, 3, 12, 8]
    print("Original list:", numbers)
    insertion_sort_descending(numbers)
    print("Sorted list:", numbers)


if __name__ == "__main__":
    run_tests()
    main()