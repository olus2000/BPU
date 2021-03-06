# BPU
Designs and files for my Brainfuck Processing Unit.

BPU.circ is a [Logisim](http://www.cburch.com/logisim/) file containing all designs and examples included in [my tutorial](https://dev.to/olus2000/bal-1-designed-for-hardware-me7).

microcode.md explains how each command is executed by the BPU in 3 cycles.

compiler.py is an interactive command line tool for compiling BAL code to a Logisim-readable format.

Examples folder holds example programs that can be loaded into the computer's ROM and run. There are three kinds of files:
 - \*.bal (Brainfuck Assembly Language)
   
   Source code in BAL with comments.
   
 - \*.bcb (BAL compiled to binary)
 
   A binary file representing the initial memory state of the BPU. The standard format for compiled BAL.
   
 - \*.bcl (BAL compiled for Logisim)
 
   Format readable by Logisim to load the program into the ROM.

## Loading a program to Logisim
1. Open BPU.circ with Logisim.
2. Click on the ROM in the upper left corner of the main circuit.
3. In the ROM's properties there's a line "Contents: (click to edit)". Click it.
4. In the popup window click "Open..." and select the \*.bcl file you want to run.
5. Close the popup window.
6. Press the reset button on the bottom of the main circuit using the Poke tool (the hand on the left side of the toolbar).
7. Run the simulation (check out the "Simulate" menu).
