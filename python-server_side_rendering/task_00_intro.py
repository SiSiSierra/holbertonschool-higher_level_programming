#!/usr/bin/python3
import os


def generate_invitations(template, attendees):

    if type(template) is not str:
        print('Template is not a string, no output files generated.')
        return
    if template == '':
        print('Template is empty, no output files generated.')
        return
    if type(attendees) is not list:
        print('Attendees is not a list, no output files generated.')
        return
    if len(attendees) == 0:
        print('No data provided, no output files generated.')
        return
    if all(type(a) is dict for a in attendees) is False:
        print('Attendess aren\'t all dicts, no output files generated.')
        return

    i = -1
    for person in attendees:
        i += 1
        print("Making file")
        new = str(template)
        keys = ["name", "event_title", "event_date", "event_location"]
        for key in keys:
            try:
                j = person[key]
                if j is None:
                    raise KeyError
            except KeyError:
                person[key] = "N/A"
            new = new.replace(f"{{{key}}}", person[key])
        try:
            name = f"output_{i}.txt"
            if os.path.exists(name):
                print(f"{name} already exists.")
                continue
            with open(name, "w") as f:
                f.write(new)
        except Exception as e:
            raise Exception(e)
