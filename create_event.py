from datetime import datetime, timedelta

import cal_setup
from cal_setup import get_calendar_service


def main(summary, color, description, start, end):
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 12) + timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=1)).isoformat()

    event_result = service.events().insert(calendarId=cal_setup.BOT_CALENDAR,
                                           body={
                                               "summary": 'Zimmer Aufräumen',
                                               "colorId": "6",
                                               "description": 'Hannah ist Cool',
                                               "start": {"dateTime": start, "timeZone": 'Europe/Vienna'},
                                               "end": {"dateTime": end, "timeZone": 'Europe/Vienna'},
                                           }
                                           ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])


if __name__ == '__main__':
    main()
