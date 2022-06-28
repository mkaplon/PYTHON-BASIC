from string import ascii_lowercase
from stock_info import sheet_creator, get_max_cols

example_data = {"Name": ["A", "B"],
                "Surname": ["Test1", "Test2"],
                "Age": ["20", "30"]}

example_data2 = {"Name" : [el for el in ascii_lowercase[:25]],
            "Number" : [str(num) for num in range(25)]}


def test_sheet_creator(capfd):
    sheet_creator("example sheet", example_data)
    out, err = capfd.readouterr()
    assert out == "==== example sheet ====\n| Name | Surname | Age |\n------------------------\n| A    | Test1   | 20  |\n| B    | Test2   | 30  |\n"

def test_get_max_cols():
    example_input = get_max_cols(example_data2, "Number", 2, "Example title")
    expected_output = {"Name": ["y", "x"], "Number" : ["24", "23"]}
    assert example_input == expected_output
