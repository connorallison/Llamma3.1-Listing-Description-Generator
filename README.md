# Llamma3.1-Listing-Description-Generator


#### Data files 
housing_data_simulation1.csv is the original training data and the one that ended up yielding the best results. 
This was the file that was used to train the model that then generated the listing descriptions that we rated and compared to the training data. 

housing_data_simulation2.csv contains 40 additional listing description templetes and several additional features for each price point. 

housing_data_simulation test copy.csv contains the first fifty observations from housing_data_simulation1.csv without the listing descriptions column
This data was used as the test copy. 

#### Models 
*Llama_RealEstate_LLM* is the first successful model we created. It will train the base Llama model using the training data and then generate listing descriptions for the test set. 
It will take about 50min to train and 15 to generate a batch of 50 listing descritions. 

*Llama_RealEstate_LLM_withSave* is the same as Llama_RealEstate_LLM but when the model is trained, it is saved to the user's google drive. You will need to grant permission and have at least 5Gb

*Llama_RealEstate_LLM_Creative* contains additional fine-tuning, style tokens and additional prompts. This model does not work as well as the original. 

*UntrainedLlama3_1* uses the base llama model to generate listing descriptions. This will take a very long time to run. 

**Additional Notes** 
You will need a hugging face token and permission from Meta to use Llama3.1-8b. You will need to set up this token as a google secret


#### Evaluations
Both Listing Eval files and StaticEvalMetrics contain simple python code that takes the ratings for both sets of listing descriptions and compares them using a 2-sample t-test
