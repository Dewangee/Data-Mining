import numpy

label_values = {}
label_mean = {}
label_std = {}
label_prob = {}
probabilty = {}
final_list = []

def gaussianProbability(x, mean, std):
    if std == 0:
        std = 1
    return (1/(std * (numpy.math.sqrt(2*numpy.math.pi))))*numpy.math.exp((-(x-mean)**2)/(2*(std**2)))


def trainNB(featureMatrix, labels):

    # Separating the data points into Labels

    for i in range(len(labels)):
        if labels[i] in label_values:
            label_values[labels[i]].append(featureMatrix[i])
        else:
            label_values[labels[i]] = [featureMatrix[i]]

    for i in set(labels):
        label_prob[i] = labels.count(i)/len(labels)

    # Finding mean and median of the each feature for all labels and save it in arrays

    for i in label_values:
        label_mean[i] = numpy.mean(label_values[i], axis=0)
        label_std[i] = numpy.std(label_values[i], axis=0)

def classifyNB(testPoint):

    for i in label_values:
        probabilty[i] = label_prob[i]

        for j in range(len(testPoint)):
            probabilty[i] *= gaussianProbability(testPoint[j], label_mean[i][j], label_std[i][j])

    return max(probabilty, key=probabilty.get)

def testing(labels, feature_matrix):

    trainNB(feature_matrix, labels)

    testvalues = [line.rstrip('\n').split(",") for line in open('test.txt')]
    data = [list(map(float, l)) for l in testvalues]

    # Writing labels after testing

    file = open("labels.txt", "w")
    for i in data:
        a = classifyNB(i)
        final_list.append(a)
        file.write(a + '\n')

def cross_validation(labels, feature_matrix):

    x_val = numpy.array_split(feature_matrix, 10)
    x_labels = numpy.array_split(labels, 10)


    sum = 0
    
    for testcase in range(len(x_val)):

        new_feature_matrix = []
        new_labels = []

        i = 0
        while i < len(x_val):

            if i != testcase:
                for j in x_val[i]:
                    new_feature_matrix.append(j)
                for j in x_labels[i]:
                    new_labels.append(j)
            i += 1

        trainNB(new_feature_matrix, new_labels)

        testvalues = x_val[testcase]

        test_labels = []
        for i in testvalues:
            test_labels.append(classifyNB(i))

        i = 0
        accuracy = 0

        while i < len(test_labels):
            if test_labels[i] == x_labels[testcase][i]:
                accuracy += 1
            i += 1

        sum += accuracy/(len(test_labels))

    print("Accuracy", (sum/len(x_val))*100)


def main():

    val = [line.rstrip('\n').split(",") for line in open('train.txt')]
    labels = [val[i][len(val[i]) - 1] for i in range(len(val))]
    feature_matrix = [[float(val[i][j]) for j in range(len(val[i]) - 1)] for i in range(len(val))]

    cross_validation(labels, feature_matrix)
    testing(labels, feature_matrix)

    r_percentage = final_list.count('R')/len(final_list)
    d_percentage = final_list.count('D')/len(final_list)
    # print("Percentage of R = ", r_percentage*100)
    # print("Percentage of D= ", d_percentage*100)

main()