class StudentsInMLOps:
    def __init__(self):
        self.total_students = 0
        self.class_name = "MLOps SE"

    def enrollStudents(self, count):
        self.total_students += count
        
    def dropStudents(self, count):
        if count > self.total_students:
            return ("Count cannot be greater than total students")
        self.total_students -= count
        

    def getTotalStrength(self):
        return self.total_students

    def getClassName(self):
        return self.class_name
    

    

