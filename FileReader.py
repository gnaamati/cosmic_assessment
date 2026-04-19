import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Parse a File")
    parser.add_argument("--file", required=True, help="input file")
    args = parser.parse_args()
    return args

#========================================= 
def slurp(file):
    rows = []
    try:
        with open (file, encoding="utf-8") as f:
            for line in f:
                rows.append(line.strip())
    except FileNotFoundError:
        exit(f"File not found: {file}")
    except OSError as e:
        exit(f"Error opening file {file}: {e}")
          
    return rows

#======================================== 
def line2dict(headers, line):
    headers_fields = headers.split("\t")
    line_fields    = line.split("\t")
  
    result = {}
    i = 0
    for header in headers_fields:
        header = header.lower()
        if i in range(len(line_fields)):
            result[header] = line_fields[i]
        else:
            result[header] = ''
        i += 1

    return result
#======================================== 

#======================================== 
def line2dict_csv(headers, line):
    headers_fields = headers.split(",")
    line_fields    = line.split(",")

    result = {}
    i = 0
    for header in headers_fields:
        header = header.lower()
        if i in range(len(line_fields)):
            result[header] = line_fields[i]
        else:
            result[header] = ''
        i += 1

    return result
#======================================== 

def file2dict(file):
    data = {}
    lines = slurp(file)
    for l in lines:
        if l:
            data[l] = '1'
    
    return data


