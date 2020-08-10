import time
import numpy


def Interpolation_Search(arr, target):
    Low = 0
    High = (len(arr) - 1)
    while Low <= High and target >= arr[Low] and target <= arr[High]:
        POS = Low + int(((( arr[High] - arr[Low])) * ( target - arr[Low])) / float(High - Low))

        
        if arr[POS] == target:
            return POS
        if arr[POS] < target:
            Low = POS + 1;
        else:
            High = POS - 1;
    
    return "The target element is not in the sequence."

def Binary_Search(arr, target):
    Low = 0
    High = (len(arr) - 1)
    while Low <= High and target >= arr[Low] and target <= arr[High]:
        POS = int((Low + High)/ 2)
        
        if arr[POS] == target:
            return POS
        if arr[POS] < target:
            Low = POS + 1;
        else:
            High = POS - 1;
    
    return "The target element is not in the sequence."


#comparing times for both searches
def main():

  #when N = 100
  #interpolation search
  seq = numpy.random.randint(1,32767, 100)
  start1 = time.clock()
  Interpolation_Search(seq, 6)
  end1 = time.clock()
  msec1 = (end1 - start1) * 1000
  print("interpolation search using N=100 takes %.12f" % msec1, "milliseconds")
  
  #binary search
  start2 = time.clock()
  Binary_Search(seq, 6)
  end2 = time.clock()
  msec2 = (end2 - start2) * 1000
  print("binary search using N=100 %.12f" % msec2,"milliseconds" )

  
 # when N =1000
  seq = numpy.random.randint(1,32767, 1000)
  start1 = time.clock()
  Interpolation_Search(seq, 6)
  end1 = time.clock()
  msec1 = (end1 - start1) * 1000
  print("interpolation search using N=1000 takes %.12f" % msec1, "milliseconds")
  
  #binary search
  start2 = time.clock()
  Binary_Search(seq, 6)
  end2 = time.clock()
  msec2 = (end2 - start2) * 1000
  print("binary search using N=1000 takes %.12f" % msec2, "milliseconds")

 
  
  # when N = 5000
  #interpolation search
  seq = numpy.random.randint(1,32767, 5000)
  start1 = time.clock()
  Interpolation_Search(seq, 6)
  end1 = time.clock()
  msec1 = (end1 - start1) * 1000
  print("interpolation search using N= 5000 takes %.12f" % msec1, "milliseconds")

    #binary search
  start2 = time.clock()
  Binary_Search(seq, 6)
  end2 = time.clock()
  msec2 = (end2 - start2) * 1000
  print("binary search using N=5000 takes %.12f" % msec2, "milliseconds")

if __name__ == "__main__":
    main()