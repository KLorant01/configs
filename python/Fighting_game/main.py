import Creation
def init():
    crew: list = [0,0,0]
    professions: list = ['commander', 'biologist', 'marin']
    for i in range(3):
        crew[i] = Creation.Crew_Member
        Creation.Crew_Member.make(crew[i], profession=professions[i], skill_points=10, dice=4)
    print(crew)


def main():
    while 1:
        pass


if __name__ == "__main__":
    init()
    main()