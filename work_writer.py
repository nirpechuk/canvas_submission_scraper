import csv

def work(nerd_name, delta_ongoing=0, delta_finished=0):
    operating_column = 0

    with open("work.csv", newline="") as workfile:
        workreader = csv.reader(workfile, delimiter=',')
        data = list(workreader)

        for i in range(len(data[0])):
            if data[0][i] == nerd_name:
                operating_column = i
                break
        if operating_column == 0:
            raise Exception("word nerd not found: " + nerd_name)


    with open("work.csv", "w", newline="") as workfile:
        workwriter = csv.writer(workfile, delimiter=',')
        workwriter.writerow(data[0])
        data[1][operating_column] = str(int(data[1][operating_column]) + delta_ongoing)
        workwriter.writerow(data[1])
        data[2][operating_column] = str(int(data[2][operating_column]) + delta_finished)
        workwriter.writerow(data[2])

        return int(data[1][operating_column]), int(data[2][operating_column])
