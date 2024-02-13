import fingerprint_feature_extractor
import numpy as np
import cv2

def printDetails( FeaturesTerminations, FeaturesBifurcations):
    print('Ridge endings:')
    for i in range(len(FeaturesTerminations)):
        print(FeaturesTerminations[i].locX, FeaturesTerminations[i].locY)
        
    print('Ridge bifurcations:')
    for i in range(len(FeaturesBifurcations)):
        print(FeaturesBifurcations[i].locX, FeaturesBifurcations[i].locY)
        
def interleave_arrays(arr1, arr2):
    interleaved = []
    # Determine the length of the shorter array
    min_length = min(len(arr1), len(arr2))
    
    # Interleave elements until the end of the shorter array
    for i in range(min_length):
        interleaved.append(arr1[i])
        interleaved.append(arr2[i])
    
    # Append remaining elements from the longer array, if any
    if len(arr1) > min_length:
        interleaved.extend(arr1[min_length:])
    elif len(arr2) > min_length:
        interleaved.extend(arr2[min_length:])
    
    return interleaved

# extract minutiae feature
def extract_minutiae(image:np.ndarray, n_features:int = 80) -> np.ndarray:
    """extract minutiae features of a finger print.
    finally select the first n features that model builed on.
    Args:
    image (np.ndarray): image input
    n_features (int) : number of requeired features
    return:
    (np.ndarray): extraced features
    """
    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(image, spuriousMinutiaeThresh=10, invertImage=True)
    feature_list = []
    # printDetails(FeaturesTerminations, FeaturesBifurcations)
    minutiea_feature = interleave_arrays(FeaturesTerminations, FeaturesBifurcations)
    
    for featuer in minutiea_feature:
        if featuer.Type == 'Bifurcation':
            feature_type = 1
        else:
            feature_type = 0
        feature_list.append([featuer.locX, featuer.locY, feature_type, featuer.Orientation[0]])
        if len(feature_list) > n_features: break
        
    # select first n features
    if len(feature_list) < n_features:
        # zero pad to meen n_features requiement
        for _ in range(len(feature_list),n_features):
            feature_list.append([0,0,0,0])
        else:
            feature_list = feature_list[:n_features]
    return np.array(feature_list)

if __name__ == '__main__':
    img = cv2.imread('./1.jpg', 0)
    print(extract_minutiae(img, 7))
    # FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(img, spuriousMinutiaeThresh=10, invertImage = False, showResult=False, saveResult = True)
