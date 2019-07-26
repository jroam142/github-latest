import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]
    base_url = "https://api.github.com"

    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.
    response = requests.get(base_url + '/users/' + username + '/events')
    first_event_timestampt = json.loads(response.content)[0]['created_at']

    # print("COMPLETE THE TODOs")
    print(first_event_timestampt)
    


