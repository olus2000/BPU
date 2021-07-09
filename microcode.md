#### Load command
0. PC->A; MEM->D; D->PR;


#### 0/1 - add/sub
1. DP->A; MEM->D; D->ALU; PC++;
2. DP->A; ALU->D; D->MEM;


#### 2/3 - move pointer
1. DP->D; D->ALU; PC++;
2. ALU->D; D->DP;


#### 4/5 - jump
1. PC->D; D->ALU; PC++;
2. DP->A; ALU->D; D->PC;


#### 6 - input
1. DP->A; I/O; D->MEM; PC++;
2. Next Command;


#### 7 - output
1. DP->A; MEM->D; I/O; PC++;
2. Next Command;
