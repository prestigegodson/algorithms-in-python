def reverse_string(strings):

    if len(strings) == 1:
        return strings[0]

    length = len(strings) - 1

    return strings[-1] + reverse_string(strings[0:length])


print(reverse_string('AB'))
