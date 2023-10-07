def create_dict(filename):
    with open(filename) as csv_file:
        header = csv_file.readline().strip().split(',')
        dict = {}
        
        for line in csv_file:
            values = line.strip().split(',')
            for i in range(len(header)):
                if header[i] in dict:
                    dict[header[i]] = dict[header[i]] + [values[i]]
                else:
                    dict[header[i]] = [values[i]]
        return dict
