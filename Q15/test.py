from colorama import Fore
from Q15_INSERTTEAMNUMBER import two_sum

TEST_INPUT = [
    [[2, 7, 11, 15], 9],
    [[3, 2, 4], 6],
    [[3, 3], 6],
    [[1, 0, 0, 1, 0, 1, 1, 1, 0], 1],
    [[7, 8, 9, 10, 11], 21],
    [[9, 3, 6], 9],
]
TEST_OUTPUT = [
    [2, 7],
    [2, 4],
    [3, 3],
    [0, 1],
    [10, 11],
    [3, 6],
]


def test_function():
    for inp, out in zip(TEST_INPUT, TEST_OUTPUT):
        res = two_sum(inp[0], inp[1])
        error_message = (
            "Expected {} from input array {} and target {}, but got {}."
        ).format(out, inp[0], inp[1], res)
        assert res == out, Fore.RED + error_message
    print(Fore.GREEN + "All tests passed!")


def main():
    test_function()


if __name__ == "__main__":
    main()
