import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitilize"""

def test_capitilize():

    """Позитивные проверки"""

    assert utils.capitilize("privet") == "Privet"
    assert utils.capitilize("privet petr") == "Privet petr"
    assert utils.capitilize("0236040") == "0236040"
    assert utils.capitilize("privet, petr") == "Privet, petr"
    assert utils.capitilize("privet! Petr") == "Privet! Petr"

    """Негативные проверки"""

    assert utils.capitilize("...") == "..."
    assert utils.capitilize("   ") == "   "
    assert utils.capitilize("023petr023") == "023petr023"
    assert utils.capitilize("!petr023") == "!petr023"


"""trim"""

def test_trim():

    """Позитивные проверки"""

    assert utils.trim(" privet petr") == "privet petr"
    assert utils.trim("   privet petr") == "privet petr"
    assert utils.trim("   !privet petr") == "privet petr"
    assert utils.trim("     123privet petr") == "123privet petr"
    assert utils.trim("  Privet petr") == "Privet petr"
    assert utils.trim("  123 petr") == "123 petr"

    """Негативные проверки"""

    assert utils.trim("") == ""


    """to_list"""

    @pytest.mark.parametrize('string, delimeter, result',
[
        
        ("Петр, Дима, Маша", ",", ["Петр", "Дима", "Маша"]),
        ("5,6,7,8,9,10", "," ["5", "6", "7","8","9","10"]),
        ("!@?@:@$", "@", ["!","?",":","$"]),
       
        ("", None, []),
        ("1","2","5","9 9"), None, ["1","2","5","9 9"],
    ])
    def test_to_list(string, delimeter, result):
        if delimeter is None:
            res = utils.to_list(string)
        else:
            res = utils.to_list(string, delimeter)
        assert res == result


    
    """contains"""

    @pytest.mark.parametrize('string, symbol, result', [
        ("Петр", "П", True),
        ("Ирина", "Ы", False),
        ("Телевизор", "л", True),
        ("Белград", "д", True),
        ("Яблоко", "й", False),
        ("", "", True),
        ("", "1", False),
        ("Петр", "!", False),
        ("023", "2", True),
        ("321", "П", False),
        ("Петр", "п", False),
        ("Петр", "1", False),

    ])
    def test_contains(string, symbol, result):
        res = utils.contains(string, symbol)
        assert res == result


        """delete_symbol"""


@pytest.mark.parametrize('string, symbol, result', [
        ("Петр", "П", "етр"),
        ("Ирина", "р", "Иина"),
        ("Телевизор", "л", "Теевизор"),
        ("Белград", "д", "Белгра"),
        ("Яблоко", "б", "Ялоко"),
        ("023", "0", "23"),
        ("Столица Сербии", "", "СтолицаСербии"),

        ("Петр", "", "Петр"),
        ("", "", ""),
        ("", "0", ""),
        ("Петр", "?", "Петр"),
        ("Петр", "ё", ),

    ])
def test_delete_symbol(string, symbol, result):
        res = utils.delete_symbol(string, symbol)
        assert res == result


"""starts_with"""




@pytest.mark.parametrize('string, symbol, result', [
     
        ("Петр", "П", True),
        ("Телевизор", "Т", True),
        ("", "", True),
        ("023", "0", True),
        ("SkyPro", "S", True),

        ("321", "П", False),
        ("Петр", "п", False),
        ("Петр", "1", False),
        ("Петр", "g", False),
        ("Петр", "?", False),

    ])
def test_starts_with(string, symbol, result):
        res = utils.starts_with(string, symbol)
        assert res == result


"""end_with"""



@pytest.mark.parametrize('string, symbol, result', [
     
        ("Петр", "р", True),
        ("Телевизор", "р", True),
        ("", "", True),
        ("023", "3", True),
        ("SkyPro", "о", True),

        ("321", "П", False),
        ("Петр", "п", False),
        ("Петр", "1", False),
        ("Петр", "g", False),
        ("Петр", "?", False),
        ("", ";", False),

    ])
def test_end_with(string, symbol, result):
        res = utils.end_with(string, symbol)
        assert res == result



"""is_empty"""


@pytest.mark.parametrize('string, result')[
     
        ("", True),
        ("  ", True),
        ("   ", True),
        

        ("Не пусто", False),
        ("Не пусто с пробелом", False),
        ("023", False),

    ]
def test_is_empty(string, result):
        res = utils.is_empty(string,)
        assert res == result



"""list_to_string"""


@pytest.mark.parametrize('lst, joiner, result',[
      (["P", "E", "T", "R"], ".", "P.E.T.R"),
      ([1,2,3,4,5], None, "1,2,3,4,5"),
      (["Петр", "Первый"], "-", "Петр-Первый"),
      (["Петр", "Первый"], "Великий", "ПетрВеликийПервый"),
      (["Петр", "1" "Первый"], "", "Петр1Первый"),

      ([], None, ""),
      ([], ",", ""),
      ([], "Петр", "")
])
def test_list_to_string('lst, joiner, result'):
      if joiner == None:
            res = utils.list_to_string(lst)
      else:
            res = utils.list_to_string(lst, joiner)
            assert res == result




















