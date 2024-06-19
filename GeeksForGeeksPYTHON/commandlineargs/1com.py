import argparse

if __name__== "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("Numberone",help="First No:")
    parser.add_argument("Numbertwo",help="Second No:")
    parser.add_argument("Operation",help="Opertaion:", choices=['add','sub','mul'])
    args=parser.parse_args()

    print(args.Numberone)
    print(args.Numbertwo)
    print(args.Operation)

    numone=int(args.Numberone)
    numtwo=int(args.Numbertwo)
    if(args.Operation=="add"):
        print(numone+numtwo)
    elif(args.Operation=="sub"):
        print(numone-numtwo)
    else:
        print(numone*numtwo)