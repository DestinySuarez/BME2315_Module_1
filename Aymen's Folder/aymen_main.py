from aymen_patient import *
import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy import stats


Patient.instantiate_from_csv(
    "/Users/destinysuarez/Desktop/Computational BME/Module 1/BME2315_Module_1/General Use/Metadata and Protein Data for Module 1.csv"
)

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
import matplotlib.pyplot as plt
import numpy as np
import statistics
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

t_stat, p_value = stats.ttest_ind(
    abeta42_female_patients,
    abeta42_male_patients
)

print("T-test:")
print("T-statistic:", t_stat)
print("P-value:", p_value)

patient_groups = ["Female Patients", "Male Patients"]
mean_abeta42 = [female_mean, male_mean]
stdev_abeta42 = [female_stdev, male_stdev]

yerr = [np.zeros(len(mean_abeta42)), stdev_abeta42]

plt.bar(
    patient_groups,
    mean_abeta42,
    yerr=yerr,
    capsize=10,
    color=["pink", "blue"]
)

t_stat, p_value = stats.ttest_ind(
    abeta42_female_patients,
    abeta42_male_patients
)

plt.text(
    0.5,
    350,
    f"T-test p-value = {p_value:.4f}",
    ha="center"
)

plt.title("Average ABeta42 Levels in Patients with Dementia")
plt.xlabel("Sex")
plt.ylabel("Average ABeta42 (pg/ug)")
plt.show()
age_at_death = []
abeta42_levels = []

for patient in Patient.all_patients:
    age_at_death.append(patient.age_at_death)

for patient in Patient.all_patients:
    abeta42_levels.append(patient.abeta42)

X = age_at_death
y = abeta42_levels

plt.scatter(X, y, color="purple")

plt.xlabel("Age at Death")
plt.ylabel("ABeta42 Level (pg/ug)")
plt.title("ABeta42 Levels vs. Age at Death")

plt.show()