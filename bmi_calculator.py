import pandas as pd

def calculate_bmi(height, weight):
    # BMI formula: weight(kg) / height(m)^2
    bmi = weight / (height**2)

    return bmi

def main():
    user_h=1.7
    user_w=74

    user_bmi = calculate_bmi(user_h, user_w)

    print("BMI for the user: ", user_bmi)


if __name__ == "__main__":
    main()

