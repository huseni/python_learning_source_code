__author__ = 'kathiria'

def parse(lines, types, names):
    records = []

    for line in lines:
        fields = line.split()
        records = { name:func(val)
                    for name, func, val in zip(names, types, fields)}
        records.append(record)
    return records