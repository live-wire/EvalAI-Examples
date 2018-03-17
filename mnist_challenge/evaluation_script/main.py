import sys
import os
import time
import numpy as np
import json
import copy
import numpy as np
import pandas as pd


def evaluate(annFile, resFile, phase_codename):
	# We will not use the annFile at all for evaluation

	userfilename = resFile
	answerfilename = "Data/answers.csv"

	user = pd.read_csv(userfilename)
	answers = pd.read_csv(answerfilename)

	submission_result = ""
	result = {}
    result['result'] = []
    result["submission_result"] = submission_result

	if len(user) != len(answers):
		submission_result = "Number of rows in the training data ("+str(len(answers))+") and the submission file ("+str(len(user))+") don't match."
		result["submission_result"] = submission_result
		return result

	temp = {}
	temp[phase_codename] = {}
	matches = 0
	for i in range(0, len(user)):
	    if user.iloc[i]['label'] == answers.iloc[i]['label']:
	        matches = matches+1
	score = (matches/len(user))*100
	print("Score:",score)
	temp[phase_codename]['score'] = score
	result['result'].append(temp)
	submission_result = "Evaluated scores for the phase "+str(phase_codename)+". Score="+str(score)
	result["submission_result"] = submission_result
    # Final accuracies as a dict with the following structure
    """
    {
      "result": [
        {
          "split_codename_1": {
            "key1": 30,
            "key2": 50,
            
          }
        },
        {
          "split_codename_2": {
            "key1": 90,
            "key2": 10,
            
          }
        },
        {
          "split_codename_3": {
            "key1": 100,
            "key2": 45,
            
          }
        }
      ],
      "submission_metdata": "data in any format here (only visible to challenge host)",
      "submission_result": "data in any format here (visible to both challenge host and challenge participant)"
    }
    """
    return result

