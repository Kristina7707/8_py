def write_file(data):
    with open('students.csv','a') as file:
        file.writelines(data)
          
def read_file():
    with open('students.csv','r') as file:
        return file.readlines()