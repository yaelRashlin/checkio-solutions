def sun_angle(time):
    h, m = [int(i) for i in time.split(":")]
    if h < 6 or h > 18:
        return  "I don't see the sun!"
    
    d = {}
    minutes = 0
    for i in range(6,19):
        d[i] = minutes
        minutes = minutes + 60
       
    total_min = d[h] + m
    if total_min > 720:
       return  "I don't see the sun!"
       
    return 0.25 * total_min
    
    
if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
