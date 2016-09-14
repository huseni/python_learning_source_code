__author__ = 'kathiria'

store = []


def sort_by_last_letter(string):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(string, key=last_letter)
