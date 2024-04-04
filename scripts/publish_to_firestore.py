import os
from google.cloud import firestore


def update_pull_request_url():
    step_id = os.environ["STEP_ID"]
    team = os.environ["TEAM_NAME"]
    url = os.environ["PULL_REQUEST_URL"]
    db = firestore.Client()
    doc_ref = db.collection(u'onboarding').document(team)
    doc_ref.update({
        u'pr.`'+step_id+"`" : url,
    })

if __name__ == '__main__':
    # os.environ["GCP_PROJECT_ID"] = "dataplattform-sandbox-6f27"
    # os.environ["AUTH_PROJECT_ID"] = "698137771009"
    # os.environ["SERVICE_ACCOUNT"] = "dataplattform-deploy@dataplattform-sandbox-6f27.iam.gserviceaccount.com"
    # os.environ["TEAM_NAME"] = "spotify"
    # os.environ["PULL_REQUEST_URL"] = "hahah.com"
    # os.environ["STEP_ID"] = "dask-infrastructure-setup"
    update_pull_request_url()