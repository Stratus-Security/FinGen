from .FindingsGenerator import FinGen

def main(args):
    FinGen.CreateFinding(args.api_key, args.title, args.company)

if __name__ == "__main__":
    main(FinGen.get_parser().parse_args())