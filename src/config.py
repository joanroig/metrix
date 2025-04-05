import os
import textwrap

from color_utils import ColorUtils
from file_utils import FileUtils


class Config:
    """Class to handle configuration and environment variables."""

    # Version
    VERSION = "2.0"

    # Debug Mode
    DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"

    # Authentication
    TOKEN = os.getenv("GITHUB_TOKEN") if not DEBUG_MODE else FileUtils.read_token_from_file()
    GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

    # Fonts
    FONT_SIZE = int(os.getenv("FONT_SIZE"))
    SYMBOL_FONT_SIZE = int(os.getenv("SYMBOL_FONT_SIZE"))
    FONT_PATH = os.getenv("FONT_PATH")
    SYMBOL_FONT_PATH = os.getenv("SYMBOL_FONT_PATH")

    # Colors
    _TEXT_COLOR = os.getenv("TEXT_COLOR").lower()
    _BACKGROUND_COLOR = os.getenv("BACKGROUND_COLOR").lower()
    MINIMUM_CONTRAST = int(os.getenv("MINIMUM_CONTRAST"))
    TEXT_COLOR, BACKGROUND_COLOR, METHOD, CONTRAST = ColorUtils.resolve_colors(_TEXT_COLOR, _BACKGROUND_COLOR, MINIMUM_CONTRAST)

    # Content Settings
    TEXT = textwrap.dedent(os.getenv("TEXT"))
    TYPING_CHARACTER = os.getenv("TYPING_CHARACTER")
    ACTIVITY_TEXT = os.getenv("ACTIVITY_TEXT")
    ACTIVITY_DAYS = int(os.getenv("ACTIVITY_DAYS"))

    # Display Settings
    FPS = int(os.getenv("FPS"))  # Maximum rate is 50 FPS, higher values make it slower
    LOOP = 0 if os.getenv("LOOP").lower() == "true" else -1
    WIDTH = int(os.getenv("WIDTH"))
    HEIGHT = int(os.getenv("HEIGHT"))

    # Glitch Effects
    GLITCHES = os.getenv("GLITCHES").lower() == "true"
    MAX_GLITCHES = int(os.getenv("MAX_GLITCHES"))
    GLITCH_PROBABILITY = int(os.getenv("GLITCH_PROBABILITY")) / 100
    GLITCH_SYMBOLS = ['☺', '☻', '♥', '♦', '♣', '♠', '•', '◘', '○', '◙', '█', '░', '▒', '▓', '☼', '♪', '♫', '■', '□', '▲', '►', '▼', '◄', '◊', '●']

    # Output Paths
    OUTPUT_GIF_NAME = "metrix"
    TEMP_FRAMES_DIR = "frames"
