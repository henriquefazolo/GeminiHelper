import re


def parse_gemini_response(response_text):
    """
    Extracts content inside <text> tags, ignoring <reasoning>.
    """
    # Pattern to find content between <text> and </text>
    pattern = r"<text>(.*?)</text>"
    match = re.search(pattern, response_text, re.DOTALL)

    if match:
        return match.group(1).strip()
    else:
        return "ERRO DE FORMATACAO"

# Example usage with the raw output
# clean_output = parse_gemini_response(llm_output)