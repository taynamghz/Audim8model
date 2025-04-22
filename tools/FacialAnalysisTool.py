from deepface import DeepFace
import cv2
import numpy as np

class FacialAnalysisTool:
    def analyze(self, image_path: str):
        """
        Analyzes facial features including age group, face shape, symmetry, etc.
        """
        # Perform facial analysis
        result = DeepFace.analyze(image_path, actions=['age', 'gender', 'race', 'emotion', 'facial_landmarks'])

        # Extract and classify various features
        face_data = {
            "AgeGroup": self.classify_age(result['age']),
            "FaceShape": self.classify_face_shape(result['facial_landmarks']),
            "SymmetryLevel": self.classify_symmetry(result['facial_landmarks']),
            "FeatureProminence": self.classify_feature_prominence(result['facial_landmarks']),
            "SkinTone": result['dominant_race'],
            "BasicEmotion": result['dominant_emotion'],
            "EmotionIntensity": self.classify_emotion_intensity(result['emotion']),
        }
        
        return face_data

    def classify_age(self, age):
        """
        Classifies the age group based on the detected age.
        """
        if age < 13:
            return "Child"
        elif age < 18:
            return "Teen"
        elif age < 30:
            return "YoungAdult"
        elif age < 60:
            return "MiddleAged"
        else:
            return "Senior"
    
    def classify_face_shape(self, facial_landmarks):
        """
        Classifies the face shape based on facial landmarks.
        This is a simplified version and can be expanded further.
        """
        # Example simplified logic (to be improved with actual geometric analysis)
        left_cheek = facial_landmarks['left_cheek']
        right_cheek = facial_landmarks['right_cheek']
        chin = facial_landmarks['chin']
        
        # Use simple geometric checks to determine face shape (for example purposes)
        distance_cheeks = np.linalg.norm(np.array(left_cheek) - np.array(right_cheek))
        distance_chin = np.linalg.norm(np.array(chin) - np.array([0, 0]))  # Simplified

        if distance_cheeks > distance_chin:
            return "Oval"
        else:
            return "Round"

    def classify_symmetry(self, facial_landmarks):
        """
        Classifies the symmetry of the face based on landmarks.
        """
        # Compare the symmetry of facial landmarks (dummy logic)
        left_eye = facial_landmarks['left_eye']
        right_eye = facial_landmarks['right_eye']
        
        # Calculate distance between eyes (simplified logic)
        distance_eyes = np.linalg.norm(np.array(left_eye) - np.array(right_eye))
        
        if distance_eyes < 10:
            return "HighSymmetry"
        elif distance_eyes < 20:
            return "ModerateSymmetry"
        else:
            return "LowSymmetry"
    
    def classify_feature_prominence(self, facial_landmarks):
        """
        Classifies feature prominence based on the facial landmarks.
        """
        # Dummy logic for feature prominence based on cheekbones and jawline
        left_cheek = facial_landmarks['left_cheek']
        right_cheek = facial_landmarks['right_cheek']
        jawline = facial_landmarks['jawline']
        
        # Calculate the prominence of features (simplified)
        cheekbones_distance = np.linalg.norm(np.array(left_cheek) - np.array(right_cheek))
        jawline_distance = np.linalg.norm(np.array(jawline[0]) - np.array(jawline[1]))

        if cheekbones_distance > jawline_distance:
            return "HighCheekbones"
        elif jawline_distance > cheekbones_distance:
            return "StrongJawline"
        else:
            return "SoftJawline"
    
    def classify_emotion_intensity(self, emotion_dict):
        """
        Classifies the intensity of emotions based on the provided emotion dictionary.
        """
        max_emotion = max(emotion_dict, key=emotion_dict.get)
        intensity = emotion_dict[max_emotion]
        
        if intensity > 0.75:
            return "Intense"
        elif intensity > 0.5:
            return "Moderate"
        else:
            return "Subtle"
