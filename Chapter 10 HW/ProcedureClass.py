class Procedure:

    def __init__(self, proc_name, date, practitioner, charge, patient_ID):
        self.__proc_name = proc_name 
        self.__date = date
        self.__practitioner = practitioner 
        self.__charge = charge 
        self.__patient_ID = patient_ID 


    def get_proc_name(self):
        return self.__proc_name
    
    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charge(self):
        return self.__charge

    def get_patient_ID(self):
        return self.__patient_ID
        