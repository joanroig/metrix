
import os
import time
from venv import logger

from color_utils import ColorUtils
from config import Config
from file_utils import FileUtils
from frame_builder import FrameBuilder
from gif_builder import GifBuilder
from github_api import GitHubAPI
from text_builder import TextBuilder

if __name__ == "__main__":
    logger.info("Starting...")
    try:
        text_color = os.getenv("TEXT_COLOR", "limegreen").lower()
        background_color = os.getenv("BACKGROUND_COLOR", "white").lower()
        # allow parallel executions
        Config.TEMP_FRAMES_DIR = Config.TEMP_FRAMES_DIR + "_" + str(int(time.time()))
        while True:
            # restore original values on each iteration
            Config.TEXT_COLOR, Config.BACKGROUND_COLOR, Config.METHOD, Config.CONTRAST = ColorUtils.resolve_colors(text_color, background_color, Config.MINIMUM_CONTRAST)
            # Check if the file already exists
            # filename = f"bulk/{Config.OUTPUT_GIF_NAME}_{Config.BACKGROUND_COLOR}_{Config.TEXT_COLOR}_{Config.CONTRAST}_{Config.METHOD}.gif"
            filename = f"bulk/{Config.OUTPUT_GIF_NAME}_{Config.BACKGROUND_COLOR}_{Config.TEXT_COLOR}.gif"
            if os.path.exists(filename):
                logger.warning(f"File already exists: {filename}, skipping generation.")
                continue
            FileUtils.cleanup_frames_folder(Config.TEMP_FRAMES_DIR)
            data = GitHubAPI.fetch_github_data(Config.GITHUB_USERNAME, Config.TOKEN)
            text_lines = TextBuilder.generate_text(data["user"], data["repos"])
            frame_rate = 50  # Maximum rate is 50 FPS, higher values make it slower
            commits_last_month = GitHubAPI.get_commits_last_month(Config.GITHUB_USERNAME, Config.TOKEN)
            activity_graphic = TextBuilder.generate_activity_graphic(commits_last_month)
            FrameBuilder.create_typing_frames(text_lines, activity_graphic)
            GifBuilder.generate_gif_ffmpeg(frame_rate, filename)
            logger.info(f"GIF saved as: {filename}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
