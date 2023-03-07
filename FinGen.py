from FinGen import FindingsGenerator


def main(args):
    FindingsGenerator.FinGen.CreateFinding(args.api_key, args.title, args.company)

if __name__ == "__main__":
    main(FindingsGenerator.FinGen.get_parser().parse_args())