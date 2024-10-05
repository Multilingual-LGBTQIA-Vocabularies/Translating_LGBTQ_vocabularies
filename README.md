# Translating and Integrating LGBTQ+ Vocabularies

## Introduction
This repository documents Maria Adamidou' s master's thesis completed in 2024.

This repository corresponds to the development and evaluation of a pipeline aimed at facilitating the translation of Homosaurus terms using automatic translation methods, along with an examination of the current state of mappings to and from Homosaurus. The objective is to create a pipeline that streamlines the translation process for experts, reducing their workload.

The methodology involves curating a set of tokens, using two different Methods, by analyzing token frequencies from Homosaurus, QLIT, IHLIA, and the Queerlit database. These tokens are then translated by human experts and used to enhance initial translations obtained from the automatic translation tool DeepL. Evaluation of the translated terms involves the application of an exact match algorithm and three similarity algorithms, which measure various aspects of the translation fidelity, as described later. The translations were then evaluated by volunteers. Spanish volunteers evaluated the alphabetically first 499 terms, while French evaluated the 142 terms that are considered easy to translate and validate. Finally, the exploaration of the current state of mappings from Homosaurus to LCSH, QLIT and GSSO was conducted, shedding light on potential implications.

## Using DeepL and refining the translations

The Python script located in the folder /Scripts/DeepL_translation with the file name ```DeepL_translations.py``` generates the translation from the ```Homosaurus_english_prefLabel.csv``` file, which is in the same folder, to the language chosen by the user. This csv file contains just the English prefLabel Homosaurus terms. For more extensive information of the Homosaurus terms used, refer to the file ```Dutch_English_PrefLabel_AltLabel_HomosaurusURI.xlsx``` in the /Data/Homosaurus folder. This Excel file contains the URI, English prefLabel and altLabel, and Dutch prefLabel and altLabel of Homosaurus. In the same folder there are the files ```v3.3.nt``` and ```hs-nl.json```, which are the versions of Homosaurus used in this thesis.

The ```Homosaurus_english_prefLabel.csv``` file can contain any text the user wants to translate. In this thesis, the Homosaurus terms in English were used. To translate into different languages, locate line 35 of the Python script and change the language code from "NL" to "SV" for Swedish, "FR" for French, "ES" for Spanish, etc. Detailed instructions for alternative uses of files and further instructions are provided at the top of every Python script used in this thesis, ensuring correct usage and customization.

The resulting files containing the naive DeepL translations can be found in the following folders:

- /Results/Dutch_translations: File called ```output_dutch_DeepL.csv```.
- /Results/Swedish_translations: File called ```output_swedish_DeepL.csv```.
- /Results/French_translations: File called ```output_french_DeepL.csv```.
- /Results/Spanish_translations: File called ```output_spanish_DeepL.csv```.

Two (manually constructed) Methods were proposed for the creation of the set of tokens as outlined in the following table:

|    Source   |   Method A  | Method B |
|-----------|-----------|-----|
| #tokens from Homosaurus terms      | - |  40 tokens |
| #tokens from QLIT terms      | - |  40 tokens | 
| #tokens from combined Homosaurus and QLIT dataset      | 60 tokens |  -| 
| #tokens of high frequency in IHLIA      | 30 tokens |  50 tokens |
| #tokens of high frequency in QueerLit      | 30 tokens |  50 tokens | 
| Total #tokens     | 83 tokens |  101 tokens |

The frequencies used for the creation of the Methods can be found in the folder /Data/Frequencies. Specifically:
- The file ```Homosaurus-frequencies.xlsx``` contains the Homosaurus frequencies and the file ```QLIT_frequencies.xlsx``` contains the QLIT frequencies, both generated using Google Sheet tools.
- The file ```Queerlit_database_frequencies.xlsx``` contains the frequencies of the Queerlit database sent by the Swedish expert.
- The file ```IHLIA_frequencies.csv``` contains the IHLIA frequencies sent by the Dutch expert. 

The folder /Data/QLIT contains the following files:
- ```QLIT_in_Homosaurus.xlsx```: This file, provided by the Swedish expert, contains QLIT terms that were translated from Homosaurus and have links to it.
- ```QLIT_not_in_Homosaurus.xlsx```: Also provided by the Swedish expert, this file contains QLIT terms that do not have links to Homosaurus.
- ```QLIT.csv```: This file contains all the QLIT terms merged together.

The set of tokens generated by Method A is stored in the file ```Method_A.csv``` and those generated by Method B are in ```Method_B.csv``` both located in the folder /Data/Methods.

The two sets of tokens were merged and sent to the experts for translation. This merged set of tokens, along with their Dutch, Swedish, French and Spanish expert translations, is stored in the file ```Experts_Token_translations.xlsx``` in folder /Data. 

The naive Deepl translations were then refined using the tokens translated and evaluated by the experts. The Python script ```Refinement.py```, located in the folder /Scripts/Refinement was used for this process. Additionally, the following files in this folder were used in conjunction with this Python script for the thesis:

- ```Method_A.csv``` and ```Method_B.csv```: Contain the tokens for Methods A and B.
- ```Homosaurus_english_prefLabel.csv```: Contains only the English prefLabel Homosaurus terms.
- ```experts_tokens_dutch.csv```, ```experts_tokens_swedish.csv```, ```experts_tokens_spanish.csv``` and ```experts_tokens_french.csv```: Contain all the English tokens sent to the experts alongside their Dutch, Swedish, Spanish, and French translations, respectively. 

The Dutch and Swedish results of this automatic refinement of the naive DeepL translations with the tokens from Method A and B by the script can be found in the following folders:

- /Results/Dutch_translations:

    - ```output_dutch_methodA_automatic.csv```: Contains the automatic refinement of the Dutch DeepL translations with Method A tokens by the python script.
    - ```output_dutch_methodB_automatic.csv```: Contains the automatic refinement of the Dutch DeepL translations with Method B tokens by the python script.
    
- /Results/Swedish_translations: 
 
    - ```output_swedish_methodA_automatic.csv```: Contains the automatic refinement of the Swedish DeepL translations with Method A tokens by the python script.
    - ```output_swedish_methodB_automatic.csv```: Contains the automatic refinement of the Swedish DeepL translations with Method B tokens by the python script.

As mentioned in the thesis, due to a bug encountered when sending translations to the Spanish and French experts, the French and Spanish results used in this thesis were manually generated instead of using this Python script. These manual refinements can be found in the following folders:

- /Results/French_translations. File named ```output_french_methodB_manual.csv```: The file contains the French translations modified manually by Method B tokens and sent to the French experts.
- /Results/Spanish_translations. File named ```output_spanish_methodB_manual.csv```: The file contains the Spanish translations modified manually by Method B tokens and sent to the Spanish experts. 


Finally, as mentioned in the thesis there was a further manual refinement of the Dutch and Swedish DeepL translations, which had already been refined automatically by the Python script. The resulting translations of these further manual refinements can be found in the following folders:

- /Results/Dutch_translations:

    - ```output_dutch_methodA_semi-manual.csv```: The file containing the Dutch DeepL translations with further manual refinement, previously refined automatically with Method A tokens by the python script.
    - ```output_dutch_methodB_semi-manual.csv```: The file containing the Dutch DeepL translations with further manual refinement, previously refined automatically with Method B tokens by the python script.
    
- /Results/Swedish_translations: 
 
    - ```output_swedish_methodA_semi-manual.csv```: The file containing the Swedish DeepL translations with further manual refinement, previously refined automatically with Method A tokens by the python script.
    - ```output_swedish_methodB_semi-manual.csv```: The file containing the Swedish DeepL translations with further manual refinement, previously refined automatically with Method B tokens by the python script.

## Exact Match evaluation

The naive DeepL translations and the two new DeepL translations, one including tokens from Method A and the other from Method B, were evaluated using an exact match Python script created for this thesis. The Dutch DeepL translations were compared against both the Dutch prefLabel and AltLabel of Homosaurus, while the Swedish DeepL translations against QLIT, which does not have an AltLabel. The exact match Python script created for this thesis, named ```Exact_match.py```, is located in folder /Scripts/Exact_Match. Additionally, the following files in this folder were used in conjunction with this Python script for the thesis:

- ```output_dutch_DeepL.csv```, ```output_dutch_methodA_automatic.csv```, ```output_dutch_methodB_automatic```, ```output_dutch_methodA_semi-manual.csv``` and ```output_dutch_methodA_semi-manual.csv```: Contain all the different versions of the Dutch translations (naive DeepL translations, automatically refined by Method A and B, automatically refined by Method A and B with further manual refinement) .
- ```output_swedish_DeepL.csv```, ```output_swedish_methodA_automatic.csv```, ```output_swedish_methodB_automatic```, ```output_swedish_methodA_semi-manual.csv``` and ```output_swedish_methodA_semi-manual.csv```: Contain all the different versions of the Swedish translations (naive DeepL translations, automatically refined by Method A and B, automatically refined by Method A and B with further manual refinement) .
- ```PrefLabel.csv``` and  ```AltLabel.csv```: Contain all the Dutch prefLabel and altLabel Homosaurus terms, respectively. 
- ```QLIT.csv```: Contains all the Swedish QLIT terms.

Each comparison is done separately. First, the Naive DeepL translations are compared with the AltLabel and then the PrefLabel. This process was repeated for the Method A and Method B DeepL translations, as well as for the Swedish translations with QLIT. The results of these Exact Match comparisons can be found in the folder /Results/Evaluation:

- ```Dutch_Exact_Match_Results.xlsx```: This Excel sheet contains all the possible comparisons between the Dutch files mentioned above and the Dutch prefLabel and altLabel of Homosaurus.
- ```Swedish_Exact_Match_Results.xlsx```: This Excel sheet contains all the possible comparisons between the Swedish files mentioned above and the QLIT terms.

## Similarity evaluation

The Dutch DeepL translations automatically refined with tokens from Method B and with further manual refinement, were also evaluated using 3 similarity measuers (Jaccard similarity, ratio algorithm, Levenshtein distance) using the Python script ```similarity.py```, located in folder /Scripts/Similarity_comparisons. The other files in this folder were used in conjunction with this script for the thesis and are the same as the ones used for the Exact Match evaluation.

Each comparison is done separately. The Naive DeepL translations are first compared with the AltLabel and then the PrefLabel. This process was then repeated for the Method A DeepL translation, Method B DeepL translation, and Swedish translations with QLIT. In this thesis, only the naive Dutch DeepL translation and the Dutch DeepL translations automatically refined by Method A and B tokens with further manual refinement were compared against the Homosaurus Dutch prefLabel. The results of these three similarity comparisons (Jaccard similarity, the ratio algorithm and the Levenshtein distance) can be found in the folder /Results/Evaluation:

- ```Dutch_similarity_results_DeepL.xlsx```: This Excel sheet contains the similarity results of the Jaccard similarity, the ratio algorithm and the Levenshtein distance for the Dutch naive DeepL translation and the Dutch Homosaurus prefLabel.
- ```Dutch_similarity_results_MethodA_semi-manual.xlsx```: This Excel sheet contains the similarity results of the Jaccard similarity, the ratio algorithm and the Levenshtein distance for the Dutch DeepL translations automatically refined by Method A tokens with further manual refinement and the Dutch Homosaurus prefLabel.
- ```Dutch_similarity_results_MethodB_semi-manual.xlsx```: This Excel sheet contains the similarity results of the Jaccard similarity, the ratio algorithm and the Levenshtein distance for the Dutch DeepL translations automatically refined by Method B tokens with further manual refinement and the Dutch Homosaurus prefLabel.

## Spanish and French volunteers' evaluation

Experts reviewed the translations to determine whether they were suitable for use without further modification, or if adjustments were necessary. A designation of **YES** indicated approval of the translation, while **NO** signified that changes were required. Additionally, an **Unsure** option was available for cases where the expert was uncertain about the adequacy of the translation. It's noteworthy that Spanish experts used the **Unsure** option, while the French did not. The evaluation process differed slightly between the two languages. The Spanish experts evaluated the first 499 terms alphabetically, while the French experts the 142 terms that are considered easy to translate and validate. The detailed results of the experts' evaluation can be found in the folder /Results/Evaluation in the files ```French_Experts_evaluation.xlsx``` and ```Spanish_Experts_evaluation.xlsx```. The first one contains the results of evaluation of the French Experts, while the second one contains the results of evaluation of the Spanish Experts. 

## Mapping and Issues

In the final phase of the study, the objective is to examine the current scope of links between LCSH, GSSO, QLIT, and Homosaurus, aiming to explore the consequences of integrating multilingual labels into Homosaurus. In file ```gsso.owl``` located in folder /Data/GSSO is the version of GSSO that was utilized in this thesis. Furthermore, in the file ```Mappings.xlsx``` located in folder /Results/Mapping are all the mappings explored in this thesis. These mappings include the links between Homosaurus version 3 and LCSH, the links between Homosaurus version 2 and 3 and GSSO, and the links between Homosaurus version 3 and QLIT. 

However, it's worth noting that GSSO is outdated, resulting in a lot of issues and version conflicts. Examples of these issues can be found in the file ```Issues_GSSO_Homosaurus_links.xlsx``` located in folder /Results/Mapping.

---------

This work gains insights into the automated translation of LGBTQ+ terms and the current mapping of links from and to Homosaurus. The key findings are summarized as below.

- Different Methods of token creation have little differences on their results but demonstrated variations in token selection. Future research could explore additional methods to further improve results.
- Evaluation results indicated that translations generated by the pipelines can serve as a foundation for longer LGBTQ+ translations, achieving over 65% accuracy in most evaluations.
- A lot of issues were found in the links between Homosaurus and GSSO due to the GSSO being outdated. Attempting to integrate new links may create even more issues.

-----

We used the packages

To reproduce the DeepL translations, you will need to create a DeepL account to get an API key for DeepL's API. Also, to use the scripts, these packages need to be installed:

- pip install deepl
- pip intall csv
- pip install fuzzywuzzy
- pip install Levenshtein

## Acknowledgements

I would like to start by expressing our gratitude to experts from IHLIA and the Homosaurus project for their support and contribution to this thesis, especially Jack van der Wel who was our Dutch expert, and his provision of the IHLIA data was crucial to our research. I would also like to thank Sandrine Vachon who was our French expert, and Olov Kriström, our Swedish expert, whose assistance with providing data from the Queerlit database and QLIT was immensely helpful.

## Other notes

- You can get more info about generating the DeepL API key here:
https://support.deepl.com/hc/en-us/articles/360020695820-API-Key-for-DeepL-s-API
