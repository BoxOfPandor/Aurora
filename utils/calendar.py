from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

def get_google_calendar_events(credentials_file):
    creds = service_account.Credentials.from_service_account_file(credentials_file, scopes=["https://www.googleapis.com/auth/calendar.readonly"])
    service = build('calendar', 'v3', credentials=creds)
    
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return "Vous n'avez pas d'événements à venir dans votre agenda."

    events_list = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        events_list.append(f"{start} - {event['summary']}")

    return "Voici vos prochains événements : " + "; ".join(events_list)
