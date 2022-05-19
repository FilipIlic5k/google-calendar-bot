# Script to delete events from google calendar
import sys

import googleapiclient

import cal_setup
from cal_setup import get_calendar_service


def main(eventID):
    # Delete the event
    service = get_calendar_service()
    try:
        service.events().delete(
            calendarId=cal_setup.BOT_CALENDAR,
            eventId=eventID,
        ).execute()
    except googleapiclient.errors.HttpError:
        print("Failed to delete event")

    print("Event deleted")


if __name__ == '__main__':
    main(*sys.argv[1:])
