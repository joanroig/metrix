
import os
import shutil

from log_config import logger


class FileUtils:
    """Class for file utilities."""

    @staticmethod
    def cleanup_frames_folder(temp_frames_dir):
        if os.path.exists(temp_frames_dir):
            shutil.rmtree(temp_frames_dir)
        os.makedirs(temp_frames_dir)

    @staticmethod
    def read_token_from_file(file_path=".github_token"):
        """ Reads a PAT token from a file, used only for debugging locally """
        logger.info(f"Reading token from: {os.path.abspath(file_path)}")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        logger.info(f"Error reading token, please make sure to place it in: {os.path.abspath(file_path)}")
        return None

    @staticmethod
    def resolve_font_path(font_path: str) -> str:
        """
        Resolves the font path:
        - If font_path exists -> return as-is
        - Else -> check GITHUB_ACTION_PATH fallback
        - Raise error if still not found
        """
        if font_path and os.path.isfile(font_path):
            return font_path

        github_action_path = os.getenv('GITHUB_ACTION_PATH')
        if github_action_path:
            fallback_path = os.path.join(github_action_path, font_path)
            if os.path.isfile(fallback_path):
                return fallback_path

        raise FileNotFoundError(f"Font file not found: {font_path}")
