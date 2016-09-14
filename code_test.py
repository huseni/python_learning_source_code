    def remove_data(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())