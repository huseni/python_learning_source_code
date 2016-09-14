__author__ = 'kathiria'


class DictError(Exception):
    pass


class distdict(dict):
    def __setitem__(self, key, value):
        try:
            value_index = self.values().index(value)

            existing_key = self.keys()[value_index]
            if existing_key != key:
                raise DictError("This value already %s" % str(self[existing_key]))
        except ValueError:
            pass

        super(distdict, self).__setitem__(key, value)

my = distdict()
my['key'] = 'value'
my['other_key'] = 'value1'
print(my)
