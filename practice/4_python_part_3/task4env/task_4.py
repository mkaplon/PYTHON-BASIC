"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
from faker import Faker
from unittest.mock import Mock, patch

def print_name_address(args: argparse.Namespace) -> None:
    fake = Faker()
    args = vars(args)
    for _ in range(args['NUMBER']):
        my_dict = dict()
        for key in args:
            if key!='NUMBER':
                my_dict[key] = eval(f'fake.{args[key]}()')
        print(my_dict)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Define dicts")
    parser.add_argument("NUMBER", type=int)
    values = parser.parse_known_args()[1]
    for el in values:
        el2 = el.split('=')
        parser.add_argument(el2[0], default=el2[1])
    args = parser.parse_args()
    print_name_address(args)

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""

@patch('faker.providers.address.Provider.address', return_value="62323 Hobbs Green\nMaryshire, WY 48636")
@patch('faker.providers.person.Provider.name', return_value="Chad Baird")
@patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(NUMBER=1, imie="name", adres="address"))
def test_print_name_address(mock_args, mock_name, mock_address, capfd):
    args = argparse.ArgumentParser().parse_args()
    print_name_address(args)
    out, err = capfd.readouterr()
    assert out == "{'imie': 'Chad Baird', 'adres': '62323 Hobbs Green\\nMaryshire, WY 48636'}\n"