# Define a class named American which has a static method called printNationality.

class American:
    @staticmethod
    def printNationality(self, nationality):
        return nationality
    

american = American()

print(American.printNationality(american, 'American'))

