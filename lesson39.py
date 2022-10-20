from parser2 import Parser

parser = Parser('https://dvmn.org/modules/', 'fffff.txt')

parser.run()
print(parser.results)
