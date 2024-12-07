import os
import pathlib
from aocd.models import Puzzle
from aocd.exceptions import PuzzleLockedError
import sys
import datetime


TEMPLATE_FOR_CODE_FILE = """'''AoC_Year{}_Day{}_Part{}'''



INPUT_PATH=r\"{}\"
EXAMPLE_INPUT_PATH=r\"{}\"


"""


TEMPLATE_FOR_NOTEBOOK_FILE = r"""{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "INPUT_PATH=\"input.txt\"\n",
    "EXAMPLE_INPUT_PATH=\"example1.txt\"\n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

"""


def download(year, day, path_to_save_at):
    """Get input and write it to input.txt inside the puzzle folder"""
    puzzle = Puzzle(year=year, day=day)

    # Download input
    # year_path =
    output_path = pathlib.Path(path_to_save_at) / "input.txt"
    output_path.write_text(puzzle.input_data)

    # Download example data
    for index, example in enumerate(puzzle.examples, start=1):
        output_path = output_path.with_stem(f"example{index}")
        output_path.write_text(example.input_data)

    # Add README with link to puzzle text
    readme_path = output_path.with_name("README.md")
    readme_path.write_text(
        f"# {puzzle.title}\n\n"
        f"**Advent of Code: Day {day}, {year}**\n\n"
        f"See {puzzle.url}\n"
    )


def setup_day(year, day):
    day_folder_path = os.path.join(pathlib.Path(__file__).parent, "day" + str(day))
    os.makedirs(day_folder_path, exist_ok=True)

    try:
        download(year=year, day=day, path_to_save_at=day_folder_path)
    except PuzzleLockedError:
        print("Puzzle is still locked. Could not download inputs")

    for part in range(1, 3):
        part_path = os.path.join(day_folder_path, f"part{part}.py")
        if not os.path.exists(part_path):
            with open(part_path, "w") as f:
                f.write(
                    TEMPLATE_FOR_CODE_FILE.format(
                        year,
                        day,
                        part,
                        "input.txt",
                        "example1.txt",
                    )
                )

    scratchpad_path = os.path.join(day_folder_path, f"scratchpad.ipynb")
    if not os.path.exists(scratchpad_path):
        with open(scratchpad_path, "w") as f:
            f.write(TEMPLATE_FOR_NOTEBOOK_FILE)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        year = int(sys.argv[1])
        day = int(sys.argv[2])
    else:
        today = datetime.date.today()
        year = today.year
        day = today.day
    print(f"Setting up folder for Year {year} Day {day}")
    setup_day(year=year, day=day)
    print("Setup Done")
