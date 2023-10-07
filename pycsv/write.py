def create_result(filename,dict):
    with open(filename,"w") as f:
        f.write(",".join(dict.keys())+"\n")
        values = list(dict.values())
        for i in range(len(values[0])):
            row = [values[j][i] for j in range(len(values))]
            f.write(",".join(row)+"\n")
