
import math
import re
from datetime import datetime
from typing import Counter

from config import Config
from github_api import GitHubAPI
from log_config import logger


class TextBuilder:
    """Class to generate text and activity graphics."""
    @staticmethod
    def generate_activity_graphic(commits_last_month):
        if not commits_last_month:
            return ""

        log_commits = [math.log(c + 1) for c in commits_last_month]
        max_log = max(log_commits) if max(log_commits) > 0 else 1

        graphic = ""
        for log_commit in log_commits:
            percentage = (log_commit / max_log) * 100
            if percentage == 0:
                graphic += " "
            elif percentage < 25:
                graphic += "_"
            elif percentage < 50:
                graphic += "▁"
            elif percentage < 75:
                graphic += "▄"
            elif percentage < 100:
                graphic += "█"
            else:
                graphic += "◘"
        return graphic

    @staticmethod
    def extract_amount(variable_name, text):
        # Create a regex to find the pattern {variable_name[X]} or {variable_name}
        pattern = r"\{" + re.escape(variable_name) + r"\[(\d+)\]\}"
        match = re.search(pattern, text)

        # Check if the match is found
        if match:
            amount = int(match.group(1))  # Extract the number inside the brackets
            # Remove the pattern from the text (i.e., the variable with [X] part)
            text = re.sub(pattern, f"{{{variable_name}}}", text)
        else:
            amount = None  # If no amount is defined, set to None

        return amount, text

    @staticmethod
    def generate_text(user_data, repos):
        text = Config.TEXT

        total_commits = GitHubAPI.get_total_commits(Config.GITHUB_USERNAME, Config.TOKEN)

        languages_count, text = TextBuilder.extract_amount("preferred_languages", text)
        topics_count, text = TextBuilder.extract_amount("preferred_topics", text)
        licenses_count, text = TextBuilder.extract_amount("preferred_licenses", text)

        preferred_languages = [
            lang for lang, _ in Counter(
                repo.get('language') for repo in repos if repo.get('language')
            ).most_common(languages_count)
        ]

        preferred_topics = [
            topic for topic, _ in Counter(
                topic for repo in repos if repo.get('topics') for topic in repo['topics']
            ).most_common(topics_count)
        ]

        preferred_licenses = [
            license_key for license_key, _ in Counter(
                repo['license'].get('spdx_id') for repo in repos if repo.get('license') and repo['license'].get('spdx_id')
            ).most_common(licenses_count)
        ]

        variables = {
            "username": Config.GITHUB_USERNAME,
            "separator": "-" * (math.floor(Config.WIDTH / Config.FONT_SIZE) - 1),
            "updated_date": datetime.now().strftime('%Y-%m-%d'),
            "total_repos": user_data.get("public_repos", 0) + user_data.get("total_private_repos", 0),
            "total_commits": total_commits,
            "total_stars": sum(repo.get('stargazers_count', 0) for repo in repos),
            "total_forks": sum(repo.get('forks_count', 0) for repo in repos),
            "total_watchers": sum(repo.get('watchers', 0) for repo in repos),
            "total_open_issues": sum(repo.get('open_issues', 0) for repo in repos),
            "preferred_languages": ', '.join(preferred_languages) if preferred_languages else 'N/A',
            "preferred_topics": ', '.join(preferred_topics) if preferred_topics else 'N/A',
            "preferred_licenses": ', '.join(preferred_licenses) if preferred_licenses else 'N/A',
        }

        # Dynamically include all top-level GitHub user data, excluding nested objects
        for key, value in user_data.items():
            if isinstance(value, dict):
                continue
            if key == 'created_at' or key == 'updated_at':
                try:
                    variables[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
                except Exception:
                    variables[key] = 'N/A'
            else:
                variables[key] = value

        try:
            return text.format(**variables).splitlines()
        except KeyError as e:
            logger.error(f"Error: Missing or incorrect variable {e} in template.")
