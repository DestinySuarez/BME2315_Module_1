# Import the Patient class and modules needed to read and analyze the dataset.
from Patient_Destiny import Patient
import csv
import matplotlib.pyplot as plt
import numpy as np

# Create Patient objects from every row in the patient CSV dataset.
Patient.instantiate_from_csv("/Users/destinysuarez/Desktop/Computational BME/Module 1/Patient_Info_Module_1/Metadata and Protein Data for Module 1_Patient.csv")

# Print the first five Patient objects to verify that the CSV was loaded correctly.
print(Patient.all_patients[:5])

# Sort patients based on years of education
Patient.all_patients.sort(key=lambda patient: patient.years_education)

# Print the sorted patients
print("\nPatients sorted by years of education:")
print(Patient.all_patients[:10])

# Filter patients with at least 16 years of education and no dementia
filtered_patients = Patient.filter_patients(16, "No dementia")

print("\nPatients with at least 16 years of education and no dementia:")
print(filtered_patients)

# Create two groups based on cognitive status
no_dementia = [patient.years_education for patient in Patient.all_patients
               if patient.cognitive_status == "No dementia"]

dementia = [patient.years_education for patient in Patient.all_patients
            if patient.cognitive_status == "Dementia"]

# Calculate the mean and standard deviation for each group
means = [np.mean(no_dementia), np.mean(dementia)]
standard_deviations = [np.std(no_dementia), np.std(dementia)]

# Create a bar graph comparing mean years of education between the two groups.
# Error bars represent one standard deviation.
groups = ["No dementia", "Dementia"]

plt.bar(groups, means, yerr=standard_deviations, capsize=5)

plt.xlabel("Cognitive Status")
plt.ylabel("Mean Years of Education")
plt.title("Mean Years of Education by Cognitive Status")
plt.show()

# Create a scatter plot of years of education and age at death
education = [patient.years_education for patient in Patient.all_patients]
age_at_death = [patient.age_death for patient in Patient.all_patients]

plt.scatter(education, age_at_death)

plt.xlabel("Years of Education")
plt.ylabel("Age at Death")
plt.title("Years of Education vs. Age at Death")
plt.show()