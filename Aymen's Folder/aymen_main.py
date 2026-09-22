import matplotlib.pyplot as plt
import numpy as np
import statistics
from pathlib import Path
from sklearn.linear_model import LinearRegression
from aymen_patient import *


# Find the CSV file inside Aymen's Folder
csv_file = Path(__file__).parent / "Metadata and Protein Data for Module 1.csv"

Patient.instantiate_from_csv(csv_file)


Patient.all_patients.sort(
    key=Patient.get_age_at_death,
    reverse=False
)


for patient in Patient.all_patients:
    print(patient)


female_dementia_patients = Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia"
)


print("Female patients with dementia:")


for patient in female_dementia_patients:
    print(patient)


abeta42_female_patients = []
abeta42_male_patients = []


for patient in Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia"
):
    abeta42_female_patients.append(patient.abeta42)


for patient in Patient.filter(
    Patient.all_patients,
    sex="Male",
    cognitive_status="Dementia"
):
    abeta42_male_patients.append(patient.abeta42)


female_mean = statistics.mean(abeta42_female_patients)
male_mean = statistics.mean(abeta42_male_patients)


female_stdev = statistics.stdev(abeta42_female_patients)
male_stdev = statistics.stdev(abeta42_male_patients)


patient_groups = ["Female Patients", "Male Patients"]
mean_abeta42 = [female_mean, male_mean]
stdev_abeta42 = [female_stdev, male_stdev]


plt.bar(
    patient_groups,
    mean_abeta42,
    yerr=stdev_abeta42,
    capsize=10,
    color=["pink", "blue"]
)


plt.title("Average ABeta42 Levels in Patients with Dementia")
plt.xlabel("Sex")
plt.ylabel("Average ABeta42 (pg/ug)")


plt.savefig(Path(__file__).parent / "abeta42_bar_graph.png")
plt.show()
plt.close()


age_at_death = []
abeta42_levels = []


for patient in Patient.all_patients:
    age_at_death.append(patient.age_at_death)
    abeta42_levels.append(patient.abeta42)


X = np.array(age_at_death).reshape(-1, 1)
y = np.array(abeta42_levels)


model = LinearRegression()
model.fit(X, y)


plt.scatter(
    age_at_death,
    abeta42_levels,
    color="purple"
)


plt.plot(
    age_at_death,
    model.predict(X),
    color="red"
)


plt.xlabel("Age at Death")
plt.ylabel("ABeta42 Level (pg/ug)")
plt.title("ABeta42 Levels vs. Age at Death")


plt.savefig(Path(__file__).parent / "abeta42_regression_graph.png")
plt.show()
plt.close()