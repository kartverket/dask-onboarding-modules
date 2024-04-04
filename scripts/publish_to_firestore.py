import os
from google.cloud import firestore


def update_pull_request_url():
    project_id = os.environ["GCP_PROJECT_ID"]
    step_id = os.environ["STEP_ID"]
    team = os.environ["TEAM_NAME"]
    url = os.environ["PULL_REQUEST_URL"]
    db = firestore.Client(project=project_id)
    doc_ref = db.collection(u'onboarding').document(team)
    doc_ref.update({
        u'pr.`'+step_id+"`" : url,
    })

if __name__ == '__main__':
    update_pull_request_url()