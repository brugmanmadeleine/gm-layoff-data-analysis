import csv
import unittest

def csv_reader(filename):
    employees = {} 

    with open(filename, "r") as file: 
        reader = csv.DictReader(file) 

        for row in reader:
            employee_id = row["employee_id"]
            employees[employee_id] = { 
                "gender": row["gender"],
                "race": row["race"],
                "hire_year": int(row["hire_year"])
            }
    return employees 


def split_by_hire_year(employees, split_year):
    before_year = {}
    after_year = {}

    for employee_id, info in employees.items(): 
        if info["hire_year"] < split_year: 
            before_year[employee_id] = info
        else:
            after_year[employee_id] = info
    return before_year, after_year 

def race_or_gender(employees):
    counts = { 
        "race": {},
        "gender": {}
    }

    for info in employees.values():
        race = info["race"]
        gender = info["gender"]

        if race not in counts["race"]:
            counts["race"][race] = 0

        counts["race"][race] += 1

        if gender not in counts["gender"]:
            counts["gender"][gender] = 0

        counts["gender"][gender] += 1

    return counts


def race_and_gender_counter(employees):

    counts = {}

    for info in employees.values():
        race = info["race"]
        gender = info["gender"]

        combination = f"{race}&{gender}"

        if combination not in counts:
            counts[combination] = 0
        
        counts[combination] += 1

    return counts


def csv_writer(data, filename): 

    with open(filename, "w", newline="") as file: 
        writer = csv.writer(file)
        writer.writerow(["Race&Gender", "num_employee"])

        for combination, count in data.items():
            writer.writerow([combination, count])

class TestEmployeeDataAnalysis(unittest.TestCase):

    def setUp(self):
        self.employees = csv_reader("smaller_dataset.csv")

    def test_load_csv(self):
        self.assertEqual(len(self.employees), 20)
        self.assertEqual(len(self.employees["employee_1"]), 3)
    

    def test_split_by_hire_year(self):
        test_employees = {
            "employee_1": {"gender": "Female", "race": "White", "hire_year": 1960},
            "employee_2": {"gender": "Male", "race": "Black", "hire_year": 1964},
            "employee_3": {"gender": "Female", "race": "Black", "hire_year": 1968},
            "employee_4": {"gender": "Male", "race": "White", "hire_year": 1970}
        }

        # test splitting at 1964
        before_1964, after_1964 = split_by_hire_year(test_employees, 1964)

        self.assertEqual(len(before_1964), 1)
        self.assertEqual(len(after_1964), 3)
        self.assertIn("employee_1", before_1964) 
        self.assertIn("employee_2", after_1964)

        # test splitting at 1970
        before_1970, after_1970 = split_by_hire_year(test_employees, 1970)

        self.assertEqual(len(before_1970), 3)
        self.assertEqual(len(after_1970), 1)
        self.assertIn("employee_4", after_1970)

    def test_race_or_gender(self):
        test_employees = {
        "employee_1": {"gender": "Female", "race": "White", "hire_year": 1960},
        "employee_2": {"gender": "Male", "race": "Black", "hire_year": 1965},
        "employee_3": {"gender": "Female", "race": "Black", "hire_year": 1968},
        "employee_4": {"gender": "Male", "race": "White", "hire_year": 1970}
        }

        results = race_or_gender(test_employees)

        # test outer dictionary
        self.assertEqual(len(results), 2)
        self.assertIn("race", results)
        self.assertIn("gender", results)

        # test race counts
        self.assertEqual(results["race"]["White"], 2)
        self.assertEqual(results["race"]["Black"], 2)

        # test gender counts
        self.assertEqual(results["gender"]["Female"], 2)
        self.assertEqual(results["gender"]["Male"], 2)

        self.assertEqual( #tests if it works with an empty dictionary
            race_or_gender({}),
            {"race": {}, "gender": {}}
            )


    def test_race_and_gender_counter(self):
        test_employees = {
                "employee_1": {"gender": "Female", "race": "White", "hire_year": 1960},
                "employee_2": {"gender": "Male", "race": "Black", "hire_year": 1965},
                "employee_3": {"gender": "Female", "race": "Black", "hire_year": 1968},
                "employee_4": {"gender": "Male", "race": "White", "hire_year": 1970},
                "employee_5": {"gender": "Female", "race": "Black", "hire_year": 1971},
                "employee_6": {"gender": "Male", "race": "Black", "hire_year": 1966}
            }

        results = race_and_gender_counter(test_employees)

        self.assertEqual(len(results), 4)
        self.assertEqual(results["Black&Female"], 2)
        self.assertEqual(results["Black&Male"], 2)
        self.assertEqual(results["White&Female"], 1)
        self.assertEqual(results["White&Male"], 1)




def main():
    employee_data = csv_reader('GM_employee_data.csv')

    employees_before_1964, employees_after_1964 = split_by_hire_year(employee_data, 1964)

    race_gender_counts_total = race_or_gender(employee_data)
    race_gender_counts_after_layoffs = race_or_gender(employees_before_1964)

    gendered_race_counts_total = race_and_gender_counter(employee_data)
    gendered_race_counts_after_layoffs = race_and_gender_counter(employees_before_1964)

    print("Analysis Results:")
    print("--------------------------------------------------------")

    # Task 1: Splitting employees
    print("Task 1: Split Employees by Hire Year")
    print(f"Number of employees hired total: {len(employee_data)}")
    print(f"Number of employees after layoffs: {len(employees_before_1964)}")
    print("--------------------------------------------------------")

    # Task 2: Comparing race or gender of all employees before and after layoffs
    print("Task 2: Comparing Race and Gender Before and After Layoffs")
    print("Category: Before Layoffs ---> After Layoffs")
    print("Race:")
    for category, count_before in race_gender_counts_total['race'].items():
        count_after = race_gender_counts_after_layoffs['race'].get(category, 0)
        print(f"\t{category}: {count_before} ---> {count_after}")

    print("Gender:")
    for category, count_before in race_gender_counts_total['gender'].items():
        count_after = race_gender_counts_after_layoffs['gender'].get(category, 0)
        print(f"\t{category}: {count_before} ---> {count_after}")

    print("--------------------------------------------------------")

    # Task 3: Comparing race and gender combinations before and after layoffs
    print("Task 3: Comparing Gendered Race Combinations Before and After Layoffs")
    print("Category: Before Layoffs ---> After Layoffs")
    print("Gendered races:")
    for category, count_before in gendered_race_counts_total.items():
        count_after = gendered_race_counts_after_layoffs.get(category, 0)
        print(f"\t{category}: {count_before} ---> {count_after}")

    print("--------------------------------------------------------")

    csv_writer(gendered_race_counts_total, "GM_employee_data_before_layoffs.csv")
    csv_writer(gendered_race_counts_after_layoffs, "GM_employee_data_after_layoffs.csv")

if __name__ == "__main__":
    # Uncomment the following line to run the unittests
    # unittest.main(verbosity=2)
    
   main()
