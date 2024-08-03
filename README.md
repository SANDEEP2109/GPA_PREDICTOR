# GPA_PREDICTOR
The purpose of this program is to assist students in recording their GPA for each completed semester and predicting the GPA for the upcoming semester using a simple trend analysis.
Components:

Global List:

store_gpa: A list that exists outside the class and holds all the GPA values that the user enters for each semester.
Functions:

Enter_GPA(): This function intends to require the input of the number of semesters they have completed from the user. GPA is the average of the courses per semester taken by the user and the user is expected to input his or her GPA per semester. The GPAs are then stored in the list defined as store_gpa, Named as store_gpa for convenience.
predict_next_gpa(gpas): The parameters of this function are the GPA of previous semesters, as for the output, it calculates the GPA for the forthcoming semester. It has been used like this: If there are less than two GPAs, then, returns the last GPA entered. Otherwise, the improvement or decline over semesters is computed depending on the previous semester GPA and this is used to predict the next semester GPA.
Main Function:

main(): Thus it is stated that the main function controls the working process. It majorly uses Enter_GPA() function to get the GPAs from the user, it displays the current GPAs, it also uses the predict_next_gpa() function to determine the next semester GPA, it also displays this GPA.
Execution Flow:

The function call for starting this program is the main() function.
Specifically, in main(), the user is asked to input the number of the semesters they have done.
Each semester, the user is required to input his/her GPA which is placed in the store_gpa list.
The program proceeds to output the entered GPAs to the screen.
The program then passes the total credits of the semester and the cumulative GPA to the predict_next_gpa() function to predict the GPA for the next semester.
Last of all, it prints the estimated GPA for the next semester.
Usage:
This program comes in handy for the students who wish to monitor the trend of their academic performance over the years and project their future scores.
