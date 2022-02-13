from colorama import Fore
from Q5_INSERTTEAMNUMBER import average_of_list

TEST_INPUT = [
    [],
    [1, 2, 3, 4, 5],
    [-4, 5, 10, 11],
    [71, 2000, 12, 789, 2, -189],
    [1, 2, 3, 4, 190, 18, 14, -912, 2, 3, 4, 5, 67],
    [
        1,
        123,
        90,
        28,
        2991,
        29,
        48,
        10,
        2000,
        2,
        223,
        70,
        89,
        192,
        -10000,
        20,
        211,
        343,
        23100,
        2,
        21,
        431,
        1,
        2,
        3,
        144,
        13,
        231,
        103,
        145,
    ],
]
TEST_OUTPUT = [0, 3, 5, 447, -47, 688]


def test_function():
    for inp, out in zip(TEST_INPUT, TEST_OUTPUT):
        res = average_of_list(inp)
        error_message = ("Expected {} from input value {}, but got {}.").format(
            out, inp, res
        )
        assert res == out, Fore.RED + error_message
    print(Fore.GREEN + "All tests passed!")


def main():
    test_function()


if __name__ == "__main__":
    main()
