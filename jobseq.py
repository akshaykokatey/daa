# P3 Job sequence
def printjobschedule(array, t):

    m = len(array)

    for j in range(m):
        for q in range(m - 1 - j):
            if array[q][2] < array[q + 1][2]:
                array[q], array[q + 1] = array[q + 1], array[q]

    res = [False] * t

    job = ['-1'] * t

    for q in range(len(array)):

        # Find a free slot

        for q in range(min(t - 1, array[q][1] - 1), -1, -1):

            if res[q] is False:
                res[q] = True
                job[q] = array[q][0]
                break

    # print
    print(job)

array = [['a', 2, 10],
       ['b', 1, 50],
       ['c', 2, 9],
       ['d', 3, 26],
       ['e', 2, 18]]

print("Maximum profit sequence of jobs is- ")
printjobschedule(array, 3)