
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum1=0
    sum2=0
    arr=sorted(arr)
    for i in range(0,len(arr)-1):
        sum1+=arr[i]
    for i in range(1,len(arr)):
        sum2+=arr[i]
        
    print(str(sum1) +" " +  str(sum2))
        
        
