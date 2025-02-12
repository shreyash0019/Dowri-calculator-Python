from utils import print_separator

def get_user_inputs():
    print_separator("Age Factor")
    print("Select your age range:")
    print("1. 20 - 25\n2. 26 - 30\n3. Above 30")
    age_option = int(input("Enter your choice (1/2/3): "))

    print_separator("Profession Factor")
    print("Select your profession:")
    print("1. Doctor\n2. Engineer\n3. Teacher\n4. Business\n5. Unemployed")
    profession_option = int(input("Enter your choice (1/2/3/4/5): "))

    print_separator("Education Factor")
    print("Select your education level:")
    print("1. High School\n2. Bachelor's\n3. Master's\n4. PhD")
    education_option = int(input("Enter your choice (1/2/3/4): "))

    print_separator("Salary Factor")
    print("Select your monthly salary range:")
    print("1. ₹20,000 - ₹50,000\n2. ₹50,001 - ₹1,00,000\n3. Above ₹1,00,000")
    salary_option = int(input("Enter your choice (1/2/3): "))

    print_separator("Residence Factor")
    print("Select your residence:")
    print("1. Urban\n2. Rural")
    residence_option = int(input("Enter your choice (1/2): "))

    print_separator("Country Factor")
    print("Select your country:")
    print("1. India\n2. USA\n3. UK\n4. Canada\n5. Other")
    country_option = int(input("Enter your choice (1/2/3/4/5): "))

    return age_option, profession_option, education_option, salary_option, residence_option, country_option
