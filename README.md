# Cloudbric-slack-emergency

1. When we assign manager to respond to emergencies, we use Google Calendar.
2. Then we register manager assigned to emergencies with Slack using API.

## Process
* Download csv file(saved as "clb_error_manager_list") from Google Calendar.
* And then run `python from_csv_to_slack_reminder.py` to get `slack_reminder_emergency.txt`.
* Then Cut and Paste each line to Slack emergency channel.