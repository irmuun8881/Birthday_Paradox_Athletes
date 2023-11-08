# Birthday Paradox Analysis with Athlete Birthdates

## Introduction

The birthday paradox is a well-known probability concept that highlights the surprising likelihood of shared birthdays within a relatively small group of people. It states that with just 23 individuals, there is a 50.73% chance of at least one pair sharing the same birthdate. This probability dramatically increases as the group size grows; with only 70 people, the likelihood of a shared birthday jumps to an astonishing 99.99%.

## Project Overview

This project leverages the concept of the birthday paradox by analyzing birthdate data from a substantial sample of 6800 NBA and NFL athletes. The goal is to determine the percentage of groups of athletes (comprising 23 individuals) in which at least one pair shares the same birthday. The sample size varies, starting from 460 athletes and incrementally increasing to around 6800.

## Installation

To run this project, you need to install the required Python dependencies. You can do this using the provided `requirements.txt` file. Here's how to install the dependencies:

1. First, ensure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/irmuun8881/Birthday_Paradox_Athletes.git

3. **Navigate to the Project Directory:**
   - Change your current directory to the project folder:
     ```bash
     cd Birthday_Paradox_Athletes
     ```

4. **Install Project Dependencies:**
   - Install the required Python packages by running the following command:
     ```bash
     pip install -r requirements.txt
     ```

   This command will install all the necessary dependencies listed in the `requirements.txt` file.

These installation instructions will help you set up the project environment and ensure that you have the required packages to run the analysis and visualizations.

## Analysis and Visualization

To perform this analysis, the project follows these key steps:

1. Data Collection: Birthdate data for 6800 NBA and NFL athletes is collected as a representative sample.

2. Group Formation: The data is grouped into smaller subsets, each containing 23 athletes.

3. Shared Birthday Analysis: For each group of 23 athletes, the project calculates the percentage of groups in which at least one pair shares the same birthday.

4. Total Sample Size Variation: The project systematically changes the total sample size, starting from 460 athletes and gradually increasing to approximately 6800.

5. Plot Generation: The results are visualized through plots, allowing for a clear representation of the relationship between sample size and the percentage of shared birthdays.

## Results and Insights

The project's analysis reveals intriguing results and insights into the birthday paradox:

- Expected Probability: The mathematically calculated probability for 23 people sharing a birthday is 50.73%. The analysis based on athlete birthdate data yields a mean value of 52.96%. This result demonstrates how the concept aligns with real-world data.

- Variance: The variance in the data analysis is approximately 1.99, indicating the degree of dispersion from the mean. A higher variance suggests more fluctuations in the results.

- Sample Size Influence: The analysis shows that the fluctuation in the percentage of shared birthdays decreases as the sample size increases. The graph becomes more stable, particularly starting from a sample size of around 2000 athletes.

These findings shed light on the counterintuitive nature of the birthday paradox and its implications for group dynamics and probability theory.

This repository contains the code, data, and visualizations used in the analysis, enabling you to explore the results in detail and apply the concept of the birthday paradox to different scenarios.

---
_This project is for educational and illustrative purposes and does not provide any personal or private information about the athletes involved._
