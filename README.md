(a) Documentation:
The API expects data for 15 attributes (all non-categorical attributes and excluding G3)
Can be called by entering the format localhost:5000/predict?school=SCHOOL_NAME&age= … into a browser, where each attribute contains a string or int 
For example: localhost:5000/predict?age=18&absences=6&health=3&Medu=4&Fedu=4&traveltime=2&failures=0&studytime=2&famrel=4&goout=4&freetime=3&Dalc=1&Walc=1&G1=5&G2=6
Read the student.txt file to learn what values can be entered for each attribute
Output is the quality of the student and represented by either a 1 or 0 (1 indicating a quality student with G3 >= 15, 0 indicating a quality student with G3 < 15)

(b) The model used the following features:
Age - student’s age
Medu - mother’s education
Fedu - father’s education
Traveltime - home to school travel time
Studytime - weekly study time
Failures - number of past class failures
Famrel - quality of family relationships
Freetime - free time after school
Goout - going out with friends
Dalc - workday alcohol consumption
Walc - weekend alcohol consumption
Health - current health status
Absences - number of school absences
G1 - student’s G1 score
G2 - student’s G2 score

The retrained model consistently achieves an accuracy of >90% when predicting G3 in the test set. This is a significant increase in accuracy compared to the baseline model.

(c) Deployment: 
 
cd into fall-2021-hw4-a-mama
cd into dockerfile 
Build the docker container 
docker build -t ml:latest .
docker run -d -p 5000:5000 ml
Run the test URL’s 

(d) To train the model, we split the data into training and testing sets using sklearn and the method train_test_split with a test size of 0.5. After training the model on the training set, we ran it on the testing set. We did this multiple times, with each time yielding an accuracy of above 90%.
