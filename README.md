# data_science_bootcamp
Projects completed over the course of an intensive 12-week data science bootcamp at Constructor Academy, Zurich 2022

# Project 1 Twitter challenge (shortly before the X rebranding)
This was an exercise in webscraping data from twitter users, performing analysis and visualization on the data. 
For the purposes of obtaining the data, we used an active account on the Twitter API. The code to retrieve data is available here, but the authentication creditinals are not shared. 
Some basic time series trends and sentiment analysis were performed, and displayed in a streamlit app, which can be found here. 

Specifically, we were asked to:

Use the Twitter API to access Twitter data. Find the most frequently used hashtags. Choose 5 famous American celebrities, analyze their twitter usage (e.g. number of tweets, retweets, when tweet during the day, etc.) and compare the results to Elon Musk’s Twitter account.

# Project 2 Auto Machine Learning and Supervised Learning Challenge
This was a challenge to find the best model for an anonamous dataset. 

Specifically, we were asked to:

Supervised Learning Challenge

The dataset we will be using contains two CSV files ‘features’ and ‘target’.

Each row in the ‘features’ belongs to a ‘measurement’ and each column represents a ‘feature’. For each row in the ‘features’ you have a corresponding class label in ‘target’. You can consider the row-numbers as keys.

You will have to use data labelled as ‘train’ for implementing the models. You have to submit the results that you obtain from the predictions of your Machine Learning models from the data labelled as ‘test’.

Complete the following:

Explore your data. Can you identify anything interest that is worth noting from the data?
Define a set of possible classifiers and show which one performs best. Keep in mind the problem of overfitting.
Using feature selection try to reduce the number of features. In the dataset you have over 120 features. Find the good ones for your classifier.
Keep in mind that there is no best solution to the challenge. Show how you approach a problem, and the skills/methods you use in that approach.

Evaluation Process:

The relevant metric in scikit-learn to increase is f1_macro. After you finish your best model, please save your predictions to CSV file with the column names ‘Id’ and ‘Predicted’. No index column!

Submit your CSV file in ‘Submit Predictions’ section.

You can check your score in ‘My Submissions’ section and choose the one to make it Final Score by checking the ‘Use for Final Score’ checkbox.

# Project 3 group Machine Learning Challenge

Customer segmentation

You are given a dataset of credit card transactions. The dataset contains 8500 customers and their activity over a 6-month period. Each transaction is characterized by 18 features described below.

Your task is to find the most useful customer segmentation to improve the marketing campaigns of the company.

The features:

customer_id : id of the credit card holder
balance_account : balance amount left in the account to make purchases at the end of the 6-month period
purchases_amount : amount of purchases made from account
paid_advance : number of transactions made with “Cash in Advance” method
full_purchases : maximum purchase amount done in full payment
balance_frequency_update : how frequently the balance has been updated, score between 0 and 1 (1 = frequently - updated, 0 = not frequently updated)
installments : amount of purchases done in installments
purchases_frequency : how frequently the purchases are being made, score between 0 and 1 (1 = frequently - - purchased, 0 = not frequently purchased)
full_purchases_frequency : how frequently purchases are happening in full payment (1 = frequently purchased, - 0 = not frequently purchased)
purchases_installments_frequency : how frequently purchases in installments are being done (1 = frequently - done, 0 = not frequently done)
cash_advance_frequency : how frequently the cash in advance being paid
nr_cash_advances : cash in advance given by the user
nr_purchases : number of purchase transactions made
credit_limit : limit of credit card for user
fixed_rate_period : duration of fixed interest rate of credit card service for user (in months)
payments : amount of payment done by user
min_payments : minimum amount of payments made by user
full_payment_prc : percent of full payment paid by user

# Project 4 Deep Learning group challenge

Brain Tumor Detector

Introduction

A brain tumor is a collection, or mass, of abnormal cells in your brain. Brain tumors can be cancerous (malignant) or noncancerous (benign). When benign or malignant tumors grow, they can cause the pressure inside your skull to increase. This can cause brain damage, and it can be life-threatening. The idea of this problem is to try and build an AI-powered system to be able to not just detect brain tumor but also find out specific type of tumors by looking at Brain MRI Scans. This will be a multi-class classification problem to classify each brain MRI scan image into 1 out of 4 classes using deep learning models for CV.

The dataset

Final dataset contains 7022 images of human brain MRI images which are classified into 4 classes: glioma - meningioma - no tumor and pituitary. The size of the images in this dataset is different and you can resize them all to 128x128 to make the models run faster. Dataset is already divided into train and test folders for convenience. Build models on the train dataset and check performance on the test data using CNNs, Transfer Learning, Data Augmentation etc.

../../_images/brain_tumor_images.png
Key Objectives

Train-Test Datasets are already prepared in the folders when you load them. Do split the train dataset into 80:20 (train-validation split – use seed=42). Resize images to 128x128 for quicker modeling
Build a basic CNN model from scratch (2-3) layers which should serve as a baseline model and give you around close to 90-91% accuracy easily
Try different approaches of data augmentation, more complex CNN architectures, pre-trained models, transfer learning along with NN training approaches like early stopping, dynamic learning rates etc. to see if you can push the model performance to 98-99% (remember in healthcare, model accuracy >= 98% is usually desired)
Showcase model performance on test data using confusion matrix, classification reports
Helper Notebook: Use this notebook to load the data quickly and get started (uses memory efficient version by loading data into tensorflow datasets) OR you could use this tutorial to use traditional ImageDataGenerators (though the first approach is preferred and more memory efficient).

Data Augmentation examples: https://www.tensorflow.org/tutorials/images/transfer_learning#use_data_augmentation OR check out the hints in the helper notebook towards the end.

Models: Feel free to build your own models from scratch and maybe experiment with pre-trained models e.g. VGG, ResNet etc.





