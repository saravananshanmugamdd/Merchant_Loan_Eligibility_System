import logging
import os
from datetime import datetime

Log_dir="logs"
os.makedirs(Log_dir, exist_ok=True)

log_file=datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")

logging.basicConfig(
    filename=os.path.join(Log_dir, log_file),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s|%(message)s"
)

Logger=logging.getLogger(__name__)


