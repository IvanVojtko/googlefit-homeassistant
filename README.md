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

![](https://github.com/IvanVojtko/googlefit-homeassistant/blob/master/2.png?raw=true)

![](https://github.com/IvanVojtko/googlefit-homeassistant/blob/master/1.png?raw=true)

# Installation

## HACS - Recommended
- Have [HACS](https://hacs.xyz) installed, this will allow you to easily update.
- Add `https://github.com/IvanVojtko/googlefit-homeassistan` as a [custom repository](https://github.com/IvanVojtko/googlefit-homeassistant) with Type: Integration
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

In order to generate `credentials.json`, see the prerequisites for the Google Calendar component:
<https://www.home-assistant.io/components/calendar.google/#prerequisites>
To make sensor work you have to enable the Fitness API in your project. Add all Fitness API read scopes. After generating credentials, download `credentials.json` file
and place it into this directory, next to `get_credentials.py`
In oder to enable Fitness API open Google Cloud console: 
<https://console.cloud.google.com/apis/library/fitness.googleapis.com>
and enable API.

To allow HA access your Fit data, you need to complete a challenge. It can't be completed by HA so that's why you need to use `get_credentials.py` script. Run script, open 
the generated URL, allow access and don't forget to tick mark all permissions. This script will generate  `.google_fit.token` file. Copy this file to your HA configuration directory.

