COLOR_NAMES = {"aliceblue":"#f0f8ff", "amaranth":"#e52b50", "amber":"#ffbf00", "amethyst":"#9966cc",
               "antiqueWhite":"#faebd7", "apricot":"#fbceb1", "aqua":"#00ffff", "army green":"#4b5320",
               "asparagus":"#87a96b", "aureolin":"#fdee00", "beaver":"#9f8170", "beige":"#f5f5dc"}
color_name = input("What color would you like to see? ").lower()
while color_name != "":
    try:
        print(COLOR_NAMES[color_name])
    except KeyError:
        print("Sorry, your color name is not in the dictionary of colors.")
    color_name = input("What color would you like to see? ").lower()