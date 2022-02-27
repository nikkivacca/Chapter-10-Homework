import ProcedureClass as pr
import PatientClass as pc 

def main():


    patient = pc.Patient(patient_ID, name, address, phone, veteran_status)
    patient_ID = 1
    name= "Matt Jones"
    address = "123 Main St, Waco, TX 76706"
    phone = "254-555-7415"
    veteran_status = "TRUE"


    physical_exam = pr.Procedure("Physical Exam", "2/15/2022", "Dr.Irvine", 250, 1)

    MRI_exam = pr.Procedure("MRI", "2/15/2022", "Dr.Hamilton", 1500, 1)

    CT_scan = pr.Procedure("CT Scan", "2/15/2022", "Dr.Drey", 1200, 2)


    print("*** Patient Bill ***")
    print(patient)
    print()
    print(physical_exam)
    print()
    print(MRI_exam)
    print()
    print(CT_scan)

