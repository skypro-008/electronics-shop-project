from pathlib import Path

PATH = Path(__file__).resolve().parent.parent
CSV = Path.joinpath(PATH, "src", "items.csv")
