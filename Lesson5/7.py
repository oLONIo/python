from json import dumps
results = [{}, {'average_profit': 0}]
ct = 0
with open('test7.txt', 'r') as lol:
    for line in lol:
        i = line.split(' ')
        if int(i[2]) - int(i[3]) >= 0:
            results[1]['average_profit'] = results[1]['average_profit'] + int(i[2]) - int(i[3])
            ct += 1
        results[0][i[0]] = int(i[2]) - int(i[3])
    results[1]['average_profit'] = results[1]['average_profit'] / ct
print(results)