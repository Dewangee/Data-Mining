import sys
import random
import numpy

def get_initial_seeds(number_of_clusters, data):
    seeds = []
    i = 0
    while i < number_of_clusters:
        random_number = random.randint(0, len(data) - 1)
        if (data[random_number] not in seeds):
            seeds.append(data[random_number])
            i += 1
    return seeds


def find_distance(point1, point2):
    distance =abs(numpy.sum(numpy.array(point1)-numpy.array(point2)))
    return distance


def update_centroid(cluster):
    x =  numpy.median(cluster, axis=0)
    return x


def create_clusters(number_of_clusters, data):

    #Get initial seeds
    #seeds=get_initial_seeds(number_of_clusters,data)
    seeds = [[1], [2],[3]]

    cluster=[]

    for i in range(sys.maxsize):
        cluster = [[] for i in seeds]
        new_seeds = []

        # Creating clusters after calculating minimum distance

        for i in data:
            mindistance = sys.maxsize
            index = 0
            for j in range(number_of_clusters):
                center = seeds[j]
                dist = find_distance(i, center)
                if (dist < mindistance):
                    mindistance = dist
                    index = j
            cluster[index].append(i)

        # Updating values of representatives for each cluster
        for i in cluster:
            new_seeds.append(update_centroid(i))

        print("seeds", seeds)
        print("New seeds", new_seeds)
        print("Cluster", cluster)

        if numpy.array_equal(new_seeds,seeds):
            break
        else:
            seeds = new_seeds

    return cluster



def main():
    number_of_clusters = int(input("Number of clusters : "))
    Val = [line.rstrip('\n') for line in open('testcases.txt')]
    Val = [i.split(",") for i in Val]
    data = [list(map(float, l)) for l in Val]
    print("Dataset", data)

    number_of_datapoints = len(data)

    if (number_of_clusters > number_of_datapoints):
        print("Input error : Number of clusters > Number of datapoints")
        exit(1)

    cluster = create_clusters(number_of_clusters, data)
    print("Final Cluster: ")
    print(*cluster, sep="\n")


main()

