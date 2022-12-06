# Camryn Hurley

def count_hashtag(string, tag):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(tag)] == tag:
            total += 1
            index += len(tag)
        else:
            index += 1
    print(total)

hashtag = '#'

test = '''
    #so cool, #slay
    im so ready for #break
    '''
count_hashtag(test, hashtag)
