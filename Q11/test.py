from colorama import Fore
from Q11_INSERTTEAMNUMBER import calc

TEST_INPUT = [[5, 8, "+"], [5, 8, "-"], [1, 0, "*"], [100, 10, "/"], [5, 2, "/"]]
TEST_OUTPUT = [13, -3, 0, 10, 2]


def test_function():
    for inp, out in zip(TEST_INPUT, TEST_OUTPUT):
        res = calc(inp[0], inp[1], inp[2])
        error_message = (
            "Expected {} from input values ({}, {}, {}), but got {}."
        ).format(out, inp[0], inp[1], inp[2], res)
        assert res == out, Fore.RED + error_message
    print(Fore.GREEN + "All tests passed!")


def main():
    test_function()


if __name__ == "__main__":
    main()
