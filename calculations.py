def dowry_calculator(age_option, profession_option, education_option, salary_option, residence_option, country_option):
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
        case 1:
            dowry *= 1.5
        case 2:
            dowry *= 1.3
        case 3:
            dowry *= 1.1
        case 4:
            dowry *= 1.2
        case 5:
            dowry *= 0.5

    # Education factor
    match education_option:
        case 1:
            dowry *= 1.0
        case 2:
            dowry *= 1.2
        case 3:
            dowry *= 1.4
        case 4:
            dowry *= 1.6

    # Salary factor
    match salary_option:
        case 1:
            dowry += 100000
        case 2:
            dowry += 200000
        case 3:
            dowry += 300000

    # Residence factor
    match residence_option:
        case 1:
            dowry += 50000
        case 2:
            dowry += 20000

    # Country factor
    match country_option:
        case 1:
            dowry *= 1.0
        case 2:
            dowry *= 1.3
        case 3:
            dowry *= 1.2
        case 4:
            dowry *= 1.2
        case 5:
            dowry *= 0.8

    dowry = max(100000, min(dowry, 1500000))
    return round(dowry, 2)
