Jayam Sutariya
CS 422

Project 1

1. Decision Trees
Function(s):
DT_train_binary(X, Y, max_depth)
Funtion is incomplete as of now. However, the entropy and information gain helper functions exist. Recursion was tested
for subsequent depths, however, the output or the decision tree data structure was not implemented. In other words, 
if gone to max depth, the features needed to create the tree are calculated but that solution is not converted into a
decision tree itself. Other errors exist as well currently.

DT_test_binary()
This function has not been implemented yet, because the Decision tree data strucure was not ouputted from the last 
function. However, it would not be much different than testing the accuracy of other models in this project.

DT_make_prediction()
This function was not implemented either

2. Nearest Neighbors
An euclidian distance function was implemented from scractch as I was not aware the function could be imported from 
a library. Distances are calculated between a test sample and every training sample. All the distances are added to
an array of distances. These distances are sorted from smallest to largest. The labels for the training data are 
sorted in a similar way. Based on the k-value, the nearest K training samples are looked at. The corresponding
training samples' labels are summed up. Based on the sign of the sum, the test sample is either predicted positive or
negative. After all the test samples have been predicted a label, the labels are compared with that of the training
sample labels and accuracy is calculated.

3. Clustering
This function first checks whether or not the K-value is greater than 0. After that, it checks if the value of mu is 
specified. If it is, the function continues on with the mentioned mu. If not mentioned, the function randomly assigns 
K cluster centers. Euclidian distance is calculated from the test samples to the cluster centers/mean. The test samples
are assigned to one of the K clusters based on the lowest distance. New cluster centers are calculated based on the 
new clusters. This is done recursively until the new mu matches the old mu, meaning if the clusters did not change, 
or the model converged.

Note:
Apologies for the incomplete parts. I am new to Python and learning Python was tough for me this past couple weeks
because I had a lot of courseload. Learning to implement with numpy was one of the more difficult things for this 
project. Nonetheless, I will start even earlier next project and try to finish it for full credit.