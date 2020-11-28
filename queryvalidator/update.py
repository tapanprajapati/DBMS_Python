import queryvalidator.common_methods as validator

sql = 'UPDATE test SET salary = 2000, first_name = Zongyu WHERE id = 1'

def validate(parsetree):
    validator.validatetable(parsetree)
    validator.validatecolumnvaluepair(parsetree)
    validator.validatecondition(parsetree)


