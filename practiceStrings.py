
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    
    for i in range(len(tableData)):
            for x in tableData[i]:
             if colWidths[i] < len(x):
                colWidths[i] = len(x)

    

    for x in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][x].rjust(colWidths[i]), end = ' ')
        print()
        x += 1
    

printTable()

