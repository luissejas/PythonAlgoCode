import random
import time

def Insertion_sort(examplelist):
    for i in range(1,len(examplelist)):
        reference_value = examplelist[i] #Keeping the original value when the swap is performed
        j = i - 1 # Used to put the j, one position behind the i
        while j >= 0 and reference_value < examplelist[j]:
            #Performing the swap
            examplelist[j + 1] = examplelist[j]
            examplelist[j] = reference_value
            j = j - 1

def Merge_Sort(st_Array):
    #We are creating an exit condition, if the size of the list is 1, it is already sorted
    if len(st_Array) > 1:
        #Now we are defining the middle number to start breaking down our algorithm
        middle_num = (len(st_Array))//2
        lft_array = st_Array[:middle_num]
        #print(lft_array)
        rght_array = st_Array[middle_num:]
        #print(rght_array)
        Merge_Sort(lft_array)
        Merge_Sort(rght_array)
        #Since we already defined the condition of >1, when the list size is actually one, we do the following:
        #As we increase the level of stacks, the number of elements in every list naturally increases
        #Since all of the metadata is broken down in units we will sort all of them in a new array
        #With this, we will have to face three situations
        # A) Left list x Right list --> New Array
        # B) Left list --> New Array, case all of the terms in right list have already been sorted
        # C) Right list --> New Array, case all of the terms in left list have already been sorted
        # Before addressing each situation we will need to declare some variable to do so:
        # leftlist_ref is the reference to iterate through every element in the left list
        leftlist_ref = 0
        # rightlist_ref is the reference to iterate through every element in the right list
        rightlist_ref = 0
        # The auxiliary_ref is the reference to keep the previous value on the new position of the main list
        # to avoid any loss
        mainlist_ref = 0

        #A) (As mentioned on the three cases previously)
        while leftlist_ref < len(lft_array) and rightlist_ref < len(rght_array):
            if lft_array[leftlist_ref] < rght_array[rightlist_ref]:
                # st_Array is the main array, the one which you start the function
                st_Array[mainlist_ref] = lft_array[leftlist_ref]
                leftlist_ref = leftlist_ref + 1
            else:
                st_Array[mainlist_ref] = rght_array[rightlist_ref]
                rightlist_ref = rightlist_ref + 1
            mainlist_ref = mainlist_ref + 1

        #B)
        while leftlist_ref < len(lft_array):
            st_Array[mainlist_ref] = lft_array[leftlist_ref]
            leftlist_ref = leftlist_ref + 1
            mainlist_ref = mainlist_ref + 1

        #C)
        while rightlist_ref < len(rght_array):
            st_Array[mainlist_ref] = rght_array[rightlist_ref]
            rightlist_ref = rightlist_ref + 1
            mainlist_ref = mainlist_ref + 1

list_population = [1000, 2000, 4000, 8000, 16000, 32000]
best_insert_timelist = [0]
average_insert_timelist = [0]
worst_insert_timelist = [0]
best_merge_timelist = [0]
average_merge_timelist = [0]
worst_merge_timelist = [0]


for n in range(0, len(list_population)):
    list_best = list(range(list_population[n]))
    #print(list_best)
    list_worst = list(range(list_population[n], -1, -1))
    #print(list_worst)
    list_average = [random.randint(1, list_population[n]) for b in range(list_population[n])]
    #print(list_average)

    #Best Insertion Sort
    start_time = time.time()
    Insertion_sort(list_best)
    end_time = time.time()
    total_time = end_time - start_time
    best_insert_timelist.append(total_time)

    #Best Merge Sort
    start_time = time.time()
    Merge_Sort(list_best)
    end_time = time.time()
    total_time = end_time - start_time
    best_merge_timelist.append(total_time)

    #Average Insertion Sort
    start_time = time.time()
    Insertion_sort(list_average)
    end_time = time.time()
    total_time = end_time - start_time
    average_insert_timelist.append(total_time)

    #Average Merge Sort
    start_time = time.time()
    Merge_Sort(list_average)
    end_time = time.time()
    total_time = end_time - start_time
    average_merge_timelist.append(total_time)

    #Worst Insertion Sort
    start_time = time.time()
    Insertion_sort(list_worst)
    end_time = time.time()
    total_time = end_time - start_time
    worst_insert_timelist.append(total_time)

    #Worst Merge Sort
    start_time = time.time()
    Merge_Sort(list_worst)
    end_time = time.time()
    total_time = end_time - start_time
    worst_merge_timelist.append(total_time)


print("These are the population sizes \n" + str(list_population))
print("The times for the best cases in insertion sort are \n" + str(best_insert_timelist))
print("The times for the best cases in merge sort are \n" + str(best_merge_timelist))
print("The times for the average cases in insertion sort are \n" + str(average_insert_timelist))
print("The times for the average cases in merge sort are \n" + str(average_merge_timelist))
print("The times for the worst cases in insertion sort are \n" + str(worst_insert_timelist))
print("The times for the worst cases in merge sort are \n" + str(worst_merge_timelist))