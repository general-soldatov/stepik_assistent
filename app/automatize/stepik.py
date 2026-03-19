import requests
from typing import Dict
from app.models.stepik import Section, Lesson, StepSource, Unit

class StepikAPI:
    def __init__(self, config: Dict[str, str]):
        self.token = self._get_token(**config)
        self.base_url = "https://stepik.org/api"
        self.headers = {
            'Authorization': f'Bearer {self.token}'
        }

    @staticmethod
    def _get_token(client_id, client_secret):
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        resp = requests.post('https://stepik.org/oauth2/token/',
                             data={'grant_type': 'client_credentials'}, auth=auth)
        return resp.json()['access_token']

    @staticmethod
    def _request_post(url: str, headers: Dict[str, str], data: Dict):
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def post(self, point: str, data: dict):
        return self._request_post(
            url=f"{self.base_url}/{point}",
            headers=self.headers,
            data=data
        )[point][0]

    def create_section(self, section: Section) -> Dict:
        module_data = {"section": section.model_dump()}
        return self.post('sections', module_data)

    def create_lesson(self, lesson: Lesson) -> Dict:
        data = lesson.model_dump()
        data['is_public'] = False
        module_data = {"lesson": data}
        return self.post('lessons', module_data)

    def create_step(self, step: StepSource) -> Dict:
        module_data = {"stepSource": step.model_dump()}
        return self.post('step-sources', module_data)

    def create_unit(self, unit: Unit) -> Dict:
        module_data = {"unit": unit.model_dump()}
        return self.post('units', module_data)
