import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

df =pd.DataFrame()
csv_file = ("project.csv")

def introduction():
    msg='''*********************************************************************************************************\n
                            WELCOME TO ANALYSIS SYSTEM OF CLASS 12\n
        ****************************************************************************************************************'''
    for x in msg:
        print(x,end ='')
        time.sleep(0.005)
    wait = input('Press any key to continue.....')         

def made_by():
    msg=''' 
            Project By: Sambhav Jain 
            Class:12 Science
            School:Rishabh Public School
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')



def read_csv_file():
    df =pd.read_csv(csv_file)
    print(df)

# name of function      : clear
# purpose               : clear output screen
def clear():
    for x in range(65):
               print()

def data_analysis_menu():
        df = pd.read_csv(csv_file)
        while True:
            clear()
            print('\n\nData Analysis MENU ')
            print('_'*100)
            print('1.  Show Whole DataFrame\n')
            print('2.  Show Top Rows\n')
            print('3.  Show Specific Column\n')
            print('4.  Add a New Record\n')
            print('5.  Add a New Column\n')
            print('6.  Delete a Column\n')
            print('7.  Delete a Record\n')
            print('8.  EXIT')
            ch = int(input('Enter your choice:'))
            if ch == 1:
                print(df)
                wait = input()
            if ch == 2:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input()
            if ch == 3:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input()
            if ch==4:
                a = int(input('Enter Sr. No.:'))
                b = int(input('Enter Date:'))
                c = int(input(' Enter Rate:'))
                d = int(input('Enter Barcode:'))
                e = input('Enter Name of the Customer:')
                f = int(input('Enter APP ID:'))
                g = input('Enter STATUS:')
                h = input('Enter CONDITION:')
                i = input('Enter Vehicle name:')
                j = int(input('Enter Loan Amount:'))
                k = int(input('Enter Tenure:'))
                l = input('Enter Dealer Name:')
                m = input('Enter EX NAME:')
                     
                data={'Sr. No.':a,'Date':b,'Rate':c,'Barcode':d,'Name of the Customer':e,'APP ID':f,
                      'STATUS':g,'CONDITION':h,'Vehicle name':i,'Loan Amount':j,'Tenure':k,
                      'Dealer Name':l,'EX NAME:':m}
                df = df.append(data,ignore_index=True)
                print(df)
                wait=input()
            if ch==5:
                col_name = input('Enter new column name :')
                col_value = int(input('Enter default value of column :'))
                df[col_name]=col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()
            
            if ch==6:
                col_name =input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()
            
            if ch==7:
                index_no =int(input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()
            
            if ch == 8:
                break


# name of function      : graph
# purpose               : To generate a Graph menu
def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nData Visualisation ')
        print('_'*100)
        print('1.  line graph acc to Loan Amount')
        print('2.  line graph acc to Rate ')
        print('3.  deptwise highest tenure')
        print('4.  bar graph acc to highest loan amount')
        print('5.  deptwise Tenure')
        print('6.  exit')
        ch = int(input('Enter your choice:' ))
        
        if ch==1:
            g = df.groupby('SR.NO')
            x = df['SR.NO'].unique()
            y = g['Loan Amount'].sum()
            plt.xticks(rotation='vertical')
            plt.xlabel('SR.NO')
            plt.ylabel('Loan Amount')
            plt.title('line graph acc to loan amount')
            plt.grid(True)
            plt.plot(x, y)
            plt.show()
        
        if ch==2:
            g = df.groupby('SR.NO')
            x = df['SR.NO'].unique()
            y = g['RATE'].sum()
            plt.xticks(rotation=30)
            plt.xlabel('SR.NO')
            plt.ylabel('RATE')
            plt.title('line graph acc to RATE')
            plt.plot(x, y)
            plt.grid(True)
            plt.show()
            wait = input()
        
        if ch==3:
            g = df.groupby("SR.NO")
            x = df['SR.NO'].unique()
            y = g['Tenure'].sum()
            plt.xlabel('SR.NO')
            plt.ylabel('HIGHEST TENURE')
            plt.xticks(rotation=30)
            plt.title('DEPTWISE HIGHEST Tenure')
            plt.bar(x,y)
            plt.grid(True)
            plt.show()
        
        if ch==4:
            g = df.groupby("Name of the Customer")
            x = df['Name of the Customer'].unique()
            y = g['Loan Amount'].sum()
            plt.bar(x,y)
            plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title("bar graph acc to highest loan amount")
            plt.xlabel('Name of the Customer')
            plt.ylabel("Loan Amount")
            plt.show()
            wait= input()
        
        if ch==5:
            g = df.groupby("SR.NO")
            x = df['SR.NO'].unique()
            y = g['Tenure'].sum()
            plt.hist(x,)
            plt.xticks(rotation=30)
            plt.title("deptwise Tenure ")
            plt.xlabel('dept')
            plt.ylabel('Tenure')
            plt.grid(True)
            plt.show()
       
        if ch==6:
            break


def statistics():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nData Statistics')
        print('_'*100)
        print('1.  Count Vehicle name')
        print('2.  Maximum rate ')
        print('3.  sum of loan amount')
        print('4.  Average of loan amount')
        print('5.  Minimum rate')
        print('6.  exit')
        ch = int(input('Enter your choice:' ))

        if ch==1:
            print(df['Vehicle name'].count())
            wait=input()
        
        if ch==2:
            print(df['RATE'].max())
            wait=input()

        if ch==3:
            print(df['Loan Amount'].sum())
            wait=input()

        if ch==4:
            print(df['Loan Amount'].mean(axis=0))
            wait=input()

        if ch==5:
            print(df['RATE'].min())
            wait=input()

        if ch==6:   
            break
                                
def main_menu():
           clear()
           introduction()
           while True:
                      clear()
                      print('MAIN MENU ')
                      print('_'*100)
                      print()
                      print('1.  Read CSV File\n')
                      print('2.  Data Analysis Menu\n')
                      print('3.  Data Visualisation\n')
                      print('4.  Data Statistics\n')
                      print('5.  Exit\n')
                      choice = int(input('Enter your choice :'))
        
                      if choice==1:
                                 print('Here Is Your Table')
                                 read_csv_file()
                                 wait=input()
        
                      if choice==2:
                                 print('Opening Analysis Menu')
                                 data_analysis_menu()
                                 wait=input()
        
                      if choice==3:
                                 graph()
                                 wait=input()

                      if choice==4:
                                 statistics()
                                 wait=input()
                      
        
        
                      if choice==5:
                                 break
           clear()
           made_by()

# call your main menu
main_menu()
