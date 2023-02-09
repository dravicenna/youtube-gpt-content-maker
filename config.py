
# MODEL SETTINGS
MODEL = "text-davinci-003"
API_PARAM = {
    'engine': MODEL,
    'max_tokens': 512,
    'temperature': 0.77,
    'top_p': 1,
    'frequency_penalty': 0.28,
    'presence_penalty': 0.13,
}
# VIDEO SETTINGS
CHANNEL_NAME = 'historyfactstv'
DURATION = 8
SIZE = (1080, 1920)
FPS = 30
# FOLDERS
VIDEO = 'video'
MUSIC = 'music'

VID_TO_GENRATE = 12  # How many videos generate for each request
PROMPT_TEMPLATE = f'Generate {str(VID_TO_GENRATE)} unique and memorable facts about the specified request. Use irony, puns, and word play to create entertaining and easily understandable facts. No references or sources required. Output format will be: ["fact1",\n"fact2",/n...,/n"fact{str(VID_TO_GENRATE)}"]. My first request is '  # noqa
