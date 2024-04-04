import os
from google.cloud import firestore


def update_pull_request_url():
    step_id = os.environ["STEP_ID"]
    team = os.environ["TEAM_NAME"]
    api_url = os.environ["PULL_REQUEST_URL"]
    url = api_url.replace("https://api.github.com/repos", "https://github.com").replace("pulls", "pull")
    db = firestore.Client()
    doc_ref = db.collection(u'onboarding').document(team)
    doc_ref.update({
        u'pr.`'+step_id+"`" : url,
    })

if __name__ == '__main__':
    update_pull_request_url()