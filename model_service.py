from typing import Dict
import tiinfer

class AdderModel(tiinfer.Model):
    def __init__(self, model_dir: str):
        super().__init__(model_dir)

    def load(self) -> bool:
        self.ready = True
        return self.ready

    def preprocess(self, request: Dict) -> Dict:
        return request

    def predict(self, request: Dict) -> Dict:
        return {'result': request['a'] + request['b']}

    def postprocess(self, result: Dict) -> Dict:
        return result