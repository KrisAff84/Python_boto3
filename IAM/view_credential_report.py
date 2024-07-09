"""
This script takes user input for an AWS CLI profile, then retrieves the IAM 
credential report for that account. If a credential report is not ready, expired, 
or not present, a new report is generated. The script parses the report in a human
readable format and prints to the console.
"""

import json
import time
import csv
import io
import boto3

profile = (input("AWS Profile: "))
session = boto3.session.Session(profile_name=profile)
iam = session.client('iam')

report_ready = False

while not report_ready:
    try:
        response = iam.get_credential_report()
        content = response['Content'].decode('utf-8')
        report_ready = True

    except iam.exceptions.CredentialReportNotReadyException: 
        print("Waiting for credential report to generate...")
        time.sleep(3)

    except (iam.exceptions.CredentialReportNotPresentException, iam.exceptions.CredentialReportExpiredException):
        print("Generating credential report...")
        response = iam.generate_credential_report()
        time.sleep(3)

keys, *credential_report = csv.reader(io.StringIO(content))

credentials = {}
full_credential_report = []
for record in credential_report:
    key_index = 0
    for key in keys:
        credentials[key] = record[key_index]
        key_index += 1

    full_credential_report.append(credentials.copy())

for credential in full_credential_report:
    print(f'{json.dumps(credential , indent=2)}\n')
