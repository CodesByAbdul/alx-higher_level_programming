for tens in range(100):
    for units in range(tens + 1, 10):
        print(f"{tens}{units}", end="\n" if tens == 8 and units == 9 else ", ")
