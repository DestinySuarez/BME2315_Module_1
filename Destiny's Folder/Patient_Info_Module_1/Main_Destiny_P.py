# Import the Patient class and modules needed to read and analyze the dataset.
from sklearn.linear_model import LinearRegression
import pandas as pd
from Patient_Destiny import Patient
import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Create Patient objects from every row in the patient CSV dataset.
from pathlib import Path

csv_file = Path(__file__).parent / "Metadata and Protein Data for Module 1_Patient.csv"
Patient.all_patients.clear()  # empty the list first so re-running doesn't add duplicates
Patient.instantiate_from_csv(csv_file) # Print the first five Patient objects to verify that the CSV was loaded correctly.
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

# Perform an independent samples t-test
t_stat, p_val = stats.ttest_ind(no_dementia, dementia)

# Print the t-test results
print(f't_stat = {t_stat}, p_val = {p_val}')

# Create a bar graph comparing mean years of education
groups = ["No dementia", "Dementia"]

fig, ax = plt.subplots()

ax.bar(groups, means, yerr=standard_deviations, capsize=5)

ax.set_xlabel("Cognitive Status")
ax.set_ylabel("Mean Years of Education")
ax.set_title("Mean Years of Education by Cognitive Status")

# Add T-test results to the graph
ax.text(
    0.5, 19.5,
    f"T-test: t = {t_stat:.2f}, p = {p_val:.3f}",
    ha="center",
    fontsize=12
)

plt.show()



# T-test comparing years of education between cognitive status groups
education_no_dementia = [
    patient.years_education
    for patient in Patient.all_patients
    if patient.cognitive_status == "No dementia"
]

education_dementia = [
    patient.years_education
    for patient in Patient.all_patients
    if patient.cognitive_status == "Dementia"
]

# Run the independent samples T-test
t_stat, p_val = stats.ttest_ind(
    education_no_dementia,
    education_dementia,
    equal_var=False
)

print("\nT-test results:")
print("T-statistic:", t_stat)
print("P-value:", p_val)

# Create a scatter plot of years of education and age of dementia diagnosis

# Create a scatter plot of years of education and age of dementia diagnosis

dementia_patients = [
    patient
    for patient in Patient.all_patients
    if patient.cognitive_status == "Dementia"
    and patient.age_dementia is not None
]

education = [
    patient.years_education
    for patient in dementia_patients
]

age_diagnosis = [
    patient.age_dementia
    for patient in dementia_patients
]

X = np.array(education).reshape(-1, 1)
y = np.array(age_diagnosis)

model = LinearRegression()
model.fit(X, y)

r_value, correlation_p = stats.pearsonr(education, age_diagnosis)

print("Regression slope:", model.coef_[0])
print("Regression intercept:", model.intercept_)
print("R-squared:", model.score(X, y))
print("Pearson correlation:", r_value)
print("Correlation p-value:", correlation_p)

plt.figure()

plt.scatter(
    education,
    age_diagnosis
)

# Sort education values so the regression line draws correctly
sort_indices = np.argsort(education)
X_sorted = X[sort_indices]

plt.plot(
    X_sorted,
    model.predict(X_sorted)
)

# Add regression results to the graph
plt.text(
    0.05, 0.95,
    f"r = {r_value:.2f}, p = {correlation_p:.3f}, R² = {model.score(X, y):.3f}",
    transform=plt.gca().transAxes,
    va="top"
)

plt.xlabel("Years of Education")
plt.ylabel("Age at Dementia Diagnosis")
plt.title("Age at Dementia Diagnosis vs. Years of Education")

plt.show()

# create a bar graph of years of education by sex and cognitive status, with a one-way ANOVA
healthy_female = [patient.years_education for patient in Patient.all_patients
                  if patient.sex == "Female" and patient.cognitive_status == "No dementia"]

healthy_male = [patient.years_education for patient in Patient.all_patients
                if patient.sex == "Male" and patient.cognitive_status == "No dementia"]

diseased_female = [patient.years_education for patient in Patient.all_patients
                   if patient.sex == "Female" and patient.cognitive_status == "Dementia"]

diseased_male = [patient.years_education for patient in Patient.all_patients
                 if patient.sex == "Male" and patient.cognitive_status == "Dementia"]

# Mean and standard deviation for each group
group_names = ["Healthy Female", "Healthy Male", "Diseased Female", "Diseased Male"]
group_means = [np.mean(healthy_female), np.mean(healthy_male),
               np.mean(diseased_female), np.mean(diseased_male)]
group_stds = [np.std(healthy_female), np.std(healthy_male),
              np.std(diseased_female), np.std(diseased_male)]

# One-way ANOVA
f_stat, anova_p = stats.f_oneway(healthy_female, healthy_male, diseased_female, diseased_male)
print("\nANOVA results:")
print("F-statistic:", f_stat)
print("p-value:", anova_p)

plt.figure()
plt.bar(group_names, group_means, yerr=group_stds, capsize=5)
plt.xlabel("Sex and Health Status")
plt.ylabel("Mean Years of Education")
plt.title("Years of Education by Sex and Cognitive Status")
plt.text(0.5, 0.95, f"One-way ANOVA: p = {anova_p:.3f}",
         transform=plt.gca().transAxes, ha="center", va="top")
plt.show()