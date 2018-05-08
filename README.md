# Project title

This project is about unsupervised sense clustering of translations. It is a subfield of machine translation and 
used there in order to improve or evaluate word translations.

## Motivation, method, hypotheses

The initial problem is that the translation of a single word in different contexts in L1 has often multiple target translations in L2. From those target translations one needs to pick carefully in order to match the context.
</br></br>
This is not even a problem restricted to machine translation. If we look at L2 language learners, they can not have the deep understanding and intuition of the language as a L1 speaker. L2 speakers will often just translate a word from their native language to a target language, not knowing that this would sound strange to a native speaker (because a different translation of the possible ones should have been used for a particular context).
</br></br>
From humans to machines: Knowing that humans make such mistakes quite a lot, one would not expect a statistical (machine translation) model to handle those problems with granularity ad hoc.
</br></br>
Method: soft Clustering
Monolingual features: PMI of a word with its neighbor
Bilingual features: PMI of a word and its translations
</br>
The evaluation will be a combination of manual evaluation and comparison to wordnet sense clusters.

## Task Adjustment

After some problems with the initial project, the project was reduced to a more rudimentary form.
The adjusted task was now to seperate two concepts via normal clustering, where each concept is realized as a list 
of words which are very similar to each other (list of cloth names vs. list of body parts).
As features a bag of words approach was used.
The monolingual and bilingual features were still both tested.
For the monolingual features a BOW with a window of 5 tokens was used.
For the bilingual features a BOW with the whole aligned sentence was used (due to missing word alignment).
Although I claim that the difference between a 5 window BOW and a total sentence BOW is not significant due to the corpus which was used. The corpus was the "OpenSubtitles" corpus. Since it contains transcriptions from movies and series the sentences in there are rather short (at least shorter than in corpus of written text).


## So far

Monolingual features, normal clustering:
</br>
Corpora:</br>
  COCA, COHA, GloWbe: performed really poorly. Translations like {good, nice} and {issue, problem, ..} are clustered randomly
  </br>
  EUROPARL: performed a bit better. Translations like {good, nice} and {issue, problem, ..} are clustered correctly into two clusters. But more complex translations which contain less frequent words are still a problem.


## Relevant literature 

A short list of literature (articles/books/blog posts/...). We will
pick some of the listed papers for further class discussion.

Mohit Bansal, John DeNero, Dekang Lin [_Unsupervised Translation Sense Clustering_](https://www.cs.unc.edu/~mbansal/papers/naacl12_translationSenseClustering.pdf)
</br>
Michael Denkowski, [ A Survey of Techniques for Unsupervised Word
Sense Induction ](https://www.cs.cmu.edu/~mdenkows/pdf/wsi2009.pdf) (Chapter 5 is translation related)
</br>
Marianna Apidianaki, Yifan He [ Marianna Apidianaki, Yifan He. An algorithm for cross-lingual sense-clustering tested in a MT evaluation
setting. International Workshop on Spoken Language Translation (IWSLT-2010), Dec 2010,
Paris, France. pp.219–226, 2010 ](https://hal.inria.fr/hal-00544745/document)



## Available data, tools, resources
Data for dictionaries: [ Bilingual Dictionaries for Offline Use ](https://en.wiktionary.org/wiki/User%3aMatthias_Buchmeier)
(as an alternative to the handcrafted dictionaries described in the 
[_Unsupervised Translation Sense Clustering_](https://www.cs.unc.edu/~mbansal/papers/naacl12_translationSenseClustering.pdf) paper)

[dictUtil.py](https://github.com/SfS-unsupervisedCL/project-translation_meaning_clustering/blob/master/dictUtil.py) is for extracting a pure dictionary from the above source which also contains POSTags, Descriptions, Use cases and other meta data.
<br>
Example item from en-de dict:
<br>
permanent --> {'permanent', 'unbefristet', 'Dauerwelle', 'beständig', 'dauerhaft', 'ständig', 'Permanente'}

Corpora from:
http://opus.nlpl.eu/



## Project members

- Johannes (Joapfel)
- Name (GitHubID) 
