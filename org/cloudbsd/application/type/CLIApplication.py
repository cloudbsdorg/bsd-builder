import argparse

class CLIApplication:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--verbosity",
            help="increase output verbosity"
        )
        args = parser.parse_args()
        if args.verbosity:
            print("verbosity turned on")