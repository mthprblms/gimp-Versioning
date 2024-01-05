#!/usr/bin/env python

from gimpfu import *
import time
import json

# Custom metadata field key
VERSION_METADATA_KEY = 'version_history'

def log_version(image, action_type):
    # Retrieve existing version history or create a new one
    version_history = json.loads(image.metadata(VERSION_METADATA_KEY, None) or '[]')

    # Log version information
    version_info = {
        'timestamp': time.time(),
        'action': action_type,
    }
    version_history.append(version_info)

    # Save version history back to the image metadata
    image.attach_new_metadata(1, VERSION_METADATA_KEY, json.dumps(version_history))

def save_version_history(image, drawable):
    # Save version history to a file or perform any other actions
    version_history = json.loads(image.metadata(VERSION_METADATA_KEY, None) or '[]')
    filename = "/path/to/version_history.txt"

    with open(filename, 'w') as file:
        json.dump(version_history, file)

def your_plugin_function(image, drawable):
    # Your plugin logic goes here

    # Log the version after each change
    log_version(image, 'your_action_type')

# Register your plugin
register(
    "python_fu_your_plugin",
    "Your Plugin Description",
    "Your Plugin Help",
    "Your Name",
    "Your Copyright",
    "Year",
    "Your Plugin",
    "*",
    [],
    [],
    your_plugin_function,
)

# Register a function to save the version history
register(
    "python_fu_save_version_history",
    "Save Version History",
    "Save the version history to a file",
    "Your Name",
    "Your Copyright",
    "Year",
    "Save Version History",
    "*",
    [],
    [],
    save_version_history,
)

main()
