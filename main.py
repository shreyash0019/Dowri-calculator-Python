def dowry_calculator(age_option, profession_option, education_option, salary_option, residence_option, country_option):
    # Base dowry range (in INR)
    base_dowry = 100000

    # Age factor
    match age_option:
        case 1:
            dowry = base_dowry + 200000
        case 2:
            dowry = base_dowry + 150000
        case 3:
            dowry = base_dowry + 100000

    # Profession factor
    match profession_option:
        case 1:  # Doctor
            dowry *= 1.5
        case 2:  # Engineer
            dowry *= 1.3
        case 3:  # Teacher
            dowry *= 1.1
        case 4:  # Business
            dowry *= 1.2
        case 5:  # Unemployed
            dowry *= 0.5

    # Education factor
    match education_option:
        case 1:  # High School
            dowry *= 1.0
        case 2:  # Bachelor's
            dowry *= 1.2
        case 3:  # Master's
            dowry *= 1.4
        case 4:  # PhD
            dowry *= 1.6

    # Monthly salary factor
    match salary_option:
        case 1:  # ₹20,000 - ₹50,000
            dowry += 100000
        case 2:  # ₹50,001 - ₹1,00,000
            dowry += 200000
        case 3:  # Above ₹1,00,000
            dowry += 300000

    # Residence factor
    match residence_option:
        case 1:  # Urban
            dowry += 50000
        case 2:  # Rural
            dowry += 20000

    # Country factor
    match country_option:
        case 1:  # India
            dowry *= 1.0
        case 2:  # USA
            dowry *= 1.3
        case 3:  # UK
            dowry *= 1.2
        case 4:  # Canada
            dowry *= 1.2
        case 5:  # Other
            dowry *= 0.8

    # Ensure the dowry stays within the range of ₹1,00,000 to ₹15,00,000
    dowry = max(100000, min(dowry, 1500000))

    return round(dowry, 2)


# User menu for input
print("Select your age range:")
print("1. 20 - 25\n2. 26 - 30\n3. Above 30")
age_option = int(input("Enter your choice (1/2/3): "))

print("\nSelect your profession:")
print("1. Doctor\n2. Engineer\n3. Teacher\n4. Business\n5. Unemployed")
profession_option = int(input("Enter your choice (1/2/3/4/5): "))

print("\nSelect your education level:")
print("1. High School\n2. Bachelor's\n3. Master's\n4. PhD")
education_option = int(input("Enter your choice (1/2/3/4): "))

print("\nSelect your monthly salary range:")
print("1. ₹20,000 - ₹50,000\n2. ₹50,001 - ₹1,00,000\n3. Above ₹1,00,000")
salary_option = int(input("Enter your choice (1/2/3): "))

print("\nSelect your residence:")
print("1. Urban\n2. Rural")
residence_option = int(input("Enter your choice (1/2): "))

print("\nSelect your country:")
print("1. India\n2. USA\n3. UK\n4. Canada\n5. Other")
country_option = int(input("Enter your choice (1/2/3/4/5): "))

# Calculate dowry
dowry_amount = dowry_calculator(age_option, profession_option, education_option, salary_option, residence_option, country_option)
print(f"\nThe estimated dowry amount is: ₹{dowry_amount}")
