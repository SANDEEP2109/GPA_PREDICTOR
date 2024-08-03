store_gpa = []


def Enter_GPA():
    while True:
        sem = input("Enter how many semesters are completed: ")

        if sem.isdigit():
            sem = int(sem)
            break
        else:
            print("Enter a valid number of semesters.")

    for i in range(sem):
        while True:
            try:
                gpa = float(input(f"Enter your GPA for semester {i + 1}: "))
                store_gpa.append(gpa)
                break
            except ValueError:
                print("Enter a valid GPA value.")
                continue


def predict_next_gpa(gpas):
    if len(gpas) < 2:
        # If we have less than 2 GPAs, we cannot calculate a trend, so we just return the last GPA
        return gpas[-1]

    differences = [gpas[i] - gpas[i - 1] for i in range(1, len(gpas))]
    avg_difference = sum(differences) / len(differences)
    return gpas[-1] + avg_difference


def main():
    Enter_GPA()
    print(f"Your present GPAs are: {store_gpa}")
    predicted_gpa = predict_next_gpa(store_gpa)
    print(f"Your predicted GPA for the upcoming semester is: {predicted_gpa}")


main()
