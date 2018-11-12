from option import Option
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument( "--word", "-w", help="Find score for word", type=str)
group.add_argument( "--file", "-f", help="Find score for given word", action='store_true')
group.add_argument( "--score", "-s", help="Find word for given score", type=int)
args = parser.parse_args()

option = Option()
if args.word:
    print(option.score_from_word(args.word))
elif args.file:
    print(option.score_from_file())
elif args.score:
	option.word_from_score(args.score)
