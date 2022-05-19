import create_event
from cal_setup import get_calendar_service


def main():
    cal_service = get_calendar_service()
    # Call the Calendar API

    event = create_event.main()


if __name__ == '__main__':
    main()
