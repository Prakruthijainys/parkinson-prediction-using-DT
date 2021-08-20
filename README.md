# parkinson-prediction-using-DT
# Parkinson's disease prediction from speech data using Decision tree algorithm.


ABOUT DATASET 

Dataset is collected from UCI Machine Learning Repository through the link https://archive.ics.uci.edu/ml/datasets/Parkinson%27s+Disease+Classification# The data used in this study was gathered from 188 patients with Parkinson’s disease in which 107 were men and 81 were women with age ranging from 33 to 87. This information was collected at the Department of Neurology in Istanbul university. Dataset Characteristics: Multivariate Attribute Characteristics: Integer, Real Number of instances: 756 Number of Attributes: 754 Associated Task: Classification Missing values: N/A

What is Parkinson's disease? 

Parkinson’s Disease (PD) is a neurodegenerative disorder that affects the nerve cells in the brain that produce dopamine. PD symptoms include muscle rigidity, tremors, and changes in speech and gait. Perceptually, speech and voice in people with PD are characterized by reduced loudness, monopitch, monoloudness, reduced stress, breathy. In this study, several speech signal processing techniques were used to obtain clinically relevant features, and Decision tree classifier algorithm is applied on the extracted features to construct the classification model which predicts whether the person is having Parkinson’s disease or not.

PYTHON PACKAGE USED 

Pandas: 

   • Used to read and write different files 
   • Data manipulation can be done easily with dataframes

Numpy: 

   • It is a numeric python module which provides fast maths functions for calculations.
   • It is used to read data in numpy arrays and for manipulation purpose.

sklearn:

   • In python, sklearn is a machine learning package which include a lot of ML algorithms.
   • In this code, some of the sklearn modules like train_test_split, StandardScaler, confusion_matrix, DecisionTreeClassifier and accuracy_score are used.

Matplotlib: 

   • It is a visualization library in python. It consists of several plots like line, bar, scatter, histogram etc.
   • The plot_tree method which is in sklearn requires matplotlib to plot the Decision tree.

Built with spyder.

CLASSIFICATION ALGORITHM

Decision Tree is a Supervised learning technique that can be used for both classification and Regression problems, but mostly it is preferred for solving Classification problems. It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.


