# body-part-detection

What is haar cascade?
  viola-jones algorithm
haar cascade data set contains:

24 * 24 target window is moving on to the image and it contains features like(line features,rectenguler feature,edge feature etc..)
value of feature is computed using concept of integral images(it would select best value of featuure among this by using adabush classifier)

haar cascade is 4 step process:
1). haar feature(white-black boxes)
2). integral images approach(to fasten the process of computation of delta)
3). adaboost classifier(extracting best feature and discarding non-relevaent features)

integral image :
integral image contains pixel with value of sum of above all pixels and sum of left all pixel

How to train Own Haar Cascade?

opencv provides you pre trained haar cascade like(eye,frontalface,licence plate rus,lower body
,profile face ,right eye,smile,etc...)


proces to create your own haar cascade 
1) file provided by auckland university to cretae haar cascade using commmand prompt
but it is very tedious process and not that much of accurate(training time is more)

2) method provided by youtuber sendex  but acutually it not uses windows to create haar
cascade it uses aws ($5/month)

3) amin ahemadi gui creater for creating haar cascade(cascade-trainer-gui)(Most Preferable)

haar features(haar wavelet) is sequence of rescaled square-shaped functions very similar to 
fourier analysis.
-->they are like convolutional kernels
-->haar features are relavent feature for object detection and non-relevent features are 
descarded by adaboost algorithms


