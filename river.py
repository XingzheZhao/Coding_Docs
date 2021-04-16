matrix = [
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
]

node = None
if node is None:
    print('not none')

class temp:
    val = 10

    def showValue(self):
        global val
        val = 20
        print(val)

a = temp()
a.showValue()