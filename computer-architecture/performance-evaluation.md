# Performance Evalutation


## Common metric for performance

### Latency

- Measure the how much time takes from the task started until it is done 

### Throughput

- Measure how many tasks can be done in unit time


## Performance comparsion

- We usually say "X is Y times faster than Z", then Y is the speed up

-  Y = speed(X) / speed(Z), similiar logic can be applied to throughput measurement, but not latency

- As latency is not directly propotional to performance, but inversely propotional, larger the latency, slower the speed => Y = latency(Z) / latency(X)

### Interpretation of performance

- speedup > 1 => performance improved

- speed <= 1 => performance unchanged or even worse than before 

### Summarizing the performance

- simple average cannot be directly to speedup (taking average of all speedup ratio of each computer). 
  
- The correct way to calculate the average speedup among all application, is to applying the average to the metric itself, and calculate the speedup separately
  
- Another way is to directly applpy geometric mean of the speedup, the result will be the same as finding the geometric mean of the metric and calculate the speedup because of the following:

<!-- $$
\frac{\sqrt[n]{speedup(A_1) * speedup(A_2) * ... * speedup(A_n)}}{\sqrt[n]{speedup(B_1) * speedup(B_2) * ... * speedup(B_n)}} = \sqrt[n]{\frac{speedup(A_1)}{speedup(B_1)} * \frac{speedup(A_2)}{speedup(B_2)} * ... * \frac{speedup(A_n)}{speedup(B_n)} }
$$ --> 

<div align="center"><img src="../svg/esgQhVfKcJ.svg"/></div>
