from project_management import Project
from operator import attrgetter
import datetime
FILE_NAME = "projects.txt"
def main():
    """The file content is displayed or modified
    by reading it to generate a list, and finally the modified list is written back to the file."""
    projects = []
    print("Welcome to Pythonic Project Management\nLoaded 5 projects from projects.txt")
    options = input("(L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
                    "- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>>").upper()
    projects = load_projects(FILE_NAME, projects)
    while options != "Q":
        if options == "D":
            display_projects(projects)
        elif options == "F":
            date_string = input("Show projects that start after date (dd/mm/yy): ")  # e.g., "30/9/2022"
            filer_date = judge_date(date_string)
            # print(f"That day is/was {date.strftime('%A')}")
            # print(date.strftime("%d/%m/%Y"))
            projects_after_date = filter_projects_by_date(projects, filer_date)
            sorted_projects = sorted(projects_after_date, key=attrgetter('date'))
            print_projects(sorted_projects)
        elif options == "A":
            print("Let's add a new project")
            name = input("Name: ")
            name = get_valid_name(name)
            date_string = input("Start date (dd/mm/yy): ")
            date_string = get_valid_date(date_string)
            new_project = add_new_project(name, date_string)
            projects.append(new_project)
        elif options == "U":
            projects = update_projects(projects)
        else:
            print("Invalid option")

        options = input("(L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
                        "- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>>").upper()
    judgement = input("Would you like to save to projects.txt? ").upper()
    if judgement != "N":
        save_projects(FILE_NAME, projects)
    print("Thank you for using custom-built project management software.")

def load_projects(file_name, projects):
    """Open file of projects.txt"""
    is_valid = False
    while not is_valid:
        try:
            with open(file_name, "r") as in_file:
                next(in_file)
                for line in in_file:
                    line = line.strip().split("\t")
                    if len(line) == 5:
                        date_string = line[1]
                        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
                        projects.append(Project(line[0], date, int(line[2]), float(line[3]),int(line[4])))
            is_valid = True
        except FileNotFoundError:
            print("Project file not found")
            file_name = input("Enter file name: ")
    return projects

def save_projects(file_name, projects):
    """Save projects"""
    is_valid = False
    while not is_valid:
        try:
            with open(file_name, "w") as out_file:
                out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
                for line in projects:
                    date_string = line.date.strftime("%d/%m/%Y")
                    project = [line.name, date_string, str(line.priority), str(line.cost), str(line.completion_percentage)]
                    project = "\t".join(project) + "\n"
                    out_file.write(project)
            is_valid = True
        except FileNotFoundError:
            print("Project file not found")


def display_projects(projects):
    """Display the information of projects"""
    incomplete_projects = [project for project in projects if int(project.completion_percentage) < 100]
    completed_projects = [project for project in projects if int(project.completion_percentage) == 100]
    incomplete_projects.sort()
    completed_projects.sort()
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed projects: ")
    for project in completed_projects:
        print(f"\t{project}")

def print_projects(project):
    """Print projects"""
    for term in project:
        print(term)

def filter_projects_by_date(projects, filer_date):
    """Filter projects by date"""
    projects_after_date = [project for project in projects if project.date >= filer_date]
    return projects_after_date

def judge_date(date_string):
    """Judge date of project"""
    is_valid = False
    while not is_valid:
        try:
            date_string = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid = True
        except ValueError:
            print("Invalid Date")
            date_string = input("Show projects that start after date (dd/mm/yy): ")
    return date_string


def add_new_project(name, date_string):
    """Add new project input projects"""
    is_valid = False
    while not is_valid:
        try:
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            percent_complete = int(input("Completion percentage: "))
            is_valid = True
        except ValueError:
            print("Invalid Priority")
    return Project(name, date_string, priority, cost_estimate, percent_complete)

def is_completed(self):
    """Return True if the project is 100% complete."""
    return self.completion_percentage == 100

def update_projects(projects):
    """Select a project and update its completion percentage and priority."""
    for i,project in enumerate(projects,0):
        print(f"{i} {project}")
    try:
        project_choice=int(input("Project choice:"))
        if project_choice >= 0 and project_choice < len(projects) -1:
            project_to_update = projects[project_choice]
            print(project_to_update)
            new_percentage = input(f"New percentage: ")
            if new_percentage:
                try:
                    percentage_value = int(new_percentage)
                    if 0 <= percentage_value <= 100:
                        project_to_update.completion_percentage = percentage_value
                    else:
                        print("Invalid percentage: must be between 0 and 100.")
                except ValueError:
                    print("Invalid percentage: must be a whole number.")
            new_priority = input(f"New priority: ")
            if new_priority:
                try:
                    priority_value = int(new_priority)
                    if priority_value > 0:
                        project_to_update.priority = priority_value
                    else:
                        print("Invalid priority: must be greater than 0.")
                except ValueError:
                    print("Invalid priority: must be a whole number.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid number.")
    return projects

def get_valid_name(name):
    """Get a valid name from the user."""
    while len(name.strip()) == 0:
        print("Name cannot be empty.")
        name = input("Name:")
    return name

def get_valid_date(date_string):
    """Get a valid date object from user input, retrying until format is correct."""
    is_valid = False
    date_object = 0
    while not is_valid:
        try:
            date_object = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid = True
        except ValueError:
            print(f"Invalid date format. Please use {"%d/%m/%Y"}.")
            date_string = input("Show projects that start after date (dd/mm/yy): ")
    return date_object

main()