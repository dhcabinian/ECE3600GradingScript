import re
import os
import argparse
import pyexcel as p

TOTAL_POINTS = None
def calculate_point_deductions(directory_path):
    comments_path = os.path.join(directory_path, "comments.txt")
    if os.path.getsize(directory_path) == 0:
        print("Warning checking empty comments file: %s" % directory_path)
    with open(comments_path, "r") as fh:
        deductions = 0
        for line in fh:
            print(line)
            if "-" in line:
                match_obj = re.search(r"\-(\d+)", line)
                if match_obj:
                    deductions += int(match_obj.group(1))
                match_obj = re.search(r"\-([Aa][Ll][Ll])", line)
                if match_obj:
                    return TOTAL_POINTS

        return deductions

def write_grades(csv_path, grades):
    sheet = p.get_sheet(file_name=csv_path)
    for row in sheet:
        if row[1] in grades.keys():
            print("Found key %s" % row[1])
            row[4] = grades[row[1]]
    sheet.save_as(csv_path)

def calculate_grades():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True, nargs='+')
    parser.add_argument('--points', required=True, type=int)
    args = parser.parse_args()

    args.dir = ' '.join(args.dir)
    global TOTAL_POINTS
    TOTAL_POINTS = args.points

    if os.path.exists(args.dir):
        print("Found directory " + args.dir)
    else:
        raise Exception("Could not find inputed directory")
    csv_path = os.path.join(args.dir, 'grades.csv')
    if os.path.exists(csv_path):
        print("Found csv file")
    else:
        raise Exception("Could not find csv file")

    grades = dict()

    for directory in os.listdir(args.dir):
        if directory.endswith(".csv"):
            pass
        elif 'M' <= directory[0] <= 'W':
            match_obj = re.search(r"\((\w+)\)", directory)
            unique_id = match_obj.group(1)
            directory_path = os.path.join(args.dir, directory)
            deductions = calculate_point_deductions(directory_path)
            score = TOTAL_POINTS - deductions
            grades[unique_id] = score
        else:
            pass


    write_grades(csv_path, grades)



if __name__ == "__main__":
    calculate_grades()
