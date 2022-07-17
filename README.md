[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/IvanVojtko/)

# Google Fit Sensor Component

Based on

- <https://github.com/cyberjunky/home-assistant-google_fit>

Creates Google Fit sensors.
At the moment, the component provides following measurements:

- steps
- distance
- time
- calories
- weight
- height
- sleep
- heartrate
- oxygen
- blood pressure
- nutrition
- hydratation
- BMR

# Installation

## HACS - Recommended
- Have [HACS](https://hacs.xyz) installed, this will allow you to easily update.
- Add `https://github.com/IvanVojtko/googlefit-homeassistant` as a [custom repository](https://github.com/IvanVojtko/googlefit-homeassistant) with Type: Integration
- Click Install under "Google Fit" integration.
- Restart Home-Assistant.

## Manual
- Copy directory `custom_components/google_fit` to your `<config dir>/custom_components` directory.
- Configure.
- Restart Home-Assistant.

## Example configuration.yaml

In order to add this component as is, add a new sensor:

```yaml
sensor:
  - platform: google_fit
    name: Google Fit
```

## Google Fit credentials

In order to generate `credentials.json`, follow these steps for Google Calendar component, but slightly modified:
<https://www.home-assistant.io/components/calendar.google/#prerequisites>

1. First go to the [Google Developers Console](https://console.developers.google.com/start/api?id=calendar)
2. The wizard will ask you to choose a project to manage your application. Select a project and click continue.
3. Verify that your calendar API was enabled and click ‘Go to credentials’
4. Navigate to APIs & Services (left sidebar) > [Credentials](https://console.cloud.google.com/apis/credentials)
5. Click on the field on the right of the screen, **OAuth Consent Screen**.
6. Select **External** and **Create**.
7. Set the App Name (the name of the application asking for consent) to anything you want e.g. Home Assistant.
8. You then need to select a Support email. To do this, simply click the drop down box and select your email address.
9. You finally need to complete the section: Developer contact information. To do this, simply enter your email address (same as above is fine).
10. Scroll to the bottom and click **Save and Continue**. Don’t have to fill out anything else or it may enable additional review.
11. You will then be automatically taken to the Scopes page. You do not need to add any scopes here so click Save and Continue to move to the Optional info page. You do not need to add anything to the Optional info page so click Save and Continue which will take you to the Summary page. Click Back to Dashboard.
12. Click **OAuth consent screen** again and set Publish Status to **Production** otherwise your credentials will expire every 7 days.
13. Click **Credentials** in the menu on the left hand side of the screen, then click **Create credentials** (at the top of the screen), then select OAuth client ID.
14. Set the Application type to **Desktop** and give this credential set a name (like “Home Assistant Credentials”) then click **Create**.
15. You will then be presented with a pop-up saying OAuth client created showing Your Client ID and Your Client Secret. Make a note of these (for example, copy and paste them into a text editor) as you will need these shortly. Once you have noted these strings, click **OK**. If you need to find these credentials again at any point then simply navigate to APIs & Services > Credentials and you will see Home Assistant Credentials (or whatever you named them in the previous step) under OAuth 2.0 Client IDs. To view both the Client ID and Client secret, click on the pencil icon, this will take you to the settings page for these credentials and the information will be on the right hand side of the page.
16. Double check that the Google Calendar API has been automatically enabled. To do this, select **Library** from the menu, then search for Google Calendar API. If it is enabled you will see API Enabled with a green tick next to it. If it is not enabled, then enable it.

To make sensor work you have to enable the **Fitness API** in your project. Add all Fitness API read scopes. After generating credentials, download `credentials.json` file
and place it into this directory, next to `get_credentials.py`
In oder to enable Fitness API open Google Cloud console: 
<https://console.cloud.google.com/apis/library/fitness.googleapis.com>
and enable API.

To allow HA access your Fit data, you need to complete a challenge. It can't be completed by HA so that's why you need to use `get_credentials.py` script. First install all the
requirements using `python -m pip install -r requirements.txt`. Then run script `python get_credentials.py`, open 
the generated URL, allow access and don't forget to tick mark all permissions. This script will generate  `.google_fit.token` file. Copy this file to your HA configuration directory.

## Sensors

| Sensor name        | Entity                           |
|--------------------|----------------------------------|
| Steps              | sensor.google_steps              |
| Calories           | sensor.google_calories           |
| Distance           | sensor.google_distance           |
| Heart rate         | sensor.google_heart_rate         |
| Resting heart rate | sensor.google_resting_heart_rate |
| Move time          | sensor.google_move_time          |
| Blood oxygen       | sensor.google_oxygen             |
| Sleep              | sensor.google_sleep              |
| Blood pressure SYS | sensor.google_blood_pressure_sys |
| Blood pressure DIA | sensor.google_blood_pressure_dia |
| Hydratation        | sensor.google_hydratation        |
| BMR                | sensor.google_bmr                |

![](https://github.com/IvanVojtko/googlefit-homeassistant/blob/master/2.png?raw=true)

## Attributes

| Attribute name      | Entity                  | Attribute           |
|---------------------|-------------------------|---------------------|
| Potassium           | sensor.google_nutrition | potassium           |
| Calcium             | sensor.google_nutrition | calcium             |
| Vitamin A           | sensor.google_nutrition | vitamin_a           |
| Vitamin C           | sensor.google_nutrition | vitamin_c           |
| Total carbs         | sensor.google_nutrition | carbs.total         |
| Polyunsaturated fat | sensor.google_nutrition | fat.polyunsaturated |
| Monounsaturated fat | sensor.google_nutrition | fat.monounsaturated |
| Calories            | sensor.google_nutrition | calories            |
| Trans fat           | sensor.google_nutrition | fat.trans           |
| Total fat           | sensor.google_nutrition | fat.total           |
| Sodium              | sensor.google_nutrition | sodium              |
| Saturated fat       | sensor.google_nutrition | fat.saturated       |
| Protein             | sensor.google_nutrition | protein             |
| Cholesterol         | sensor.google_nutrition | cholesterol         |
| Iron                | sensor.google_nutrition | iron                |
| Sugar               | sensor.google_nutrition | sugar               |
| Dietary fiber       | sensor.google_nutrition | dietary_fiber       |


![](https://github.com/IvanVojtko/googlefit-homeassistant/blob/master/1.png?raw=true)
