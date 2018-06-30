from django.contrib import admin

# Register your models here.
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_api_key="5578277a486a2c548a852ad0e6a935f91f7fb9cf")

with open('./fruitbowl.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters = json.dumps({
            'classifier_ids': ["food"]
        }))
print(json.dumps(classes, indent=2))
