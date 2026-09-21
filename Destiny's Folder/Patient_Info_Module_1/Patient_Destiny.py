# Import the csv module so patient data can be read from a CSV file.
import csv


# Define the Patient class to create patient objects from the dataset.
class Patient:

    all_patients = []

    # Initialize each Patient object with the selected attributes
    # that will be used for sorting, filtering, and data analysis.
    def __init__(self, donor_id, age_death, sex, education, years_education,
                 apoe, cognitive_status, age_dementia, thal,
                 abeta40, abeta42, ttau, ptau):

        self.donor_id = donor_id
        self.age_death = age_death
        self.sex = sex
        self.education = education
        self.years_education = years_education
        self.apoe = apoe
        self.cognitive_status = cognitive_status
        self.age_dementia = age_dementia
        self.thal = thal
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

        Patient.all_patients.append(self)

    # Return a readable description of a Patient object when it is printed.
    def __repr__(self):
            return f"Patient {self.donor_id}: {self.age_death} years old, {self.sex}, {self.cognitive_status}, {self.years_education} years of education"

    # Read the patient CSV file and create a Patient object for each row.
    # Numeric measurements are converted to floats for calculations and graphs.
    @classmethod
    def instantiate_from_csv(cls, filename):
        with open(filename, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                cls(
                    row["Donor ID"],
                    float(row["Age at Death"]),
                    row["Sex"],
                    row["Highest level of education"],
                    float(row["Years of education"]),
                    row["APOE Genotype"],
                    row["Cognitive Status"],
                    row["Age of Dementia diagnosis"],
                    row["Thal"],
                    float(row["ABeta40 pg/ug"]),
                    float(row["ABeta42 pg/ug"]),
                    float(row["tTAU pg/ug"]),
                    float(row["pTAU pg/ug"])
                    )

    # Filter patients using two attributes: years of education and cognitive status.
    # Return the patients who meet both conditions.
    @classmethod
    def filter_patients(cls, min_education, cognitive_status):
        filtered_patients = []

        for patient in cls.all_patients:
            if patient.years_education >= min_education and patient.cognitive_status == cognitive_status:
                filtered_patients.append(patient)

        return filtered_patients
    