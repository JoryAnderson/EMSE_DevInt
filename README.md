# EMSE_DevInt
By Cassandra, Nimmi, Yiming, and Jory.

This research was conducted as part of SENG 480A @ UVic (EMSE). 

[The included PDF](A_Replication_of_An_Empirical_Study_on_Developer_Interactions_in_Stack_Overflow.pdf) 
presents the motivation, methodology, results, and conclusions of our work and findings.

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
    
    d. Format into input file for LDA.

2. **Use LDA to process data**.
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
