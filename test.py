from StudentsInMLOps import StudentsInMLOps

def test_enroll():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(10)
    assert classroom.getTotalStrength() == 10
    
def test_valid_drop_students():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(10)
    classroom.dropStudents(5)
    assert classroom.getTotalStrength() == 5

def test_invalid_drop_students():
    classroom = StudentsInMLOps()
    assert classroom.dropStudents(5) == "Count cannot be greater than total students"



def test_class_name():
    classroom = StudentsInMLOps()
    assert classroom.getClassName() == "MLOps SE"
