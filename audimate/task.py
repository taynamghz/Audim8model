# src/audimate/config/tasks.yaml

script_analysis_task:
  description: >
    Analyze the uploaded script and extract emotional and psychological traits 
    of the character profiles based on the role descriptions. Focus on the 
    underlying emotional tones, psychological aspects, and character depth.
  expected_output: >
    A detailed character profile including emotional and psychological traits 
    of the characters, ready for the director’s review.
  agent: script_analyst

rubric_creation_task:
  description: >
    Allow the director to refine the extracted character traits and create 
    customized profiles based on specific casting needs. Provide options for 
    trait adjustments and customizations.
  expected_output: >
    A finalized rubric containing customized traits for character profiles, 
    ready to be used for matching actors.
  agent: rubric_editor

performance_analysis_task:
  description: >
    Process the self-taped audition videos, evaluating the actor’s facial 
    expressions, body language, and vocal delivery. Assess the actor’s fit 
    based on emotional tone and alignment with the character.
  expected_output: >
    A performance evaluation scorecard for each actor, including a breakdown 
    of their facial expressions, body language, and vocal tone.
  agent: video_analyzer

actor_matching_task:
  description: >
    Match actors to the character profiles using the extracted emotional 
    and psychological traits. Rank actors based on how well they align with 
    the character requirements.
  expected_output: >
    A ranked shortlist of actors, with each actor’s match score indicating 
    their suitability for the role.
  agent: matching_agent

feedback_learning_task:
  description: >
    Integrate feedback from the director to improve the trait weighting system. 
    Adjust actor rankings based on the feedback to refine future casting decisions.
  expected_output: >
    An updated agent learning model reflecting the director’s feedback and 
    improved trait reweighting for future actor matching.
  agent: learning_agent
