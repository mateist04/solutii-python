from employee import Employee 

class Manager(Employee): 
    mgr_count = 0  

    def __init__(currentObj, nume, salariu, departament):
        super().__init__(nume, salariu) 
        currentObj.departament = "f09" + departament
        Manager.mgr_count += 1


    def display_employee(currentObj):
        print(f"Name: {currentObj.name}")


    def __del__(currentObj):
        Manager.mgr_count -= 1
        super().__del__()

#creez 4 obiecte(instante) ale clasei Manager
manager1 = Manager("Teodora", 8456, "HR")
manager2 = Manager("Emilian", 9520, "IT")
manager3 = Manager("Mihnea", 9000, "Marketing")
manager4 = Manager("Nicu", 8000, "Finance")

print("Afisarea managerilor: ")
manager1.display_employee()
manager2.display_employee()
manager3.display_employee()
manager4.display_employee()


employee1 = Employee("Iulian", 50000) # obiecte ale clasei Employee pentru comparatia output-ului metodelor de print
employee2 = Employee("Maricica", 55000)


print("\nAfisare pentru angajati: ")
employee1.display_employee() #aici apelez metoda de afisare pentru obiectele din clasa Employee
employee2.display_employee()

print("\nNumarul total de angajati: ", Employee.empCount)
print("\nNumarul total de manageri: ", Manager.mgr_count)

#EXPLICATII:

# X = 6 (Stoian), deci X%3 = 0 => modific metoda display_employee astfel incat sa afiseze doar numele angajatului;
# Y = 12 (Matei Eugeniu), Y/3 = 4 obiecte pentru clasa Manager;
#importarea clasei Employee din fisierul employee.py;
#creez clasa Manager care mostenseste clasa Employee;
#variabila care retine numarul managerilor;
# functia __init__ = constructorul standard din python;
    #mereu primul argument dintre paranteze este obiectul curent, in cazul meu: currentObj, normal se denumeste
    #self, insa el poate lua orice nume atat timp cat este primul argument al functiei;
    #super() extinde functionalitatea metodelor din clasele parinte, fara a le suprascrie complet;
#functia display_employee este suprascrisa pentru a afisa doar numele managerului;
    #f din instructiunea (f"Name: {currentObj.name}") indica faptul ca sirul este formatat si poate contine expresii
    #python in interiorul acoladelor, daca scriam fara acolade se afisa chiar "currentObj.name"
#functia __del__ este de fapt un destructor care este apelata cand se sterge un obiect
    #se decrementeaza contorul de manageri
    #se apeleaza destructorul clasei parinte pentru a actualiza "empCount"
    
