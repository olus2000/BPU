Memory layout: bumper | bytes from the user

Takes text from input terminated by an newline and returns it reversed

>22
+10 >1  Set cell to the bumper value and move over
,       Read a byte

-10 [6  Don't enter the loop if newline
  +10   Restore original value
  >1 ,  Move over and read a new byte
-10 ]4  Stop looping if newline

<1      Move to the last byte
-10 [6  Don't enter the loop if already at the end
  +10   Restore original value
  . <1  Write and move to the next byte
-10 ]4 Stop looping if at the end

+10 .  Set the bumper back to newline and print it
]19    Jump back to the start