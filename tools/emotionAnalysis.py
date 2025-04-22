import cv2
import librosa
import numpy as np
from deepface import DeepFace
from moviepy.editor import VideoFileClip
import os
import statistics

class VideoEmotionAnalysisWithStatsTool:
    def __init__(self, video_path):
        self.video_path = video_path
        self.audio_path = "extracted_audio.wav"
        self.extract_audio_from_video()

    def extract_audio_from_video(self):
        """Extracts audio from the video and saves it as a .wav file"""
        clip = VideoFileClip(self.video_path)
        clip.audio.write_audiofile(self.audio_path)
        
    def analyze(self):
        """
        Analyzes both facial expressions and audio for emotional features.
        
        Returns:
            dict: A dictionary containing emotion data with statistical analysis.
        """
        # Facial emotion analysis from video frames
        video_emotions = self.analyze_facial_emotions()

        # Audio emotion analysis from audio
        audio_emotions = self.analyze_audio_emotions()

        # Combine the results
        result = {
            "VideoEmotions": video_emotions,
            "AudioEmotions": audio_emotions
        }

        # Optionally clean up audio file after analysis
        os.remove(self.audio_path)

        return result

    def analyze_facial_emotions(self):
        """
        Analyzes the facial expressions in the video to detect emotions and calculates statistics.
        
        Returns:
            dict: Facial emotion data with statistics.
        """
        video_capture = cv2.VideoCapture(self.video_path)
        facial_emotions = []
        emotion_counts = {}
        frame_count = 0

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break  # End of video

            # Analyzing emotion from each frame
            result = DeepFace.analyze(frame, actions=['emotion'])
            dominant_emotion = result[0]['dominant_emotion']
            facial_emotions.append(dominant_emotion)
            
            # Count emotion occurrences
            emotion_counts[dominant_emotion] = emotion_counts.get(dominant_emotion, 0) + 1
            frame_count += 1

        video_capture.release()

        # Statistics for facial emotions
        emotion_frequency = {emotion: count / frame_count for emotion, count in emotion_counts.items()}
        most_common_emotion = max(emotion_counts, key=emotion_counts.get)
        emotion_consistency = statistics.stdev([emotion_counts[emotion] for emotion in emotion_counts]) / frame_count

        return {
            "DominantFacialEmotion": most_common_emotion,
            "EmotionPerFrame": facial_emotions,
            "EmotionFrequency": emotion_frequency,
            "EmotionConsistency": emotion_consistency
        }

    def analyze_audio_emotions(self):
        """
        Analyzes the audio (from the extracted .wav file) for emotional features and calculates statistics.
        
        Returns:
            dict: Audio emotion data with statistics.
        """
        # Load audio file
        y, sr = librosa.load(self.audio_path, sr=None)

        # Pitch analysis
        pitch, _ = librosa.core.piptrack(y=y, sr=sr)
        pitch_range = self.calculate_pitch_range(pitch)

        # Volume analysis (root mean square energy)
        volume_level = self.calculate_volume_level(y)

        # Tone analysis (simplified as pitch range based)
        tone_type = self.calculate_tone_type(pitch_range)

        # Rhythm analysis (using tempo and onset detection)
        rhythm_pattern = self.calculate_rhythm_pattern(y, sr)

        # Calculate pitch statistics
        pitch_values = pitch[pitch > 0]  # Filter out zeros (no pitch)
        pitch_stats = {
            "PitchAvg": np.mean(pitch_values),
            "PitchStdDev": np.std(pitch_values),
            "PitchMedian": np.median(pitch_values)
        }

        # Volume statistics
        volume_stats = {
            "VolumeAvg": np.mean(np.abs(y)),
            "VolumeMax": np.max(np.abs(y)),
            "VolumeMin": np.min(np.abs(y))
        }

        return {
            "PitchRange": pitch_range,
            "VolumeLevel": volume_level,
            "ToneType": tone_type,
            "RhythmPattern": rhythm_pattern,
            "PitchStats": pitch_stats,
            "VolumeStats": volume_stats
        }

    def calculate_pitch_range(self, pitch):
        """
        Calculate pitch range based on the detected pitch over time.
        
        Args:
            pitch (np.array): Array of pitch values from librosa's piptrack.
        
        Returns:
            float: The pitch range (difference between max and min pitch).
        """
        pitch_values = pitch[pitch > 0]  # Filter out zeros (no pitch)
        if pitch_values.size == 0:
            return 0.0
        return np.max(pitch_values) - np.min(pitch_values)

    def calculate_volume_level(self, y):
        """
        Calculate the volume level of the audio.
        
        Args:
            y (np.array): The audio signal.
        
        Returns:
            float: The average volume level.
        """
        return np.mean(np.abs(y))  # Root mean square energy of the signal

    def calculate_tone_type(self, pitch_range):
        """
        Simplified classification of tone type based on pitch range.
        
        Args:
            pitch_range (float): The range of pitch in Hz.
        
        Returns:
            str: A classification of the tone type.
        """
        if pitch_range < 100:
            return "SoftSpoken"
        elif 100 <= pitch_range < 250:
            return "Normal"
        else:
            return "Commanding"

    def calculate_rhythm_pattern(self, y, sr):
        """
        Analyze the rhythm pattern of the speech using tempo and onset detection.
        
        Args:
            y (np.array): The audio signal.
            sr (int): Sampling rate of the audio.
        
        Returns:
            str: The rhythm pattern classification (e.g., "Steady", "Erratic", "Hesitant").
        """
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
        
        if tempo < 90:
            return "Hesitant"
        elif tempo < 120:
            return "Steady"
        else:
            return "Erratic"
