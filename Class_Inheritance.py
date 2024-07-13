class Device: 

    def __init__(self, name, connected_by):
        
        self.name = name 
        self.connected_by = connected_by
        self.connected = True


    def __str__(self):
        return f'Name is {self.name} and is connected by : {self.connected_by}'
    

    def disconnect(self):
        self.connected = False
        print('Disconnected')


class Printer(Device):

    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_capacity = capacity


    def __str__(self):
        return f'{super().__str__()}, and remaining pages : {self.remaining_capacity}'
    
    def print(self,pages):
        if not self.connected:
            print('Printer is not connected')
            return
        print(f'Printing {pages} pages')
        self.remaining_capacity -= pages



printer = Printer('Printer', 'USB', 1000)
print(printer)
printer.print(100)
print(printer)
printer.print(200)
print(printer)