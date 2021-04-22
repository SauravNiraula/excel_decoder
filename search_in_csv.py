import csv

def open_files(*args):
    if len(args) <= 0:
        return "No arguments"
    final_csv = []
    no_of_cols = 0
    i = 0
    for each in args:
        with open(each, 'r') as csvfile:
            results = list(csv.reader(csvfile))
            if i==0:
                no_of_cols = len(results[0])
                final_csv += results
                i += 1
            else:
                if no_of_cols != len(results[0]):
                    print("skipped file ' " + each + " '")
                    continue
                final_csv += results[1:]

    return final_csv

def search(results, dict):
    columns = results[0]
    provided_cols = dict.keys()
    try:
        provided_cols_index = [ columns.index(each) for each in provided_cols ] # use regex
    except ValueError:
        print ("provided column is not accepted")
        return []
    found = []
    for each in results[1:]:
        has_result = True
        for i in provided_cols_index:
            if each[i] != dict[columns[i]]:
                has_result = False 
                break
        if has_result:
            found.append(each)

    return found


found = search(open_files('result.csv', 'result1.csv'), {'Name of Student': 'Romeo'})
print(found)