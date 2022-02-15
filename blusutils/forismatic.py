"""nodoc"""
from typing import Union
import aiohttp, requests, rapidjson

class LangIsNotSupported(Exception):
	pass
async def async_quote(lang = 'en', *, as_dict = False) -> Union[str, dict]:
	if not isinstance(lang, str):
		raise TypeError(f'You must provide language as {str}, not as {type(lang)}')
	if lang not in ['en', 'ru']:
		raise LangIsNotSupported('This language not in supported (only english - en and russian - ru).')
	async with aiohttp.ClientSession(json_serializer = rapidjson) as requester:
		async with requester.get(url = f"http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang={lang}") as response:
			quote = await response.json()
			if as_dict: return quote
			author = '©'+quote["quoteAuthor"] if quote["quoteAuthor"] else ''
			return f'{quote["quoteText"]}{author}'
def quote(lang = 'en', *, as_dict = False) -> Union[str, dict]:
	if not isinstance(lang, str):
		raise TypeError(f'You must provide language as {str}, not as {type(lang)}')
	if lang not in ['en', 'ru']:
		raise LangIsNotSupported('This language not in supported (only english - en and russian - ru).')
	quote = rapidjson.loads(requests.post(url = f"http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang={lang}").text())
	if as_dict: return quote
	author = '©'+quote["quoteAuthor"] if quote["quoteAuthor"] else ''
	return f'{quote["quoteText"]}{author}'
