import os
import re
import time
from pathlib import Path

import requests
from requests import Timeout

from videotrans.configure import config
from videotrans.util import tools


def get_voice(*, text=None, role="2222", rate=None, volume="+0%", pitch="+0Hz", language=None, filename=None,
              set_p=True, inst=None,uuid=None):
    try:
        api_url = config.params['chattts_api'].strip().rstrip('/').lower()
        if len(config.params['chattts_api'].strip()) < 10:
            raise Exception(
                'ChatTTS API 接口不正确，请到设置中重新填写' if config.defaulelang == 'zh' else 'ChatTTS API interface is not correct, please go to Settings to fill in again')

        api_url = 'http://' + api_url.replace('http://', '').replace('/tts', '')
        config.logger.info(f'ChatTTS:api={api_url}')

        data = {"text": text.strip(), "voice": role, 'prompt': '', 'is_split': 1}
        res = requests.post(f"{api_url}/tts", data=data, proxies={"http": "", "https": ""}, timeout=3600)
        config.logger.info(f'chatTTS:{data=}')

        res = res.json()
        if res is None:
            raise Exception('ChatTTS端出错，请查看其控制台终端')
        if "code" not in res or res['code'] != 0:
            if "msg" in res:
                Path(filename).unlink(missing_ok=True)
                return True
            raise Exception(f'{res}')
        if api_url.find('127.0.0.1') > -1 or api_url.find('localhost') > -1:
            tools.wav2mp3(re.sub(r'\\{1,}', '/', res['filename']), filename)
        else:
            resb = requests.get(res['url'])
            if resb.status_code != 200:
                raise Exception(f'chatTTS:{res["url"]=}')
            config.logger.info(f'ChatTTS:resb={resb.status_code=}')
            with open(filename + ".wav", 'wb') as f:
                f.write(resb.content)
            time.sleep(1)
            tools.wav2mp3(filename + ".wav", filename)
            if os.path.exists(filename + ".wav"):
                os.unlink(filename + ".wav")
            if tools.vail_file(filename) and config.settings['remove_silence']:
                tools.remove_silence_from_end(filename)
            if set_p:
                if inst and inst.precent < 80:
                    inst.precent += 0.1
                tools.set_process(f'{config.transobj["kaishipeiyin"]} ', btnkey=inst.init['btnkey'] if inst else "",uuid=uuid)
    except ConnectionError or Timeout as e:
        raise Exception(f'无法连接到ChatTTS服务，请确保已部署并启动了ChatTTS-ui')
    except Exception as e:
        error = str(e)
        if set_p:
            tools.set_process(error, btnkey=inst.init['btnkey'] if inst else "",uuid=uuid)
        config.logger.error(f"ChatTTS合成失败:{error}")
        if inst and inst.init['btnkey']:
            config.errorlist[inst.init['btnkey']] = error
        raise
    else:
        return True
