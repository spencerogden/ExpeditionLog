import csv
import sys


def process_log(filename):
    """Takes a new format log from Expedition and saves in Excel friendly
    CSV format, all the same data in the same columns. The new log is saved
    with the prefix "Excel-".
    """
    print(f"Processing {filename}")
    with open(filename, newline='') as log_file:
        log_in = csv.reader(log_file)
        fields = next(log_in)
        field_ids = next(log_in)
        field_ids[0] = -1
        fields_to_colnum = dict(zip(map(int,field_ids),range(len(fields))))
    
        expedition_version = next(log_in)[0]
        if fields[0] != "!Boat" or not expedition_version.startswith("!v"):
            print(f"{filename} is not an Expedition Log, skipping: !Boat and !v version tags missing")
        line_num = 3
        with open("Excel-"+filename,"w") as log_out:
            csv_writer = csv.writer(log_out)
            csv_writer.writerow(fields)
            skipped_lines = []
            for line in log_in:
                pairs = zip(line[0::2], line[1::2])
                full_line = [None]*(len(fields)+1)
                for id,data in pairs:
                    try:
                        full_line[fields_to_colnum[int(id)]] = data
                    except (KeyError,ValueError):
                        skipped_lines.append(line_num)
                        break
                csv_writer.writerow(full_line)
                line_num += 1
    if skipped_lines:
        print(f"The following lines were skipped due to errors in {filename}")
        print(skipped_lines)

if __name__ == "__main__":
    for f in sys.argv[1:]:
        if f.endswith(".csv"):
            process_log(f)
        else:
            print(f"{f} is not a CSV, skipping: not a CSV file")
