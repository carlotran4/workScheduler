from __future__ import print_function

from datetime import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def get_credentials() -> Credentials:
    """Get credentials for user's Google Calendar. If they have not logged in before,
    use Oauth to get permission.
    Returns:
        Credentials: Credentials for the person's google calendar
    """
    scopes = ['https://www.googleapis.com/auth/calendar']

    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    # Use OAuth to get authorization from user.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials in token.json.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def add_event(name: str, start: datetime, end: datetime, creds: Credentials):
    """Adds an event to a user's calendar.

    Args:
        name (str): Name of event
        start (datetime): Start of event
        end (datetime): End of event
        creds (Credentials): Credentials for user's calendar
    """
    service = build('calendar', 'v3', credentials=creds)
    start_string = start.strftime("%Y-%m-%dT%H:%M:%S-05:00")
    end_string = end.strftime("%Y-%m-%dT%H:%M:%S-05:00")
    event = {
        "summary": "test",
        "start": {
            "dateTime": start_string,
            "timeZone": "America/Chicago"
        },
        "end": {
            "dateTime": end_string,
            "timeZone": "America/Chicago"
        }
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
