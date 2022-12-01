




def QSpartition(A,start, end):
    x = A[end]
    lrbi = start - 1
    for ti in range(start, end):
        if A[ti] <= x:
            lrbi += 1
            (A[lrbi], A[ti]) = (A[ti], A[lrbi])
    (A[lrbi + 1], A[end]) = (A[end], A[lrbi + 1])
    return lrbi + 1



def QSquicksort(A,start,end):
    if start < end:
        pivot = QSpartition(A,start,end)
        QSquicksort(A,start,pivot - 1)
        QSquicksort(A,pivot + 1,end)



a = [38,2,55,98,14,37,63,70,91,55,23,7,63,12,95,9,6,81,25,42,79,5,24,64,12,80,3,9,95,70,72,76,92,89,59,97,36,87,76,49,32,61,42,41,8,78,32,69,31,95]

print(a)
QSquicksort(a, 0, len(a) - 1)
print(a)
