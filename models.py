import csv
from datetime import datetime


class Data:
    def __init__(self, filename="data.csv"):
        self._filename = filename
        self._data, self.line_count = self._read()
        self._header = self._read_header()

    def writeRecord(self, **items):
        args_dict = {}
        items_dict = items

        for item in self._header:
            if item not in items_dict and item != 'date':
                raise AttributeError(f"required argument '{item}' missing")
            if item == 'date':
                args_dict[item] = datetime.today().strftime('%Y-%m-%d')
            else:
                args_dict[item] = items_dict[item]
                del items_dict[item]
        if items_dict != {}:
            for item in items_dict.keys():
                print(f"[WARN] '{item}' does not exist in file HEADER. Skipping write")  # noqa: E501

        self._write(args_dict)

    def _read(self):
        line = 0
        data_ret = []
        with open(self._filename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_ret.append(row)
                line += 1
        return data_ret, line

    def _read_header(self):
        with open(self._filename, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader, None)
        return header

    def _write(self, data_dict):
        labels = data_dict.keys()
        with open(self._filename, mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=labels)
            writer.writerow(data_dict)

    @property
    def data(self):
        return getattr(self, '_data')
