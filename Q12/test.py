from colorama import Fore
from Q12_INSERTTEAMNUMBER import get_median

TEST_INPUT = [
    [1, 2, 3, 4, 5],
    [100, 78, 98, 1000, 30],
    [1, 2, 4, 10],
    [6, 11, 23, 10],
    [100, 10, 278, 7, 12, 3, 45, 689],
]
TEST_OUTPUT = [3, 98, 3, 10.5, 28.5]


def test_function():
    for inp, out in zip(TEST_INPUT, TEST_OUTPUT):
        res = get_median(inp)
        error_message = ("Expected {} from input value {}, but got {}.").format(
            out, inp, res
        )
        assert res == out, Fore.RED + error_message
    print(Fore.GREEN + "All tests passed!")


def main():
    test_function()


if __name__ == "__main__":
    main()
