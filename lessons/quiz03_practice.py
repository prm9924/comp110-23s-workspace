class Course:
    """Models idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def __init__(self, name, level, prereqs):
        self.name = name
        self.level = level
        self.prerequisites = prereqs
    
    def is_valid_course(self, prereq: str) -> bool:
        """This method returns true if the course (self) is 400+ in level and has the prereq string as one of its prerequisites."""
        if self.level >= 400:
            if prereq in self.prerequisites:
                return True
            else:
                return False
        else:
            return False


def find_courses(courses: list[Course], prereq: str) -> list[str]:
    """Returns a list of the courses in the input list that are 400+ in level and have the prereq string as one of their prerequisites."""
    result: list[str] = []
    
    for course in courses:
        if course.level >= 400:
            if prereq in course.prerequisites:
                result.append(course.name)
    
    return result


stor215: Course = Course('discrete', 215, ['precalc', 'algebra'])
calc233: Course = Course('calc3', 233, ['precalc', 'algebra', 'calc1'])
stor435: Course = Course('probability', 435, ['precalc', 'stat'])
biol500: Course = Course('bio', 500, ['bio101'])

print(find_courses([stor215, calc233, stor435, biol500], 'precalc'))
print(stor435.is_valid_course('precalc'))