# playtech
Installing the application

The app.exe file is implemented to use the program. It is located in the head folder. You don't need to install anything to use it. However, in the folder where the main.exe file is located, there must be three folders "database", "static" and "templates". The original database is located in the "database" folder called example.db. CSS files are located in the "static" folder. HTML files for web service are located in the "templates" folder.


Using the application

For using app you should run app.exe and go to link http://127.0.0.1:5000 in your browser. 

Main page

When the application is launched, the user sees the home pages. Here is an opportunity to find an existing loan or add a new one. To find it, you need to enter the ID number. It should have 7 numbers. If the entered number is not found, the application will show an error message.

Show loans page

If the word is found, the application shows the information of the borrower, all loaned money and all loans by list with dates. Register and database are made this way so 2 same IDs can not be added to database. It shows if user is blacklisted

