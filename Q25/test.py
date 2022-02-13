from colorama import Fore
from Q25_INSERTTEAMNUMBER import number_transform

TEST_INPUT = [0, 1, 10, 11, 1000]
TEST_OUTPUT = [0, 4, 5, 34, 500]


def test_function():
    for inp, out in zip(TEST_INPUT, TEST_OUTPUT):
        res = number_transform(inp)
        error_message = ("Expected {} from input value {}, but got {}.").format(
            out, inp, res
        )
        assert res == out, Fore.RED + error_message
    print(Fore.GREEN + "All tests passed!")


def main():
    test_function()


if __name__ == "__main__":
    main()
