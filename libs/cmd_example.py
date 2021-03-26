"""
https://pypi.org/project/Baker/
https://pypi.org/project/colorama/
https://overiq.com/pygments-tutorial/

python cmd_example.py --help
python cmd_example.py my_command_with_params --help
python cmd_example.py my_command
python cmd_example.py my_command_with_params --name foo
python cmd_example.py pretty_print
"""

import baker
import colorama
from colorama import Fore, Style
from pygments import formatters, lexers, highlight

colorama.init()


@baker.command
def my_command():
    """
    my command docs
    """
    print("my_command")


@baker.command
def my_command_with_params(name="", value=0):
    """
    my command with params docs
    """
    name = f"{Fore.RED}{name}{Style.RESET_ALL}"
    value = f"{Fore.BLUE}{value}{Style.RESET_ALL}"
    print(f"my_command_with_params name={name} value={value}")


@baker.command
def pretty_print():
    """
    sql code pretty print
    """
    lexer = lexers.PostgresLexer()
    formatter = formatters.TerminalFormatter()

    code = "SELECT * FROM TABLE users WHERE user_id = 1"

    print(highlight(code, lexer, formatter))


if __name__ == "__main__":
    baker.run()
