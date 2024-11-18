# CS50 ICA Natural Gradient in Python
Kacper Jasiński 2024/03/11

#### Video Demo:  https://youtu.be/nFW6d2PGO-I
#### Description:
This project is a material for ***CS50's Introduction to Computer Science Course***. It is an implementation of ICA Natural Gradient algorithm in multiple Python scripts.
It is capable of distinguishing characteristics from signals given as an input.

>[!NOTE]
>The program does not handle extraction of the signals itself. It is only used to find characteristics from signals provided in csv files.

### Table of contents:
#### ***1. mixsignals.py***
A Command Line Program used to generate sample source signals and mixing them randomly. User can specify own functions by configuring the file.
*Configuration can be done by altering function forms in the script. User can add own signals to the code to check separation of different signals*.

Running this program produces 3 csv files:
+ **s.csv** - File containing values of source signals,
+ **a.csv** - File containing mixing matrix values,
+ **x.csv** - Product of **a** and **s** matrices. It is a representation of signals in natural environment with noises,

and prints conditioning of **a** matrix. It has only information value for user whether it will be an easy task for the machine to invert the disturbed signals. Values less than 30 can be considered as a well defined task.

It takes two command line arguments:
+ ***max*** - *float* number used to specify how long the signal is.
+ ***step*** - *float* number used to specify how long the step between each observation is.

>[!IMPORTANT]
>Values should be adjusted accordingly to functions in the configuration.

> python mixsignals.py *max step*

Example usage:
> python mixsignals.py 0.3 0.0001


#### ***2.  plotsignals.py***
A Command Line Program used to generate visualizations for signals given as an argument. Running this program produces *output_file.png* in the working directory. This file can be used to check form of originals signals or assess separation after using ***icaalg.py***.

It takes two command line arguments:
+ ***input_file.csv*** - A file with a matrix to visualize.
+ ***output_file.png*** - Choose name for output file.

> python plotsignals.py *input_file.csv output_file.png*

Example usage:
> python plotsignals.py x.csv x.png


#### ***3. icaalg.py***
A Command Line Program used to separate characteristics of signals from noises using Independent Component Analysis Natural Gradient algorithm. It includes a simple element of local parameters optimization.

Running this program produces 2 csv files:
+ **y.csv** - File containing values of cleaned signals,
+ **w.csv** - File containing weight matrix values,

and prints to the console optimal learning parameters for given optimization radius as well as the best value of ***pimi*** index for found parameters.

It takes five command line arguments:
+ ***input_file.csv*** - A file with a matrix to separate signals from,
+ ***l_param1*** - *int* index of observation where machine should start applying learning parameters,
+ ***l_param2*** - *float* number indicating learning rate update,
+ ***l_param3*** - *float* number controlling learning rate,
+ ***radius*** - *int* number indicating range of parameter optimization.

>[!CAUTION]
>Complexity of optimization task is O(n<sup>2</sup>). Be cautious when inserting ***radius*** argument as it may prevent the program of completing.

> python icaalg.py *input_file.csv l_param1 L_param2 l_param3 radius*

Example usage:
> python icaalg.py x.csv 150 0.008 -0.001 10

#### ***4. pimi.py***
A script containing *pimi* function used in ***icaalg.py*** for optimization. This is a performance index indicating the quality of signal separation. The higher the value the worse the separation is.

#### References:
Implementation of this algorithm is based on Big Data class materials at Warsaw School of Economics. https://usosweb.sgh.waw.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&kod=223090-S

##### Considerations
1. I spent long time wondering whether to implement this as a set of Command Line Programs or make scripts more configurable. I decided to stick to the idea of inserting arguments in Command Line as this gives more flexibility while running programs. Downside of this idea can be seen while running ***icaalg.py*** where number of CLA makes the call for this program really uncomfortable (especially when handling with float number values).
2. I had doubts about implementing the element of optimization because I used the simplest algorithm possible to find best local fit. Such implementation is very demanding in computing, hence the area for optimization cannot be large. Definitely a space for improvement.
