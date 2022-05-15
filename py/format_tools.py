import re

def mask_curly(match):
    match_text = match.group(0)
    return "<@" + match_text[1:-1] + "@>"

def unmask_curly(match):
    match_text = match.group(0)
    return "{" + match_text[2:-2] + "}"
    pass

def format_md_text(src_str, value):
    md_str = re.compile('\{(?!model|vendor|product_id|price|category)[a-z.=0-9 ]+\}', re.IGNORECASE)
    tmp_str = md_str.sub(mask_curly, src_str)
    tmp_str = tmp_str.format_map(value)
    
    md_str = re.compile('<@[a-z.=0-9 ]+@>', re.IGNORECASE)
    tmp_str = md_str.sub(unmask_curly, tmp_str)

    return tmp_str
