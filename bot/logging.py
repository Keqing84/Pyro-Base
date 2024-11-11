import os
from logging import (
    getLogger,
    FileHandler,
    StreamHandler,
    INFO,
    basicConfig
)


if os.path.exists('log.txt'):
    with open('log.txt', 'w+') as f:
        f.truncate(0)

basicConfig(
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
    handlers=[FileHandler("log.txt"), StreamHandler()],
    level=INFO,
)

LOG = getLogger(__name__)
