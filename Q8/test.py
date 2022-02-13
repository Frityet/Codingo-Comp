from colorama import Fore
from Q8_INSERTTEAMNUMBER import morse_code_translator

TEST_INPUT = ["SOS", "Hello World", "The quick brown fox jumped over the lazy dog"]
TEST_OUTPUT = [
    "... --- ...",
    ".... . .-.. .-.. --- / .-- --- .-. .-.. -..",
    "- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. . -.. / --- ...- . .-. / - .... . / .-.. .- --.. -.-- / -.. --- --.",
]


def test_function():
    for inp, out in zip(TEST_INPUT, TEST_OUTPUT):
        res = morse_code_translator(inp)
        error_message = ("Expected {} from input value {}, but got {}.").format(
            out, inp, res
        )
        assert res == out, Fore.RED + error_message
    print(Fore.GREEN + "All tests passed!")


def main():
    test_function()


if __name__ == "__main__":
    main()
