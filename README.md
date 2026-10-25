# General Motors Layoff Data Analysis

## Project Overview

This project was completed for SI 201 at the University of Michigan. It is based on *DeGraffenreid v. General Motors*, a discrimination lawsuit involving five Black women who challenged General Motors' seniority-based layoff policy.

The lawsuit raised questions about how a policy that appeared neutral could disproportionately affect employees based on the intersection of race and gender.

Using Python and simulated employee data, I examined how GM's layoff policy affected different demographic groups. The goal was to explore how data analysis can reveal patterns of discrimination that might be overlooked when race and gender are examined separately.

## Technologies Used

- **Python:** Data processing and analysis
- **CSV:** Reading employee records and exporting results
- **Dictionaries:** Organizing employee data and calculating demographic distributions
- **Unittest:** Testing functions and verifying expected results

## How the Project Works

I developed Python functions to:

1. Read employee records from a CSV file and organize them using nested dictionaries.
2. Separate employees into groups based on their hiring year to simulate a seniority-based layoff policy.
3. Count employees by race and gender separately.
4. Analyze race and gender together to identify patterns affecting specific demographic groups.
5. Export the results into CSV files for further analysis.

The analysis compares employee demographics before and after the simulated layoffs, with particular attention to how the policy affected Black women.

## How to Run the Project

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Keep the required CSV datasets in the same directory as `gm_layoff_analysis.py`.
4. Run the program using:

   `python gm_layoff_analysis.py`

To run the unit tests, use:

   `python -m unittest gm_layoff_analysis -v`

The program displays demographic comparisons and generates CSV files containing the analysis results.

## Key Takeaways

One of the most interesting parts of this project was seeing how analyzing demographic categories separately versus together can change our understanding of a policy's impact.

Looking only at race or gender can overlook the experiences of people affected by both forms of discrimination. This project reinforced the importance of intersectionality in data analysis and the need to consider what information a dataset might be missing.

It also helped me understand that writing code is only one part of analyzing data. Interpreting the results, recognizing limitations, and considering the real people represented by the data are equally important.

## AI Usage Disclosure

I used ChatGPT as a learning and debugging resource while completing this project. Specifically, I used AI to help me understand Python concepts, identify errors in my code, and think through the structure of certain functions and test cases.

Rather than using AI to complete the entire assignment, I worked through the code myself, tested my functions, and made revisions based on my understanding of the material.

I also used ChatGPT to help organize and edit this README.

This experience reinforced the importance of reviewing AI-generated suggestions, understanding how code works, and independently testing solutions rather than assuming they are correct.

## Data Disclaimer

The employee records used in this project are simulated and were provided for an academic assignment. They are not actual General Motors employment records, and the results should not be interpreted as an independent analysis of the historical lawsuit.
