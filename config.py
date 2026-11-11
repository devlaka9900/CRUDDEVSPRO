from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "todo.db"
APP_TITLE = "Todo Manager"
STATUSES = ["Todo", "In-Progress", "Done"]
PRIORITIES = {1: "High", 2: "Medium", 3: "Low"}

DATA_FORMAT = "yyyy-MM-dd"