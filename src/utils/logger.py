import logging
import importlib

# Try to load Rich's Console dynamically to avoid a hard dependency on 'rich' for environments
# where it's not installed; fall back to a minimal Console implementation.
_spec = importlib.util.find_spec("rich")
if _spec:
    Console = importlib.import_module("rich.console").Console
else:
    class Console:
        def print(self, *args, **kwargs):
            print(*args, **kwargs)

console = Console()

def get_logger(name: str):
    """
    Returns a logger instance with colorful output using Rich console.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s", "%H:%M:%S")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
