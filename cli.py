import sys
import argparse


def calc(args):

    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--x', type=float, default=0.0, help="This is a command line interface. Enter first float here!")

    parser.add_argument('--y', type=float, default=0.0, help='This is a command line utility. Enter second float here!')

    parser.add_argument('--o', type=str, default='add',
                        help='This is a command line interface. Enter operator here. opearators are [add, sub, mul, div]')



    args = parser.parse_args()

    sys.stdout.write(str(calc(args)))