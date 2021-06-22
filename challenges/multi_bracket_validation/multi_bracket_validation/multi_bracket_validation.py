import re

    
def multi_bracket_validation(input):
    boolen=False
    if input.count('{')  == input.count('}') and input.count('(') == input.count(')') and input.count('[') == input.count(']'):
        boolen=True

    x=re.search('\(.?}',input)
    y=re.search('\(.?]',input)
    z=re.search('\{.?\)',input)
    a=re.search('\{.?]',input)
    b=re.search('\[.?\)',input)
    c=re.search('\[.?}',input)
    
    if x or y or z or a or b or c :
        
        boolen=False
    print(boolen)
    return boolen
    
    



if __name__ == '__main__':
    multi_bracket_validation('{}')
    multi_bracket_validation('{}(){}')
    multi_bracket_validation('()[[Extra Characters]]')
    multi_bracket_validation('(){}[[]]')
    multi_bracket_validation('{}{Code}[Fellows](())')
    multi_bracket_validation('[({}]')
    multi_bracket_validation('(](')
    multi_bracket_validation('{(})')
    multi_bracket_validation('{)')
    multi_bracket_validation('{)')
    multi_bracket_validation('{')

    





    




    