#Data Visualization Tool

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dataVisualization():
    file = input("Enter the file name : ")
    df = pd.read_csv(file)

    print("\nDataset Preview")
    print(df.head())

    print("\nColumns in dataset: ")
    print(list(df.columns))

    while True:
        print("\nChoose Visualization Option: \n")
        print("1. Exit \n2. Bar Cart\n3. Scatter Cart\n4. Histogram\n5. Line Chart")

        option = input("Enter your choice : ")
        if option == "1":
            print("\nProgram Ended! \n")
            break


        elif option == "2":
            x = input("Enter the x value : ")
            y = input("Enter the y value : ")
            plt.figure(figsize=(10, 6))
            sns.barplot(x=df[x], y=df[y])
            plt.title("Bar Chart")
            plt.show()

        elif option == "3":
            x = input("Enter column for X axis: ")
            y = input("Enter column for Y axis: ")
            plt.figure()
            sns.scatterplot(x=df[x], y=df[y])
            plt.title("Scatter Cart")
            plt.show()

        elif option == "4":
            col = input("Enter column for histogram: ")
            plt.figure()
            sns.histplot(df[col], bins=10)
            plt.title("Histogram")
            plt.show()

        elif option == "5":
            x = input("Enter the x axis value : ")
            y = input("Enter the y axis value : ")
            plt.figure()
            plt.plot(df.index, df[x], df[y], marker='o')
            plt.title("Line Chart")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()
        else:
            print("Invalid Option")

dataVisualization()