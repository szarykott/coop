import cliargs as cli
import logic as l

def main():
    args = cli.parse_args()
    l.perform_action(args)

if __name__ == "__main__":
    main()