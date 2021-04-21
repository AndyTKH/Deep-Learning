# Deep-Learning 
Deep Learning (DL) is an advanced technique of machine learning (ML) based on neural network algorithm. This technique has found its application in almost every sector of business. Various deep learning models such as convolutional networks, recurrent networks, and GANs are implemented in the projects for trends prediction, image classification, and data generation.  

## Configure and Manage Your Environment with Anaconda
1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) on your computer.
2. Install ```git``` for working with Github from your terminal window with command:  
   ``` 
   conda install git 
   ``` 
3. Clone this repository to your local computer, and navigate to your downloaded folder with command:
   ```
   git clone https://github.com/AndyTKH/Deep-Learning.git                                                          
   cd Deep-Learning
   ```
4. Create and activate a new environment, named the new environment as `deep-learning-project` with Python 3.6 installed:
   
   - __Linux__ or __Mac__: 
	```
	conda create -n deep-learning-project python=3.6
	source activate deep-learning-project
	```
	- __Windows__: 
	```
	conda create --name deep-learning-project python=3.6
	activate deep-learning-project
	```
5. Install latest version of PyTorch and Torchvision:
   - __Linux__ or __Mac__: 
	```
	conda install pytorch torchvision -c pytorch 
	```
	- __Windows__: 
	```
	conda install pytorch -c pytorch
	pip install torchvision
	```
6. Install the required pip packages, as specified in the requirement text file: 
   ```
   pip install -r requirements.txt
   ```
7. Now that you have all the required libraries to run my project, assuming your `deep-learning-project` environment is still activated, you may now navigate to the specific project directory to view my project from Jupyter Notebook, replace ```project directory``` with the project name, for example replace ```project directory ``` with ```Image_Classification_Project``` for the Image Classification project:
   ```
   cd
   cd Deep-Learning/project directory
   jupyter notebook
   ```
    
