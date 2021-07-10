structure: n | f(n minus one) | f(n) | helper

>15 >32 go to start
,

RESET
>1  [3  -1  ]1      Clear first cell
>1  [3  -1  ]1      Clear second cell and add one
]9  +1  <2  [28     Intermediate jump for main loop and start fibonacci loop

FIBONACCI LOOP
>1  [6  >2  +1      Move first cell to helper
<2  -1  ]4  >1
[8  <1  +1  >2      Move second cell to helper and first cell
+1  <1  -1  ]6
>1  [6  <1  +1
>1  -1  ]4  <3      Move helper to second cell
-1  ]26 ]30         End loop and intermediate jump for main loop


OUTPUT AND RESTART
>2  .   <2  +1
]5