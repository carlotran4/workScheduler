from write import get_credentials, add_event
from datetime import datetime


def main():
    creds = get_credentials()
    start = datetime(2023, 5, 22, 13, 0, 0)
    end = datetime(2023, 5, 22, 15, 0, 0)
    add_event("test", start, end, creds)


if __name__ == "__main__":
    main()
