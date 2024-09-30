No Visual Studio, modo Debug,
Minha Rotina
```
	n  tflop GFLOPS
       (ns)
  100  1.50   0.71
 1000  1.36   0.73
10000  1.32   0.75
```
Minha Rotina Relase -O2
```
	n  tflop GFLOPS
       (ns)
  100  0.11   8.73
 1000  0.11   8.73
10000  0.11   8.75
```





Rotinas BLAS DAXPY  (y= a* x + y)
```
	n  tflop GFLOPS
       (ns)
  100  0.14    6.8
 1000  0.045  21.7
10000  0.071  14.0
20000  0.11    9.0  
40000  0.14    7.1
```


No modo Release  -O2 (otimizado)
```
	n  tflop GFLOPS
       (ns)
  100  0.12    8.1
 1000  0.042  23.4
10000  0.062  16.0
20000  0.041  24.4  
40000  0.029  33.7
80000  0.030  27.6
```

python, usando listas
```
	n  tflop GFLOPS
       (ns)

 1000  100   0.01 
10000  100   0.01
20000  100   0.01
```


python, usando numpy e loops
```
	n  tflop GFLOPS
       (ns)

 1000  200   0.005 
10000  200   0.005
20000  200   0.005
```



python, usando numpy
```
	n  tflop GFLOPS
       (ns)

 1000  0.98  1.01
10000  0.37  2.64
20000  0.38  2.56
```





