
from config import Config
from file_utils import FileUtils
from frame_builder import FrameBuilder
from gif_builder import GifBuilder
from github_api import GitHubAPI
from log_config import logger
from text_builder import TextBuilder

if __name__ == "__main__":
    logger.info(f"Starting Metrix v{Config.VERSION}")
    try:
        FileUtils.cleanup_frames_folder(Config.TEMP_FRAMES_DIR)
        data = GitHubAPI.fetch_github_data(Config.GITHUB_USERNAME, Config.TOKEN)
        text_lines = TextBuilder.generate_text(data["user"], data["repos"])
        frame_rate = Config.FPS  # Maximum rate is 50 FPS, higher values make it slower
        commits_last_month = GitHubAPI.get_commits_last_month(Config.GITHUB_USERNAME, Config.TOKEN)
        activity_graphic = TextBuilder.generate_activity_graphic(commits_last_month)
        FrameBuilder.create_typing_frames(text_lines, activity_graphic)
        filename = f"{Config.OUTPUT_GIF_NAME}.gif"
        GifBuilder.generate_gif_ffmpeg(frame_rate, filename)
        logger.info(f"GIF saved as {filename}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
