"""An example of utils with three defined functions."""
__author__ = "730528983"


# First function:
# ls means list.
def only_evens(ls: list[int]) -> list[int]:
    """There is a list which inludes only even integers."""
    dw: list[int] = []
    
    for item in ls:
        if item % 2 == 0:
            dw.append(item)
    return dw


# Second funxtion:
# si means start integer. ei means end integer.
def sub(ls: list[int], si: int, ei: int) -> list[int]:
    """This sub can locate where you want to print out."""
    if si < 0:
        si = 0
    if ei > len(ls):
        ei = len(ls)
    
    dx: list[int] = list()
    i: int = si
    while i < ei:
        dx.append(ls[i])
        i += 1
    return dx


# Third Function:
def concat(first: list[int], second: list[int]) -> list[int]:
    """This will generate a new list which contains all of the elements of both first and the second list."""
    dy: list[int] = list()
    for item in first: 
        dy.append(item)

    for item in second:
        dy.append(item)
    return dy
   