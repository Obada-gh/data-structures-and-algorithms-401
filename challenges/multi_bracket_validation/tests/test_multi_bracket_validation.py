from multi_bracket_validation import __version__
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_version():
    assert __version__ == '0.1.0'

def test_cases():
   assert multi_bracket_validation('{}') == True
   assert multi_bracket_validation('{}(){}') == True
   assert multi_bracket_validation('()[[Extra Characters]]') == True
   assert multi_bracket_validation('(){}[[]]') == True
   assert multi_bracket_validation('{}{Code}[Fellows](())') == True
   assert multi_bracket_validation('[({}]') == False
   assert multi_bracket_validation('(](') == False
   assert multi_bracket_validation('{(})') == False


# # {}	TRUE
# {}(){}	TRUE
# ()[[Extra Characters]]	TRUE
# (){}[[]]	TRUE
# {}{Code}[Fellows](())	TRUE
# [({}]	FALSE
# (](	FALSE
# {(})	FALSE
