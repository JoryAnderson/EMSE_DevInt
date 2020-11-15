# EMSE_DevInt
For SENG 480A / UVic EMSE

By Cassandra, Nimmi, Yiming, and Jory.

# Dependencies
    pip install stackapi
    
That's all for now!

#  Tentative Requirements
1. **Use StackAPI to grab SO data**.

    a. Grab maximum questions & answers daily. Do over couple days.
    
    b. Collate JSONs into single data file.
    
    c. Remove duplicates
    
    d. Format into input file for JGibbLabeledLDA

2. **Use JGibbLabeledLDA to process data**.
    * Create Java package within this project?
    
    * LDA does not label topics. This will need to be done manually.
    
3. **Additional statistics**.

# Usage
[Grabbing Data](/python/APIDump/README.md)

# Resources
[StackAPI](https://stackapi.readthedocs.io/en/latest/user/intro.html)

[JGibbLabeledLDA](http://jgibblda.sourceforge.net/#3._How_to_Program_with_JGibbLDA)

[Refactored JGibbLabeledLDA](https://github.com/myleott/JGibbLabeledLDA)
