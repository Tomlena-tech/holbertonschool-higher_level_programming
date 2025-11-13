#!/usr/bin/python3
import os, re

def generate_invitations(template, attendees):
#heck template / compared attendies into argv#
    if not isinstance(template, str):
        print("Erreur : that should be a string")
        return
    if not isinstance (attendees, list):
        print("Error : that should be a list")
        return
    if not template :
        print("Error : that should not empty")
        return
    if not attendees : 
        print("Error : that should not empty")
        
    placeholders = re.findall(r'\{(\w+)\}', template)
    for index, attendees in enumerate(attendees, template)
        try : 
            if not isinstance(attendee, dict)):
                print("N/A")


