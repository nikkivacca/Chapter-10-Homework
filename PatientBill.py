import ProcedureClass as pr
import PatientClass as pc 

def main():


    patient = pc.Patient(1, "Matt Jones", "123 Main St, Waco, TX 76706", "234-555-7415", "TRUE")
 
    procedure1 = pr.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)

    procedure2 = pr.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)

    procedure3 = pr.Procedure("CT Scan", "2/15/2022", "Dr. Drey", 1200, 2)


    print("\n*** Patient Bill ***")
    print("Name: ", patient.get_name())
    print("Address: ", patient.get_address())
    print("Phone: ", patient.get_phone())

    procedures_list = [procedure1,procedure2,procedure3]
    total_charge = 0 
    for a in procedures_list:
        if a.get_patient_ID() == patient.get_ID():
            print()
            print("Procedure: ", a.get_proc_name())
            print("Date: ", a.get_date())
            print("Practitioner: ", a.get_practitioner())
            print("Charge: $", format(a.get_charge(), ',.2f'))
            print()
            total_charge += a.get_charge()

    if patient.get_veteran_status() == "TRUE":
        total_charge = .6*total_charge
        print("Total charge is: $", format(total_charge, ',.2f'))
    else: 
        print("Total charge is: $", format(total_charge, ',.2f'))

main()