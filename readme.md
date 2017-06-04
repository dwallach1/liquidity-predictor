
# Main page

We began with a file containing 150,000 examples. While this may seem good in theory, the data was undersampled
and therefore not fully representative of the model we were aiming to generate. Of the 150,000 examples 139,974 
were classified as 0 and only 10,0026 were classified as 1. This led to our ZeroR classification to be 
around 93%. The implications of this were that using more complex classifiers yielded only minimal increases 
(less than one percent). To combat the undersampling, we used a subset of our training data that had more even 
distrobution of classifications so that our ZeroR was a value closer to 50%. 