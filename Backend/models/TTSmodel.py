from TTS.api import TTS

# Load Hindi-specific TTS model
tts = TTS(model_name="tts_models/hi/cv/vits", progress_bar=True, gpu=False)








# import torch
# import inspect
# from TTS.api import TTS
# import TTS.tts.configs.xtts_config as xtts_config
# import TTS.config.shared_configs as shared_configs
# import TTS.tts.models.xtts as xtts_models


# def add_all_safe_globals_from_module(module):
#     classes = [member for _, member in inspect.getmembers(module, inspect.isclass)]
#     torch.serialization.add_safe_globals(classes)

# # Add known modules/classes:
# add_all_safe_globals_from_module(xtts_config)
# add_all_safe_globals_from_module(shared_configs)
# add_all_safe_globals_from_module(xtts_models)

# # Load TTS model (multi-speaker)
# tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True, gpu=False)