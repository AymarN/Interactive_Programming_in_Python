Practice Exercises for Dictionaries and Images (optional)
________________________________________


Practice Exercises for Dictionaries and Images 
Solve each of the practice exercises below. Each problem includes three CodeSkulptor links: one for a template that 
you should use as a starting point for your solution, one to our solution to the exercise, and one to a tool that 
automatically checks your solution. 
1.	Create a dictionary day_to_number that converts the days of the week "Sunday", "Monday", … into the numbers 0, 1, …, respectively. 

2.	Create dictionary for name_lookup that, when you lookup the keys "Joe", "Scott", "John", and "Stephen",
you get the values "Warren","Rixner", "Greiner", and "Wong", respectively.

3.	Debug the program template below so that the resulting program draws the supplied image on the canvas.

4.	Load this image of an asteroid, and draw the image centered at the last mouse click. Prior to any mouse clicks,
the image should be drawn in the middle of the canvas. The image size is 95×93 pixels.

5.	Challenge: Find an image of your choosing and upload it to an image sharing site such as imgur.com. Add a direct link to the image
to a CodeSkulptor program and write a program that draws the image on the canvas. 

For this last problem, we will not provide a template. However, we note that common problems in this process include:
•	Having the image URL point to a webpage instead of an image, 
•	Choosing an image sharing site that has restrictions on the number of downloads or,
•	Using get_width() and get_height() to compute the image size before the image has loaded. These calls return an image size
of zero which results in an error in draw_image. To fix this error, you should either hard code the image size or use an if statement 
prevent the call to draw_image until the image sizes are not zero (indicating the image has loaded). 
