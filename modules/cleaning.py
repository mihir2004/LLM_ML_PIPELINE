import json
from modules.llm_client import call_llm

PROMPT_TEMPLATE = open('prompts/cleaning.txt').read()

def suggest_cleaning(qc_json: dict, sample_records: list) -> list:
    prompt = PROMPT_TEMPLATE.replace('{{qc_json}}', json.dumps(qc_json))
    prompt = prompt.replace('{{sample_records}}', json.dumps(sample_records))
    llm_output = call_llm(prompt)
    suggestions = json.loads(llm_output)
    return suggestions
