class accounts:
    def __init__(self, n,b,p):
        self.accNo = int(n)
        self.balance = float(b)
        self.password = p

acc = []
def isUnique(item):
    for i in acc:
        if int(item) == i.accNo:
            return 0
    return 1

def create(args):
    if not isUnique(args.accNo) or not args.accNo.isnumeric():
        return '-500'
    elif len(args.password) < 4:
        return '-201'
    elif float(args.amt) < 0:
        return '-300'
    else:
        newAcc = accounts(args.accNo,args.amt,args.password)
        acc.append(newAcc)
        return str(newAcc.accNo)

def credit(args):
    if int(args.amt) < 0:
        return '-300'

    for i in acc:
        if int(args.accNo) == i.accNo:
            if args.password == i.password:
                i.balance = i.balance + float(args.amt)
                return str(i.balance)
            else:
                return '-200'
    return '-501'

def debit(args):
    if int(args.amt) < 0:
        return '-300'

    for i in acc:
        if int(args.accNo) == i.accNo:
            if args.password == i.password:
                if(float(args.amt) > i.balance):
                    return '-301'
                else:
                    i.balance = i.balance - float(args.amt)
                    return str(i.balance)
            else:
                return '-200'
    return '-501'

def bal(args):
    for i in acc:
        if int(args.accNo) == i.accNo:
            if args.password == i.password:
                    return str(i.balance)
            else:
                return '-200'
    return '-501'

def display(args):
    ret = "Account\tBalance\n"
    if len(acc)==0:
        return '-400'
    else:
        for i in acc:
            ret = ret + str(i.accNo) + "\t" + str(i.balance) + "\n"
        return ret


def runCmd(args):
    if args.action == 'CREATE':
        ret = create(args)
    elif args.action == 'CREDIT':
        ret = credit(args)
    elif args.action == 'DEBIT':
        ret = debit(args)
    elif args.action == 'BAL':
        ret = bal(args)
    elif args.action == 'DISPLAY':
        ret = display(args)
    return ret
    


