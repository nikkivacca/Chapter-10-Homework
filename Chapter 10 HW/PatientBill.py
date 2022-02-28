import ProcedureClass as pr
import PatientClass as pc 

def main():


    patient = pc.Patient(1, "Matt Jones", "123 Main St, Waco, TX 76706", "234-555-7415", "TRUE")
 
    physical_exam = pr.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)

    MRI_exam = pr.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)

    CT_scan = pr.Procedure("CT Scan", "2/15/2022", "Dr. Drey", 1200, 2)


    print("\n*** Patient Bill ***")
    print(patient)
    print()
    print(physical_exam)
    print()
    print(MRI_exam)
    print()
    print(CT_scan)
    print() 
    ##print("Total charge is: " + sum(physical_exam.charge, MRI_exam.charge, CT_scan.charge))

main()