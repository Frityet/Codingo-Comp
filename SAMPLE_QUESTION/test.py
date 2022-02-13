from colorama import Fore
from sample import add_one

TEST_INPUT = [1, 2, -4, 5]
TEST_OUTPUT = [2, 3, -3, 6]


def test_function():
    for inp, out in zip(TEST_INPUT, TEST_OUTPUT):
        res = add_one(inp)
        error_message = (
            "Expected {} with input value {}, but got {}."
        ).format(out, inp, res)
        assert res == out, Fore.RED + error_message
    print(Fore.GREEN + "All tests passed!")


def main():
    test_function()


if __name__ == "__main__":
    main()
