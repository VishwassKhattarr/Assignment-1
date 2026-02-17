# Assignment-1: Learn Probability Density Functions using Roll-Number-Parameterized Non-Linear Model

## Objective
This assignment focuses on learning probability density functions by applying a roll-number-based non-linear transformation on NO₂ data and estimating parameters of a Gaussian-like probability distribution.

---

## Assignment Problem Statement

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/d2f8f467-b1e0-4abd-9fe9-3a631d2e3522" />


---

## Dataset
Dataset used: India Air Quality Data (Kaggle)  
https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data

Feature used:
- NO2 (no2 column)

---

## Methodology

### Step 1: Non-linear Transformation

Each NO₂ value `x` is transformed to `z` using:

z = x + a_r sin(b_r x)

Where:

a_r = 0.05 × (r mod 7)  
b_r = 0.3 × (r mod 5 + 1)

- r = University Roll Number  
- mod returns remainder after division  

This step introduces a non-linear perturbation to the original data.

---

### Step 2: Probability Density Function Estimation

The transformed variable `z` follows:

p(z) = c * exp(-λ(z − μ)^2)

Estimated parameters:
- μ (mean of z)
- λ (lambda, related to variance)
- c (normalization constant)

Parameter estimation:

μ = mean(z)  
variance = var(z)  
λ = 1 / (2 × variance)  
c = sqrt(λ / π)

---

## Implementation

### Requirements

- Python 3
- numpy
- pandas

Install dependencies:

pip install numpy pandas

---

### How to Run

1. Download dataset from Kaggle.
2. Place CSV file in project folder.
3. Run the script:

python code.py

---

## Output

The program outputs:

- a_r
- b_r
- μ (mu)
- λ (lambda)
- c (normalization constant)

These values represent the learned parameters of the probability density function.

---

## Repository Structure

assignment-1/
│── code.py  
│── data.csv  
│── assignment.png  
│── README.md  

---

## Author
Vishwas Khattar
