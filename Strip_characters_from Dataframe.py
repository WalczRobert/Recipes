""" Robert Walczak
Program to strip the first 4 character from the begining of the list in a dataframe.
Writes the cleaned data to another file."""
#to get list of files in a directory use CMD line and change to the directroy in question then
# type "dir >file.csv"
import pandas as pd

df = pd.read_csv("C:\\Users\\rewal\\PycharmProjects\\Toy_MNIST\\Testing_images\\toys.csv", encoding = "ISO-8859-1")
df['item'] = df['item'].str[3:]
df.to_csv('C:\\Users\\rewal\\PycharmProjects\\Toy_MNIST\\Training_images\\cleaned_toys.csv')
