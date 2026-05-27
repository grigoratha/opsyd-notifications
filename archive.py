import json
import hashlib

from pathlib import Path
from logger import *

def generate_hash(date, description):
    return hashlib.sha256((date + description).encode("utf-8")).hexdigest()


def load_archive(path):
    logger.info(f"Accessing archive file: {path}");
    file = Path(path)

    if not file.exists():
        logger.warning(f"Archive file is not found");
        return set()

    try:
        content = file.read_text(encoding="utf-8").strip()

        if not content:
            logger.warning(f"Archive file has no content: {path}");
            return set()

        return set(json.loads(content))

    except json.JSONDecodeError as e:
        logger.error(
            f"Archive file failed to parse: {e.msg} at line {e.lineno} column {e.colno}")
        return set()


def update_archive(path, archive_set):
    Path(path).write_text(json.dumps(list(archive_set), ensure_ascii=False, indent=2), encoding="utf-8")