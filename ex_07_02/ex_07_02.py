# Write a program to prompt for a file name, and then read through the file and look for lines of the form: "X-DSPAM-Confidence: 0.8475" When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence. Test your file on the mbox.txt (0.894128046745) and mbox-short.txt(0.750718518519) files.