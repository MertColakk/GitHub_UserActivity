import argparse
import requests

# Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--username", required=True, help="GitHub kullanıcı adını belirtin!")
args = ap.parse_args()

# Request Settings
url = f"https://api.github.com/users/{args.username}/events"
headers = {'user-agent': 'github-useractivity/0.0.1'}

# Main
if __name__ == "__main__":
    # Make request
    response = requests.get(url, headers=headers)

    # Check response status
    if response.status_code == 200:
        events = response.json()

        # Iterate through all events
        for event in events:
            event_type = event.get("type", "")
            repo_name = event.get("repo", {}).get("name", "Unknown repository")

            if event_type == "PushEvent":
                commit_count = len(event.get("payload", {}).get("commits", []))
                print(f"- Pushed {commit_count} commits to {repo_name}")
            elif event_type == "IssuesEvent":
                action = event.get("payload", {}).get("action", "unknown action")
                print(f"- {action.capitalize()} a new issue in {repo_name}")
            elif event_type == "WatchEvent":
                print(f"- Starred {repo_name}")
            elif event_type == "PullRequestEvent":
                action = event.get("payload", {}).get("action", "unknown action")
                print(f"- {action.capitalize()} a pull request in {repo_name}")
            elif event_type == "CreateEvent":
                ref_type = event.get("payload", {}).get("ref_type", "unknown type")
                print(f"- Created a new {ref_type} in {repo_name}")
            else:
                # Handle unprocessed event types
                print(f"- {event_type} occurred in {repo_name}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Error details: {response.text}")
