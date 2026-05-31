from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file(
            'token.json',
            SCOPES
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)


service = get_calendar_service()

start_date = datetime.now().date()

for day in range(1, 61):

    event_date = start_date + timedelta(days=day - 1)

    start_time = datetime.combine(
        event_date,
        datetime.strptime("11:00", "%H:%M").time()
    )

    end_time = start_time + timedelta(minutes=60)

    event = {
        'summary': f'Python Practice - Day {day}',
        'description': f'Practice Python and AI project work - Day {day}',
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {
                    'method': 'popup',
                    'minutes': 10
                }
            ]
        }
    }

    service.events().insert(
        calendarId='primary',
        body=event
    ).execute()

    print(f"Created Day {day}")

print("All 60 events created successfully.")
