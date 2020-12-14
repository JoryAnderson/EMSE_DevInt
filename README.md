# EMSE_DevInt
For SENG 480A / UVic EMSE
By Cassandra, Nimmi, Yiming, and Jory.

# Dependencies
Download the following packages needed for the included python modules and Jupyter notebooks:

    pip install stackapi sklearn numpy nltk pandas seaborn wordcloud pyLDAvis
    
Alternatively, try

    pip install -r requirements.txt
    
#  (Rough) Procedural Overview
1. **Use StackAPI to grab SO data**.

    a. Grab maximum questions & answers daily. Do over couple days.
    
    b. Collate JSONs into single data file.
    
    c. Remove duplicates
    
    d. Format into input file for JGibbLabeledLDA

2. **Use JGibbLabeledLDA to process data**.
    * LDA does not label topics. This will need to be done manually.
    
3. **Additional statistics on questions, answers, and users**.

# Usage
[Ad-Hoc Python Scripts](/python/)

[Grabbing Data](python/lib/)

# Resources
[StackAPI](https://stackapi.readthedocs.io/en/latest/user/intro.html)

[JGibbLabeledLDA](http://jgibblda.sourceforge.net/#3._How_to_Program_with_JGibbLDA)

[Refactored JGibbLabeledLDA](https://github.com/myleott/JGibbLabeledLDA)

[Preprocess](http://derekgreene.com/slides/topic-modelling-with-scikitlearn.pdf)

[LDA](https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0)
