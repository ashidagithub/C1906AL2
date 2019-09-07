

# Weekly life at Mon. to Fri.
for myday in range(1, 6):
    print('Week schedule------------')
    print('Weekday (%d) is a class day !' % myday)

    # daily life at Mon. to Fri.
    for mytime in range(0, 7):
        action = '  %02dClock... Sleeping' % mytime
        print(action)

    for mytime in range(7, 17):
        action = '  %02dClock... Study at school' % mytime
        print(action)

    for mytime in range(17, 25):
        action = '  %02dClock... Study at Home' % mytime
        print(action)

# Life for weekend
for myday in range(6, 8):
    if myday == 6:
        print('Weekday (%d) is a Python day !' % myday)
    if myday == 7:
        print('Weekday (%d) , Finally, I can have a rest day !' % myday)
