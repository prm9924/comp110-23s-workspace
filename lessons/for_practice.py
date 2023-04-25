def pets_list():
    """Uses for loop to say good boy to every pet"""
    pets: list[str] = ["Louie", "Bo", "Bear"]

    for animal in pets:
        print(f"Good boy, {animal}!")


def tuples_intro():
    """Tuples"""
    three_d_coordinate: tuple[float, float, float] = (1.0, 1.0, 1.0)

    Player = tuple[str, int]
    lebron: Player = ("James", 6)
    mj: Player = ("Jordan", 23)

    print(mj)


def range_intro():
    """range() is used to as intervals. Includes first number, does not include second"""
    names = ["Alyssa", "Janet", "Vrinda"]

    for i in range(0, 3):
        print(f"{i}: {names[i]}")

range_intro()