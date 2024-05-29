# Translating and Integrating LGBTQ+ Vocabularies

## Introduction
This repository correspons to the master's thesis of Maria Adamidou in 2024.

This repository corresponds to the development and evaluation of a pipeline aimed at facilitating the translation of Homosaurus terms using automatic translation methods, alongside an exploration of the current state of mappings to and from Homosaurus. The goal is to create a pipeline that streamlines the translation process for experts, reducing their workload.

The methodology involves curating a set of tokens by analyzing token frequencies from Homosaurus, QLIT, IHLIA, and the Queerlit database. These tokens are then translated by experts and used to enhance initial translations obtained from DeepL, the automatic translation tool utilized. Evaluation of the translated terms involves the application of exact match and similarity algorithms, supplemented by expert assessments.



The script [DeepL_translations](DeepL_translations.py) generates the translation from the [input.csv](input.csv) file to the language chosen by the user.

The [input.csv](input.csv) file can be any text the user wants. In this thesis we used the Homosaurus terms in English.

The translations then were refined by the tokens the experts translated and evaluated using the two other scripts created for this thesis: [Exact_match.py](Exact_match.py) and [similarity.py](similarity.py)

Both of these evaluation scripts have as inputs two csv files what change according to what needs to be compared. 
