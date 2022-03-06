from functools import reduce

note = [8, 6, 8, 9]

note_avg = reduce(lambda y, z:(y+z) , note) / len(note)

print(note_avg)

