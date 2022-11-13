class arguments:
    def __init__(self,args):
        self.action = args[0]
        for item in args[1:]:
            if item[0] == 'p':
                self.password = item[1]
            elif item[0] == 'a':
                self.accNo = item[1]
            elif item[0] == 'm':
                self.amt = item[1]


def checkArgs(n):
    args = ['p' , 'm' , 'a']

    if n[0] not in args:
        return 0
    elif n[0] == 'm' and len(n) == 1:
        return 2
    else:
        return 1

def parse(cmd):
    args = cmd.split(' -')
    args = list(map(lambda n : n.rstrip(),args))
    args[1:] = list(map(lambda n : n.split(),args[1:]))
    print(args)

    functions = ['CREATE','CREDIT','DEBIT','BAL','DISPLAY']

    # if any(list(map(lambda n: n.isnumeric(),args))):
    #     return '-300'
    if args[0] not in functions:
        if any(el == 2 for el in list(list(map(checkArgs,args[1:])))):
            return '-300'
        elif not all(list(list(map(checkArgs,args[1:])))):
            return '-100'

    elif args[0] in ['CREATE','DEBIT','CREDIT'] and len(args) != 4 or args[0] == 'BAL' and len(args) != 3 or args[0] == 'DISPLAY' and len(args) != 1:
        return '-101'
    
    obj = arguments(args)
    return obj