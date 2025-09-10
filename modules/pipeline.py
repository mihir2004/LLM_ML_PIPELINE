import json
from modules.llm_client import call_llm

PIPELINE_TEMPLATE = open('prompts/pipeline.txt').read()

def generate_pipeline(schema_json: dict) -> dict:
    prompt = PIPELINE_TEMPLATE.replace('{{schema_json}}', json.dumps(schema_json))
    llm_output = call_llm(prompt)
    bundle = json.loads(llm_output)
    return bundle

def regenerate_pipeline(original_pipeline: dict, tweak_instruction: str) -> dict:
    context = json.dumps(original_pipeline)
    prompt = f"Given these pipeline files: {context}\nApply this change: {tweak_instruction}\nRespond with the full updated JSON bundle."
    llm_output = call_llm(prompt)
    updated = json.loads(llm_output)
    return updated
