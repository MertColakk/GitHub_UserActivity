[https://roadmap.sh/projects/github-user-activity](https://roadmap.sh/projects/github-user-activity)

```markdown
# GitHub User Activity Tracker

This Python script fetches the recent activities of a GitHub user and displays the results in a user-friendly format. It provides details about various GitHub events like pushes, issues, pull requests, stars, and repository creations.

## Features

- Displays the number of commits pushed to a repository.
- Lists actions such as opening or closing issues.
- Shows starred repositories.
- Tracks new pull requests.
- Provides information on newly created branches or tags.

## Requirements

- Python 3.x
- `requests` library (You can install it using `pip install requests`)

## Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/github-activity-tracker.git
   cd github-activity-tracker
```

2. Install required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

   Or directly install `requests` if not using a `requirements.txt` file.

   ```bash
   pip install requests
   ```

## Usage

To use the script, run the following command:

```bash
python github_events.py -u <GitHub-Username>
```

Replace `<GitHub-Username>` with the GitHub username of the account whose activities you want to track.

### Example

```bash
python github_events.py -u kamranahmedse
```

This will fetch and display the recent activities of the user `kamranahmedse` such as pushed commits, opened issues, starred repositories, and more.

### Sample Output

```bash
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- Opened a pull request in kamranahmedse/developer-roadmap
- Created a new branch in kamranahmedse/developer-roadmap
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.

## Acknowledgments

* Thanks to the [GitHub API](https://developer.github.com/v3/) for providing the data.
* Special thanks to the open-source community for their contributions.

```

### Notes
1. **Installation**: If you want to include a `requirements.txt` file, you can generate it using:
   ```bash
   pip freeze > requirements.txt
```

Add the `requests` package to this file.

2. **Usage Example** : Replace `<GitHub-Username>` with an actual GitHub username when running the script.
