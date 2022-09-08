# ExpeditionLog

Use the script log_reformat.py to reformat [Expedition](https://www.expeditionmarine.com) logs from the new format into an Excel friendly CSV. The new file will be named "Excel-<orignial name>" and will have each datapoint in its own column with the top row the data name.

Examples:

Process one log file
  
`> python log_reformat.py log-2022Sep11.csv`

Process a whole folder

`> python log_reformat.py log*.csv`

Requires Python version 3+.
