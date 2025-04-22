# src/audimate/config/tools.yaml

script_analysis_tool:
  description: >
    A tool for parsing and analyzing scripts to extract emotional and psychological traits of characters. 
    It uses advanced natural language processing techniques and the Allam LLM to identify key aspects of character development.
  required_libraries: 
    - GPT-4
    - Allam LLM
    - spaCy
  usage: >
    This tool is used by the Script Analyst Agent to process uploaded scripts and extract character traits.

rubric_editor_tool:
  description: >
    A tool for refining and customizing character profiles based on the director’s input. 
    It allows the adjustment of traits and offers preset options like “charismatic outsider” or “villain with a conscience.”
  required_libraries: 
    - Python
    - Pandas
  usage: >
    This tool is used by the Rubric Editor Agent to modify and refine character profiles, based on the director’s requirements.

performance_analysis_tool:
  description: >
    A multimodal AI tool that processes self-taped audition videos, analyzing facial expressions, body language, and vocal delivery. 
    It uses models like MediaPipe, DeepFace, and pyAudioAnalysis for emotional tone detection and body language evaluation.
  required_libraries: 
    - MediaPipe
    - DeepFace
    - pyAudioAnalysis
    - OpenCV
  usage: >
    This tool is used by the Video Analyzer Agent to assess actor performance based on video and audio data.

actor_matching_tool:
  description: >
    A tool that ranks actors by comparing their extracted traits to the desired character profile using a matching algorithm.
    It calculates the similarity score based on emotional tone, facial expressions, and vocal delivery.
  required_libraries: 
    - scikit-learn
    - NumPy
  usage: >
    This tool is used by the Matching Agent to generate a ranked shortlist of actors who best match the character profiles.

feedback_learning_tool:
  description: >
    A tool that incorporates director feedback to adjust trait weighting in the actor matching system. 
    It uses a custom learning engine to refine and improve the model based on continuous input.
  required_libraries: 
    - TensorFlow
    - Keras
    - Pandas
  usage: >
    This tool is used by the Learning Agent to incorporate feedback and adjust the model for future matching improvements.
