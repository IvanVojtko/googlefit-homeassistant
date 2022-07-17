import pickle

from google_auth_oauthlib.flow import InstalledAppFlow

# Scopes required for integration
SCOPES = ['https://www.googleapis.com/auth/fitness.heart_rate.read',
          'https://www.googleapis.com/auth/fitness.body.read',
          'https://www.googleapis.com/auth/fitness.activity.read',
          'https://www.googleapis.com/auth/fitness.location.read',
          'https://www.googleapis.com/auth/fitness.blood_pressure.read',
          'https://www.googleapis.com/auth/fitness.oxygen_saturation.read',
          'https://www.googleapis.com/auth/fitness.activity.read',
          'https://www.googleapis.com/auth/fitness.nutrition.read',
          'https://www.googleapis.com/auth/fitness.sleep.read']


def main():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes=SCOPES)
    creds = flow.run_local_server()
    # Save the credentials
    with open('.google_fit.token', 'wb') as token:
        pickle.dump(creds, token)
    print("Please copy .google_fit.token to your HA configuration directory")


if __name__ == '__main__':
    main()
