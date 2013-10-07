#!/usr/bin/python
import sys, argparse

def main(args):
	print args

parser = argparse.ArgumentParser(description='This description is shown when -h or --help are passed as arguments.')
parser.add_argument('required_0',
					metavar = 'PARAM_0',
					help = 'This is a required parameter')

parser.add_argument(dest = 'multi_integer',
					metavar = 'N',
					type = int,
					nargs = '+',
                    help = 'This is a multi integer parameter. You have to provide +(at least one) integers.')

parser.add_argument('-b',
					'--bar',
					dest = 'arg_name',
					metavar = 'NAME',
                   	default = '',
                    help = 'Pass a single option with this parameter')

parser.add_argument('-f',
					'--foo',
					dest = 'flag_foo',
					action = 'store_true',
					help = 'This is a flag parameter it can be set or not.')

args = parser.parse_args()
main(args)