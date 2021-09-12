"""Functions to parse a file containing student data."""


def all_houses(filename):
 
    houses = set()

    # TODO: replace this with your code
    file = open(filename, "r")

    for line in file:
      new_line = line.split("|")
      if new_line[2] != "":
        houses.add(new_line[2])
      
    return houses


def students_by_cohort(filename, cohort='All'):


  students = []

  cohort_data = open(filename)

  for line in cohort_data:
    first, last, _, _, cohort_name = line.rstrip().split('|')

    if cohort_name not in ('I', 'G') and cohort in ('All', cohort_name):
      students.append(f'{first} {last}')

  cohort_data.close()

  return sorted(students)


def all_names_by_house(filename):

  dumbledores_army = []
  gryffindor = []
  hufflepuff = []
  ravenclaw = []
  slytherin = []
  ghosts = []
  instructors = []

  # TODO: replace this with your code
  cohort_data = open(filename)

  for line in cohort_data:
    first, last, house, professor, cohort_name = line.rstrip().split('|')

    if house == "Dumbledore's Army":
      dumbledores_army.append(f'{first} {last}')
    elif house == "Gryffindor":
      gryffindor.append(f'{first} {last}')
    elif house == "Hufflepuff":
      hufflepuff.append(f'{first} {last}')
    elif house == "Ravenclaw":
      ravenclaw.append(f'{first} {last}')
    elif house == "Slytherin":
      slytherin.append(f'{first} {last}')
    elif cohort_name == "G":
      ghosts.append(f"{first} {last}")
    elif cohort_name == "I":
      instructors.append(f"{first} {last}")



  cohort_data.close()
  return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):

  all_data = []

  cohort_data = open(filename)

  for line in cohort_data:
    first, last, house, professor, cohort_name = line.rstrip().split("|")
    student = (f"{first} {last}", house, professor, cohort_name)
    all_data.append(student)

  cohort_data.close()
  return all_data



def get_cohort_for(filename, name):

  dict = {}

  cohort_data = open(filename)

  for line in cohort_data:
    first, last, _, _, cohort_name = line.rstrip().split("|")
    dict[f"{first} {last}"] = cohort_name
  
  cohort_data.close()

  return dict.get(name)




    


def find_duped_last_names(filename):
  """Return a set of duplicated last names that exist in the data.

  For example:
    >>> find_name_duplicates('cohort_data.txt')
    {'Creevey', 'Weasley', 'Patil'}

  Arguments:
    - filename (str): the path to a data file

  Return:
    - set[str]: a set of strings
  """

  all_names = []
  duplicated_names = set()

  cohort_data = open(filename)

  for line in cohort_data:
    first, last, _, _, _ = line.rstrip().split("|")
    if last not in all_names:
      all_names.append(last)
    else:
      duplicated_names.add(last)

  cohort_data.close()
  return duplicated_names  
  



  


def get_housemates_for(filename, name):

  houses_students = {}
  house_names_set = set()

  target = None

  cohort_data = open(filename)

  for line in cohort_data:
    first, last, house, professor, cohort_name = line.rstrip().split("|")

    if house in houses_students:
      houses_students[house].append(f"{first} {last}")
    else:
      houses_students[house] = [f"{first} {last}"]


  for key, value in houses_students.items():
    for i in value:
      if name == i:
        target = key

  for student in houses_students[target]:
    if student != name:
      house_names_set.add(student)

  cohort_data.close()
  return house_names_set


print(get_housemates_for("cohort_data.txt", "Hermione Granger"))

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

# if __name__ == '__main__':
#     import doctest

#     result = doctest.testfile('doctests.py',
#                               report=False,
#                               optionflags=(
#                                   doctest.REPORT_ONLY_FIRST_FAILURE
#                               ))
#     doctest.master.summarize(1)
#     if result.failed == 0:
#         print('ALL TESTS PASSED')
