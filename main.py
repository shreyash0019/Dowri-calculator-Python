from inputs import get_user_inputs
from calculations import dowry_calculator

def main():
    user_choices = get_user_inputs()
    dowry_amount = dowry_calculator(*user_choices)
    print(f"\nThe estimated dowry amount is: ₹{dowry_amount}")

if __name__ == "__main__":
    main()
