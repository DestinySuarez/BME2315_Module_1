import csv
class Patient:

    all_patients = []

    def __init__(self, donor_id: str, age_at_death: int, sex: str,
                 years_of_education: int, apoe_genotype: str,
                 cognitive_status: str, brain_weight: float,
                 abeta42: float):

        self.donor_id = donor_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.years_of_education = years_of_education
        self.apoe_genotype = apoe_genotype
        self.cognitive_status = cognitive_status
        self.brain_weight = brain_weight
        self.abeta42 = abeta42

        Patient.all_patients.append(self)

    def __repr__(self):

        return (
            f"{self.donor_id}: ({self.age_at_death} | {self.sex} | "
            f"{self.years_of_education} | {self.apoe_genotype} | "
            f"{self.cognitive_status} | {self.brain_weight} | "
            f"{self.abeta42})"
        )

    def get_age_at_death(self):
        return self.age_at_death

    @classmethod
    def instantiate_from_csv(cls, filename: str):

        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)

            for row in rows_of_patients:
                Patient(
                    donor_id=row["Donor ID"],
                    age_at_death=int(row["Age at Death"]),
                    sex=row["Sex"],
                    years_of_education=int(row["Years of education"]),
                    apoe_genotype=row["APOE Genotype"],
                    cognitive_status=row["Cognitive Status"],
                    brain_weight=float(row["Fresh Brain Weight"]) if row["Fresh Brain Weight"] != "Unavailable" else None,                    abeta42=float(row["ABeta42 pg/ug"])
                )
    @classmethod
    def filter(cls, list, donor_id="any", age_at_death="any",
               sex="any", years_of_education="any",
               apoe_genotype="any", cognitive_status="any",
               brain_weight="any", abeta42="any"):

        all_patients = list
        remove_list = []

        attr_list = (
            donor_id,
            age_at_death,
            sex,
            years_of_education,
            apoe_genotype,
            cognitive_status,
            brain_weight,
            abeta42
        )

        attr_name = (
            "donor_id",
            "age_at_death",
            "sex",
            "years_of_education",
            "apoe_genotype",
            "cognitive_status",
            "brain_weight",
            "abeta42"
        )

        for attr in range(len(attr_list)):

            if attr_list[attr] != "any":

                for patient in all_patients:

                    if getattr(patient, attr_name[attr]) != attr_list[attr]:

                        remove_list.append(patient)

                all_patients = [
                    patient for patient in all_patients
                    if patient not in remove_list
                ]

                remove_list.clear()

        return all_patients