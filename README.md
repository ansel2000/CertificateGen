# CertificateGen
This Repo can be used to automate the process of generating certeficates from a given tempelate. It uses Pandas, OpenCV, and PIL libraries of python.

## Data
The list of participants can be stored in a 'xlsx'(excel) sheet along with a category in this case *Pass* or *Fail*. Reading this file is done using the *Pandas* Library. The code for this process is in *Read.py* which is executed in the following:-
 
`python Read.py`

## Selection of Points
The image is displayed in a new window using the Pillow(PIL) libray of python.
The points to print from are seleced by a *double click* and stored in a text file in order. This process is done using the OpenCV library in the file coord.py which is executed using the following :-

`python coord.py`

![](images/git1.PNG "Selecting Points")

## Output
A sample output is shown in a new window and the user can press *Esc* to stop the process or *Enter* to continue the process of generation after which the certificates get stored in the outputs folder. The code for this process is in certificate.py which is run using the following:-

`python certificate.py`

![](images/git2.PNG "Sample Output")
