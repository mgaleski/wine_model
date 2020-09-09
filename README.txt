    This model was created with the objective of accurately predicting wine quality based on the 9 point scale.After testing three
different types of model (SVC, SGD, and RFC) SVC ended up providing only marginally lower macro average to the RFC model.
(88% vs 89% macro avg.) I settled on SVC as it had far superior precision at predicting high quality wines (96% vs 84%).
I tested each field individually to see how they affected the outcome of the models and ultimately using all of the available
datapoints except density (even those that don't look to have strong correlations in the visualizations) as features yielded the best results.
The datapoints that seem to have the strongest correlations with quality are volatile acidity, citric acid content, and sulphates.

    The dataset was usable as it came and required little to no transformation prior to modelling, and the only changes I made
before loading it to SQL were dropping some irrelevant columns and creating the wine_id column to be used as primary key.


Units:
Fixed acidity - (g(tartaric acid))/dm^3
Volatile acidity - (g(acetic acid))/dm^3
Citric acid -
Residual sugar
Chlorides
Free sulfur dioxide
Total sulfur dioxide
pH
Sulphates
Alcohol (vol%)