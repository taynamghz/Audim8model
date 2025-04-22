#!/usr/bin/env python
# src/audimate/main.py
import sys
from audimate.crew import AudimateCrew

def run():
    """
    Run the Audimate crew for casting and performance analysis.
    """
    inputs = {
        'topic': 'Saudi Film Industry Casting'
    }
    AudimateCrew().crew().kickoff(inputs=inputs)
