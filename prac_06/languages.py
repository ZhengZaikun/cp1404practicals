from prac_06.programming_language import ProgrammingLanguage
def main():
    """Input and store the information for each subject, then print the dynamic subjects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    subjects =[python, ruby, visual_basic]
    print_dynamic_subjects(subjects)

def print_dynamic_subjects(subjects):
    """Printing subjects that are printed are dynamic."""
    print("The dynamically typed languages are:")
    for subject in subjects:
        if subject.is_dynamic():
            print(subject.name)

main()