# steps for the deployment 
1 - create ur notbook _ practise adjust as much as u like 
2-  save the best model and ur scaler as pickle 
______________
2- create a repo in ur git account 
3- add a readme and a gitignore file if needed (best to add )
_____________________
4- create a folder on ur pc u want to save ur project in 

5- clone ur git repo in it using git command (u must download git )
   _ this require copy the clone url from git
   _ go to ur folder press on the path and write CMD
   _ write the comman  git clone 'url' 
   _ u will find  the readme file and git ignore file 
   _ just to make sure u can use the comman git remot -v 
   _ this command will tell u the orgin fetch and push url ( the link associated with this folder _ fetch where it will be updated from and push where it will update it to )

   6- open anaconda and lunch vs code 
   7- create ur folders src , data , app  ( not needed but best practise )

   8- open terminal ( from terminal __> new termina __> instead of powershell use cmd  )

   9_ make sure ur in the right folder and  Create a conda environment for ur project using 
   this line

   conda create -n  (name of ur env here ) python=3.10 ( u can change the python version )
   so for this project i will be using this command 

   conda create -n cancer_env python=3.10 

PS : if ur not in the right older ur can use this command 
cd 'ur folder name ' 
ex : cd New_breast_cancer_project

10- after creating it will ask u to download necessary packages  press  y 

11_ activate the env using this command 
conda activate cancer_env
_ ps : u will find the path of ur project in terminal started with (CAncer_env) which mean it's activated and runing on ur project 
_ u can also press on vs Ctrl + Shift + P --> write this in the box __>  
Python: Select Interpreter 
and choose the env u just created 


12- create a file called requirements.txt to add the needed lib to ur project 

13_ put all the required lib in it  with their versions  : 

numpy==1.26.4
pandas==2.2.2
scikit-learn==1.5.1
tensorflow==2.15.0
xgboost==2.0.3
matplotlib
seaborn
joblib

14_  write this command to install the lib 
pip install -r requirements.txt 
 (make sure u wrote the file name correctly )
 (it will take a while )
 
 15- make sure it's downloaded using the command 
  pip list


16- make a new folder  call it notebooks add the notebook in it (download and put it to the notebooks folder )

17- press on the notebook--> Select Kernel --> cancer_env 
ps : if it's not showing u can   use this comman : 
conda install ipykernel
then choose :y 
then  write this command to attach it  to the env 

python -m ipykernel install --user --name cancer_env --display-name "Python (cancer_env)"


18- Now if u want we can devide our code to submodules we have 4 submodules
1️ Data + Preprocessing
2️ Training
3️ Evaluation
4️ Prediction (most imp one )

19 - but all i need is to put the model and the scaler and create the flask file 
app.py 

20 test the api using  postman 
http://127.0.0.1:5000/predict  
post method then go to body __> text : json  > past this 
{
  "features": [
    13.54,14.36,87.46,566.3,0.09779,
    0.08129,0.06664,0.04781,0.1885,0.05766,
    0.2699,0.7886,2.058,23.56,0.008462,
    0.0146,0.02387,0.01315,0.0198,0.0023,
    15.11,19.26,99.7,711.2,0.144,
    0.1773,0.239,0.1288,0.2977,0.07259
  ]
}  



first app.py then on another terminal 

streamlit run streamlit_app.py