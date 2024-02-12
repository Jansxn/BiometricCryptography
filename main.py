import fingerprint_feature_extractor
import cv2

if __name__ == '__main__':
    img = cv2.imread('./1.jpg', 0)
    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(img, spuriousMinutiaeThresh=10, invertImage = False, showResult=False, saveResult = True)
    
    print('Ridge endings:')
    for i in range(len(FeaturesTerminations)):
        print(FeaturesTerminations[i].locX, FeaturesTerminations[i].locY)
        
    print('Ridge bifurcations:')
    for i in range(len(FeaturesBifurcations)):
        print(FeaturesBifurcations[i].locX, FeaturesBifurcations[i].locY)