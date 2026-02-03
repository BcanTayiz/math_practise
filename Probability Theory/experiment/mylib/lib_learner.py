import numpy as np
import random
from sklearn.datasets import load_iris
from collections import Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris,load_wine,load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier


class LearnerNode:

    def __init__(self, id=0,row=[],target=""):
        self.id = id
        self.nodes = []
        self.distance_val = 1
        self.value = target
        self.row  = row

    
    def select_related_nodes(self,node):
        vote = 0
        for row in self.nodes:
            if self.calculate_distance_row(row,node.row) < self.distance_val:
                vote += 1

        if vote > len(self.nodes) / 2:
            self.nodes.append(node)
        
    def calculate_distance_row(self,a,b):
        abs_dist = [abs(i-j) for i,j in zip(a,b)]  
        return sum(abs_dist)

    def assing_distance(self):
        distance_values = []
        if len(self.nodes) > 0:
            for node in self.nodes:
                distance_values.append(self.calculate_distance_row(self.row,node.row))
            
            self.distance_val = min(distance_values)

    def set_value(self):
        values = Counter([node.value for node in self.nodes]).most_common(3)
        if len(values) == 3:
            self.value = random.choice(values)
            


    
class LearningUnits:

    def __init__(self,data,target):
        self.data = data
        self.target = target
        self.pool_of_learners = []
        


    def collect_learners(self):

        for i,row in enumerate(self.data):
            learner = LearnerNode(id=i,row=row,target=self.target[i])
            self.pool_of_learners.append(learner)
            for j in range(i):
                learner.select_related_nodes(self.pool_of_learners[j])

            learner.assing_distance()
            learner.set_value()

    def selected_dist_group(self,row):
        selected_dist_group = []
        for learner in self.pool_of_learners:
            dist_temp = learner.calculate_distance_row(row,learner.row)
            if dist_temp <= learner.distance_val:
                selected_dist_group.append((dist_temp,learner))
                
        if len(selected_dist_group) > 0:
            return selected_dist_group 
        else:
            dist_per = np.inf
            for learner in self.pool_of_learners:
                dist_temp = learner.calculate_distance_row(row,learner.row)
                if dist_temp < dist_per:
                    dist_per = dist_temp
                    selected_dist_group.append((dist_temp,learner))

            return selected_dist_group
        

    def predict(self,row) :
        selected_rows = self.selected_dist_group(row)
        value_rows = [val[1].value for val in selected_rows]
        vals,counts = np.unique(value_rows, return_counts=True)
        index = np.argmax(counts)
        return vals[index]



def calculate_learner_accuracy(agent_learning,X,y):
    error = 0
    correct = 0
    for x_row,y_target in zip(X,y):
        prediction = agent_learning.predict(x_row)
        #print(prediction,y_target)
        if prediction == y_target:
            correct += 1
        else:
            error += 1


    print(f"correct num: {correct}, error num: {error} ratio: {correct/(error + correct)}")
            

def match_predict(predict,real):
    correct = 0
    error = 0
    for p,r in zip(predict,real):
        if p == r:
            correct += 1
        else:
            error+=1
    
    print(f"correct num: {correct}, error num: {error} ratio: {correct/(error + correct)}")






    

        

    