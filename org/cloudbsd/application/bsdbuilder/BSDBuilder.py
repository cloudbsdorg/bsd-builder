from org.cloudbsd.application.type.CLIApplication import CLIApplication

class BSDBuilder(CLIApplication):

    def __init__(self):
        super().__init__()
        print(f'Hi')