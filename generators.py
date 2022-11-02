import string

# letters is becoming an generator function
# you can iteract wit next
# every function that uses yield instead of return is a generator function
def letters():
    for c in string.ascii_lowercase:
        yield c     # yield interrupts the progress and return to the caller
        # When a generator calls yield, #
        # it momentarily pass control back to the code looping over the generator values.
                    # when another yield is called it continues where it has stopped
                    # 

for letter in letters():
    print(letter)


'''
container.__iter__()
    Returns an iterator oobject

iterator.___next__()
    Returns the next item from the container
    If theres no further item a "StopIteration" exception is raised
'''
print("\n\n\n\nIterator sample")
usernames = ("max", "rob", "juba", "cuca")
looper = iter(usernames)

print(next(looper))
print(next(looper))
print(next(looper))
print(next(looper))
print("StopIteration exception is raised on the next iteration: \n\n\n\n\n")

print(next(looper))


