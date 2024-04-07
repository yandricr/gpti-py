import requests
import json

cred = {
    "x-nexra-user": None,
    "x-nexra-secret": None
}

def nexra(user, secret):
    cred["x-nexra-secret"] = secret
    cred["x-nexra-user"] = user


class gpt:
    error = None
    result = None
    def __init__(self, messages=[], prompt="", model="", markdown=False) -> None:
        try:
            headers = {
                "Content-Type": "application/json"
            }

            data = json.dumps({})
            try:
                data = json.dumps({
                    "messages": messages if messages is not None else [],
                    "prompt": prompt if prompt is not None else "",
                    "model": model if model is not None else "GPT-4",
                    "markdown": markdown if markdown is not None else False
                })
            except Exception as e:
                data = json.dumps({
                    "messages": [],
                    "prompt": "",
                    "model": "GPT-4",
                    "markdown": False
                })

            response = requests.post(url="https://nexra.aryahcr.cc/api/chat/gpt", headers=headers, data=data)
            if response.status_code == 200:
                err = None
                result = None

                count = -1
                for i in range(len(response.text)):
                    if count <= -1:
                        if response.text[i] == "{":
                            count = i
                    else:
                        break
                
                if count <= -1:
                    err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    result = None
                else:
                    try:
                        js = response.text[count:]
                        js = json.loads(js)
                        if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                            result = js
                            err = None
                        else:
                            err = js
                            result = None
                    except Exception as e:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None

                    if result == None and err != None:
                        self.error = err
                        self.result = None
                    else:
                        self.result = result
                        self.error = None
            else:
                data_err = {}
                try:
                    data_err = json.loads(response.text)
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                
                self.error = data_err
                self.result = None
        except Exception as e:
            self.error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.result = None
        pass
    def error(self):
        return self.error
    def result(self):
        return self.result

class gptweb:
    error = None
    result = None
    def __init__(self, prompt="", markdown=False) -> None:
        try:
            headers = {
                "Content-Type": "application/json"
            }

            data = json.dumps({})
            try:
                data = json.dumps({
                    "prompt": prompt if prompt is not None else "",
                    "markdown": markdown if markdown is not None else False
                })
            except Exception as e:
                data = json.dumps({
                    "prompt": "",
                    "markdown": False
                })

            response = requests.post(url="https://nexra.aryahcr.cc/api/chat/gptweb", headers=headers, data=data)
            if response.status_code == 200:
                err = None
                result = None

                count = -1
                for i in range(len(response.text)):
                    if count <= -1:
                        if response.text[i] == "{":
                            count = i
                    else:
                        break
                
                if count <= -1:
                    err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    result = None
                else:
                    try:
                        js = response.text[count:]
                        js = json.loads(js)
                        if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                            result = js
                            err = None
                        else:
                            err = js
                            result = None
                    except Exception as e:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None

                    if result == None and err != None:
                        self.error = err
                        self.result = None
                    else:
                        self.result = result
                        self.error = None
            else:
                data_err = {}
                try:
                    data_err = json.loads(response.text)
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                
                self.error = data_err
                self.result = None
        except Exception as e:
            self.error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.result = None
        pass
    def error(self):
        return self.error
    def result(self):
        return self.result

class dalle:
    class v1:
        error = None
        result = None
        def __init__(self, prompt="") -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                err = False
                
                data = json.dumps({
                    "prompt": "",
                    "model": "dalle"
                })

                try:
                    data = json.dumps({
                        "prompt": prompt if prompt is not None else "",
                        "model": "dalle"
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "dalle"
                    })
                
                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result
    class v2:
        error = None
        result = None
        def __init__(self, prompt="", data={
            "prompt_negative": "",
            "width": "",
            "height": "",
            "guidance_scale": ""
        }) -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                headers.update(cred)
                err = False
                
                md = {
                    "prompt_negative": "",
                    "width": 1024,
                    "height": 1024,
                    "guidance_scale": 6
                }

                try:
                    prompt = prompt if prompt is not None else ""
                except Exception as e:
                    prompt = ""

                try :
                    if data.get("prompt_negative") != None:
                        md["prompt_negative"] = data.get("prompt_negative")
                    else:
                        md["prompt_negative"] = ""

                    if data.get("width") != None:
                        md["width"] = data.get("width")
                    else:
                        md["width"] = 1024

                    if data.get("height") != None:
                        md["height"] = data.get("height")
                    else:
                        md["height"] = 1024

                    if data.get("guidance_scale") != None:
                        md["guidance_scale"] = data.get("guidance_scale")
                    else:
                        md["guidance_scale"] = 6
                except Exception as e:
                    md = {
                        "prompt_negative": "",
                        "width": 1024,
                        "height": 1024,
                        "guidance_scale": 6
                    }

                data = {}
                try:
                    data = json.dumps({
                        "prompt": prompt,
                        "model": "dalle2",
                        "data": md
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "dalle2",
                        "data": {
                            "prompt_negative": "",
                            "width": 1024,
                            "height": 1024,
                            "guidance_scale": 6
                        }
                    })
                
                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result
    class mini():
        error = None
        result = None
        def __init__(self, prompt="") -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                err = False
                
                data = json.dumps({})
                try:
                    data = json.dumps({
                        "prompt": prompt if prompt is not None else "",
                        "model": "dalle-mini"
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "dalle-mini"
                    })

                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result
        
class prodia():
    class v1():
        error = None
        result = None
        def __init__(self, prompt="", data={
            "model": "",
            "steps": "",
            "cfg_scale": "",
            "sampler": "",
            "negative_prompt": ""
        }) -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }

                try:
                    prompt = prompt if prompt is not None else ""
                except Exception as e:
                    prompt = ""

                md = {
                    "model": "absolutereality_V16.safetensors [37db0fc3]",
                    "steps": 25,
                    "cfg_scale": 7,
                    "sampler": "DPM++ 2M Karras",
                    "negative_prompt": ""
                }

                try :
                    if data.get("model") != None:
                        md["model"] = data.get("model")
                    else:
                        md["model"] = "absolutereality_V16.safetensors [37db0fc3]"

                    if data.get("steps") != None:
                        md["steps"] = data.get("steps")
                    else:
                        md["steps"] = 25

                    if data.get("cfg_scale") != None:
                        md["cfg_scale"] = data.get("cfg_scale")
                    else:
                        md["cfg_scale"] = 7

                    if data.get("sampler") != None:
                        md["sampler"] = data.get("sampler")
                    else:
                        md["sampler"] = "DPM++ 2M Karras"
                    
                    if data.get("negative_prompt") != None:
                        md["negative_prompt"] = data.get("negative_prompt")
                    else:
                        md["negative_prompt"] = ""
                except Exception as e:
                    md = {
                        "model": "absolutereality_V16.safetensors [37db0fc3]",
                        "steps": 25,
                        "cfg_scale": 7,
                        "sampler": "DPM++ 2M Karras",
                        "negative_prompt": ""
                    }

                data = {}
                try:
                    data = json.dumps({
                        "prompt": prompt,
                        "model": "prodia",
                        "data": md
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "prodia",
                        "data": {
                            "model": "absolutereality_V16.safetensors [37db0fc3]",
                            "steps": 25,
                            "cfg_scale": 7,
                            "sampler": "DPM++ 2M Karras",
                            "negative_prompt": ""
                        }
                    })

                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result
    class stablediffusion():
        error = None
        result = None
        def __init__(self, prompt="", data={
            "prompt_negative": "",
            "model": "",
            "sampling_method": "",
            "sampling_steps": "",
            "width": "",
            "height": "",
            "cfg_scale": ""
        }) -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }

                try:
                    prompt = prompt if prompt is not None else ""
                except Exception as e:
                    prompt = ""

                md = {
                    "prompt_negative": "",
                    "model": "absolutereality_v181.safetensors [3d9d4d2b]",
                    "sampling_method": "DPM++ 2M Karras",
                    "sampling_steps": 25,
                    "width": 512,
                    "height": 512,
                    "cfg_scale": 7
                }

                try :
                    if data.get("model") != None:
                        md["model"] = data.get("model")
                    else:
                        md["model"] = "absolutereality_v181.safetensors [3d9d4d2b]"

                    if data.get("sampling_steps") != None:
                        md["sampling_steps"] = data.get("sampling_steps")
                    else:
                        md["sampling_steps"] = 25

                    if data.get("cfg_scale") != None:
                        md["cfg_scale"] = data.get("cfg_scale")
                    else:
                        md["cfg_scale"] = 7

                    if data.get("sampling_method") != None:
                        md["sampling_method"] = data.get("sampling_method")
                    else:
                        md["sampling_method"] = "DPM++ 2M Karras"
                    
                    if data.get("prompt_negative") != None:
                        md["prompt_negative"] = data.get("prompt_negative")
                    else:
                        md["prompt_negative"] = ""

                    if data.get("width") != None:
                        md["width"] = data.get("width")
                    else:
                        md["width"] = ""
                    
                    if data.get("height") != None:
                        md["height"] = data.get("height")
                    else:
                        md["height"] = ""
                except Exception as e:
                    md = {
                        "prompt_negative": "",
                        "model": "absolutereality_v181.safetensors [3d9d4d2b]",
                        "sampling_method": "DPM++ 2M Karras",
                        "sampling_steps": 25,
                        "width": 512,
                        "height": 512,
                        "cfg_scale": 7
                    }

                data = {}
                try:
                    data = json.dumps({
                        "prompt": prompt,
                        "model": "prodia-stablediffusion",
                        "data": md
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "prodia-stablediffusion",
                        "data": {
                            "prompt_negative": "",
                            "model": "absolutereality_v181.safetensors [3d9d4d2b]",
                            "sampling_method": "DPM++ 2M Karras",
                            "sampling_steps": 25,
                            "width": 512,
                            "height": 512,
                            "cfg_scale": 7
                        }
                    })

                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result
    class stablediffusion_xl():
        error = None
        result = None
        def __init__(self, prompt="", data={
            "prompt_negative": "",
            "model": "",
            "sampling_method": "",
            "sampling_steps": "",
            "width": "",
            "height": "",
            "cfg_scale": ""
        }) -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                headers.update(cred)

                try:
                    prompt = prompt if prompt is not None else ""
                except Exception as e:
                    prompt = ""

                md = {
                    "prompt_negative": "",
                    "model": "absolutereality_v181.safetensors [3d9d4d2b]",
                    "sampling_method": "DPM++ 2M Karras",
                    "sampling_steps": 25,
                    "width": 1024,
                    "height": 1024,
                    "cfg_scale": 7
                }

                try :
                    if data.get("model") != None:
                        md["model"] = data.get("model")
                    else:
                        md["model"] = "absolutereality_v181.safetensors [3d9d4d2b]"

                    if data.get("sampling_steps") != None:
                        md["sampling_steps"] = data.get("sampling_steps")
                    else:
                        md["sampling_steps"] = 25

                    if data.get("cfg_scale") != None:
                        md["cfg_scale"] = data.get("cfg_scale")
                    else:
                        md["cfg_scale"] = 7

                    if data.get("sampling_method") != None:
                        md["sampling_method"] = data.get("sampling_method")
                    else:
                        md["sampling_method"] = "DPM++ 2M Karras"
                    
                    if data.get("prompt_negative") != None:
                        md["prompt_negative"] = data.get("prompt_negative")
                    else:
                        md["prompt_negative"] = ""

                    if data.get("width") != None:
                        md["width"] = data.get("width")
                    else:
                        md["width"] = ""
                    
                    if data.get("height") != None:
                        md["height"] = data.get("height")
                    else:
                        md["height"] = ""
                except Exception as e:
                    md = {
                        "prompt_negative": "",
                        "model": "absolutereality_v181.safetensors [3d9d4d2b]",
                        "sampling_method": "DPM++ 2M Karras",
                        "sampling_steps": 25,
                        "width": 1024,
                        "height": 1024,
                        "cfg_scale": 7
                    }

                data = {}
                try:
                    data = json.dumps({
                        "prompt": prompt,
                        "model": "prodia-stablediffusion-xl",
                        "data": md
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "prodia-stablediffusion-xl",
                        "data": {
                            "prompt_negative": "",
                            "model": "absolutereality_v181.safetensors [3d9d4d2b]",
                            "sampling_method": "DPM++ 2M Karras",
                            "sampling_steps": 25,
                            "width": 1024,
                            "height": 1024,
                            "cfg_scale": 7
                        }
                    })

                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result

class pixart():
    class a():
        error = None
        result = None
        def __init__(self, prompt="", data={
            "prompt_negative": "",
            "sampler": "",
            "image_style": "",
            "width": "",
            "height": "",
            "dpm_guidance_scale": "",
            "dpm_inference_steps": "",
            "sa_guidance_scale": "",
            "sa_inference_steps": ""
        }) -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                headers.update(cred)

                try:
                    prompt = prompt if prompt is not None else ""
                except Exception as e:
                    prompt = ""

                md = {
                    "prompt_negative": "",
                    "sampler": "DPM-Solver",
                    "image_style": "(No style)",
                    "width": 1024,
                    "height": 1024,
                    "dpm_guidance_scale": 4.5,
                    "dpm_inference_steps": 14,
                    "sa_guidance_scale": 3,
                    "sa_inference_steps": 25
                }

                try :
                    if data.get("sampler") != None:
                        md["sampler"] = data.get("sampler")
                    else:
                        md["sampler"] = "DPM-Solver"

                    if data.get("height") != None:
                        md["height"] = data.get("height")
                    else:
                        md["height"] = 1024

                    if data.get("width") != None:
                        md["width"] = data.get("width")
                    else:
                        md["width"] = 1024

                    if data.get("image_style") != None:
                        md["image_style"] = data.get("image_style")
                    else:
                        md["image_style"] = "(No style)"
                    
                    if data.get("prompt_negative") != None:
                        md["prompt_negative"] = data.get("prompt_negative")
                    else:
                        md["prompt_negative"] = ""
                    
                    if data.get("dpm_guidance_scale") != None:
                        md["dpm_guidance_scale"] = data.get("dpm_guidance_scale")
                    else:
                        md["dpm_guidance_scale"] = 4.5

                    if data.get("dpm_inference_steps") != None:
                        md["dpm_inference_steps"] = data.get("dpm_inference_steps")
                    else:
                        md["dpm_inference_steps"] = 14
                        
                    if data.get("sa_guidance_scale") != None:
                        md["sa_guidance_scale"] = data.get("sa_guidance_scale")
                    else:
                        md["sa_guidance_scale"] = 14
                
                    if data.get("sa_inference_steps") != None:
                        md["sa_inference_steps"] = data.get("sa_inference_steps")
                    else:
                        md["sa_inference_steps"] = 14
                except Exception as e:
                    md = {
                        "prompt_negative": "",
                        "sampler": "DPM-Solver",
                        "image_style": "(No style)",
                        "width": 1024,
                        "height": 1024,
                        "dpm_guidance_scale": 4.5,
                        "dpm_inference_steps": 14,
                        "sa_guidance_scale": 3,
                        "sa_inference_steps": 25
                    }

                data = {}
                try:
                    data = json.dumps({
                        "prompt": prompt,
                        "model": "pixart-a",
                        "data": md
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "pixart-a",
                        "data": {
                            "prompt_negative": "",
                            "sampler": "DPM-Solver",
                            "image_style": "(No style)",
                            "width": 1024,
                            "height": 1024,
                            "dpm_guidance_scale": 4.5,
                            "dpm_inference_steps": 14,
                            "sa_guidance_scale": 3,
                            "sa_inference_steps": 25
                        }
                    })
                
                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result
    class lcm():
        error = None
        result = None
        def __init__(self, prompt="", data={
            "prompt_negative": "",
            "image_style": "",
            "width": "",
            "height": "",
            "lcm_inference_steps": ""
        }) -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                headers.update(cred)

                try:
                    prompt = prompt if prompt is not None else ""
                except Exception as e:
                    prompt = ""

                md = {
                    "prompt_negative": "",
                    "image_style": "(No style)",
                    "width": 1024,
                    "height": 1024,
                    "lcm_inference_steps": 9
                }

                try :
                    if data.get("lcm_inference_steps") != None:
                        md["lcm_inference_steps"] = data.get("lcm_inference_steps")
                    else:
                        md["lcm_inference_steps"] = 9

                    if data.get("height") != None:
                        md["height"] = data.get("height")
                    else:
                        md["height"] = 1024

                    if data.get("width") != None:
                        md["width"] = data.get("width")
                    else:
                        md["width"] = 1024

                    if data.get("image_style") != None:
                        md["image_style"] = data.get("image_style")
                    else:
                        md["image_style"] = "(No style)"
                    
                    if data.get("prompt_negative") != None:
                        md["prompt_negative"] = data.get("prompt_negative")
                    else:
                        md["prompt_negative"] = ""
                except Exception as e:
                    md = {
                        "prompt_negative": "",
                        "image_style": "(No style)",
                        "width": 1024,
                        "height": 1024,
                        "lcm_inference_steps": 9
                    }

                data = {}
                try:
                    data = json.dumps({
                        "prompt": prompt,
                        "model": "pixart-lcm",
                        "data": md
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "pixart-lcm",
                        "data": {
                            "prompt_negative": "",
                            "image_style": "(No style)",
                            "width": 1024,
                            "height": 1024,
                            "lcm_inference_steps": 9
                        }
                    })
                
                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result

class stablediffusion():
    class v1():
        error = None
        result = None
        def __init__(self, prompt="") -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                err = False
                
                data = json.dumps({})
                try:
                    data = json.dumps({
                        "prompt": prompt if prompt is not None else "",
                        "model": "stablediffusion-1.5"
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "stablediffusion-1.5"
                    })
                
                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result
    class v2():
        error = None
        result = None
        def __init__(self, prompt="", data={
            "prompt_negative": "",
            "guidance_scale": ""
        }) -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }

                try:
                    prompt = prompt if prompt is not None else ""
                except Exception as e:
                    prompt = ""

                md = {
                    "prompt_negative": "",
                    "guidance_scale": 9
                }

                try :
                    if data.get("prompt_negative") != None:
                        md["prompt_negative"] = data.get("prompt_negative")
                    else:
                        md["prompt_negative"] = "absolutereality_V16.safetensors [37db0fc3]"

                    if data.get("guidance_scale") != None:
                        md["guidance_scale"] = data.get("guidance_scale")
                    else:
                        md["guidance_scale"] = 9
                except Exception as e:
                    md = {
                        "prompt_negative": "",
                        "guidance_scale": 9
                    }

                data = {}
                try:
                    data = json.dumps({
                        "prompt": prompt,
                        "model": "stablediffusion-2.1",
                        "data": md
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "stablediffusion-2.1",
                        "data": {
                            "prompt_negative": "",
                            "guidance_scale": 9
                        }
                    })

                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result
    class xl():
        error = None
        result = None
        def __init__(self, prompt="", data={
            "prompt_negative": "",
            "image_style": "",
            "guidance_scale": ""
        }) -> None:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                headers.update(cred)

                try:
                    prompt = prompt if prompt is not None else ""
                except Exception as e:
                    prompt = ""

                md = {
                    "prompt_negative": "",
                    "image_style": "(No style)",
                    "guidance_scale": 7.5
                }

                try :
                    if data.get("prompt_negative") != None:
                        md["prompt_negative"] = data.get("prompt_negative")
                    else:
                        md["prompt_negative"] = "absolutereality_V16.safetensors [37db0fc3]"

                    if data.get("guidance_scale") != None:
                        md["guidance_scale"] = data.get("guidance_scale")
                    else:
                        md["guidance_scale"] = 7.5

                    if data.get("image_style") != None:
                        md["image_style"] = data.get("image_style")
                    else:
                        md["image_style"] = "(No style)"
                except Exception as e:
                    md = {
                        "prompt_negative": "",
                        "image_style": "(No style)",
                        "guidance_scale": 7.5
                    }

                data = {}
                try:
                    data = json.dumps({
                        "prompt": prompt,
                        "model": "stablediffusion-xl",
                        "data": md
                    })
                except Exception as e:
                    data = json.dumps({
                        "prompt": "",
                        "model": "stablediffusion-xl",
                        "data": {
                            "prompt_negative": "",
                            "image_style": "(No style)",
                            "guidance_scale": 7.5
                        }
                    })

                response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
                if response.status_code == 200:
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    data_err = {}
                    try:
                        data_err = json.loads(response.text)
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                    
                    self.error = data_err
                    self.result = None
            except Exception as e:
                self.error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.result = None
            pass
        def error(self):
            return self.error
        def result(self):
            return self.result

class emi():
    error = None
    result = None
    def __init__(self, prompt="") -> None:
        try:
            headers = {
                "Content-Type": "application/json"
            }
            err = False
            
            data = json.dumps({})
            try:
                data = json.dumps({
                    "prompt": prompt if prompt is not None else "",
                    "model": "emi"
                })
            except Exception as e:
                data = json.dumps({
                    "prompt": "",
                    "model": "emi"
                })
            
            response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
            if response.status_code == 200:
                err = None
                result = None

                count = -1
                for i in range(len(response.text)):
                    if count <= -1:
                        if response.text[i] == "{":
                            count = i
                    else:
                        break
                
                if count <= -1:
                    err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    result = None
                else:
                    try:
                        js = response.text[count:]
                        js = json.loads(js)
                        if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                            result = js
                            err = None
                        else:
                            err = js
                            result = None
                    except Exception as e:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None

                    if result == None and err != None:
                        self.error = err
                        self.result = None
                    else:
                        self.result = result
                        self.error = None
            else:
                data_err = {}
                try:
                    data_err = json.loads(response.text)
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                
                self.error = data_err
                self.result = None
        except Exception as e:
            self.error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.result = None
        pass
    def error(self):
        return self.error
    def result(self):
        return self.result

class bing():
    error = None
    result = None
    def __init__(self, messages=[], conversation_style="", markdown=False, stream=False) -> None:
        try:
            headers = {
                "Content-Type": "application/json"
            }

            data = json.dumps({})

            strm = False
            try:
                if stream != None and stream == True:
                    strm = True
                else:
                    strm = False
            except Exception as e:
                strm = False
            
            try:
                data = json.dumps({
                    "messages": messages if messages is not None else [],
                    "conversation_style": conversation_style if conversation_style is not None else "Balanced",
                    "markdown": markdown if markdown is not None else False,
                    "stream": strm if strm is not None else False,
                    "model": "Bing"
                })
            except Exception as e:
                data = json.dumps({
                    "messages": [],
                    "conversation_style": "Balanced",
                    "model": "Bing",
                    "markdown": False,
                    "stream": False
                })

            response = requests.post(url="https://nexra.aryahcr.cc/api/chat/complements", headers=headers, data=data, stream=strm)
            if response.status_code == 200:
                if strm != True:
                    self.bingdata = None
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    self.error = None
                    self.result = None
                    self.bingdata = response
            else:
                data_err = {}
                try:
                    data_err = json.loads(response.text)
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                
                self.bingdata = None
                self.error = data_err
                self.result = None
        except Exception as e:
            self.error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.bingdata = None
            self.result = None
        pass
    def stream(self):
        if self.bingdata != None:
            try:
                tmp = None
                err = None
                for chunk in self.bingdata.iter_content(chunk_size=1024):
                    if err == None:
                        if chunk:
                            chk = chunk.decode()
                            chk = chk.split("")

                            for data in chk:
                                result = None

                                try:
                                    convert = json.loads(data)
                                    result = data
                                    tmp = None
                                except Exception as e:
                                    if tmp == None:
                                        tmp = data
                                    else:
                                        try:
                                            convert = json.loads(tmp)
                                            result = tmp
                                            tmp = None
                                        except Exception as e:
                                            tmp = tmp + data
                                            try:
                                                convert = json.loads(tmp)
                                                result = tmp
                                                tmp = None
                                            except Exception as e:
                                                tmp = tmp
                                
                                if result != None:
                                    if "code" not in result and "status" not in result:
                                        yield json.loads(result)
                                    else:
                                        err = result
                                        yield json.loads(err)
            except Exception as e:
                yield {"message":None,"original":None,"finish":True,"error":True}
        else:
            yield {"message":None,"original":None,"finish":True,"error":True}
        pass
    def error(self):
        return self.error
    def result(self):
        return self.result

class llama2():
    error = None
    result = None
    def __init__(self, messages=[], data={
        "system_message": "",
        "temperature": "",
        "max_tokens": "",
        "top_p": "",
        "repetition_penalty": "",
    }, markdown=False, stream=False) -> None:
        try:
            headers = {
                "Content-Type": "application/json"
            }

            data = json.dumps({})

            strm = False
            try:
                if stream != None and stream == True:
                    strm = True
                else:
                    strm = False
            except Exception as e:
                strm = False

            md = {
                "system_message": "",
                "temperature": 0.9,
                "max_tokens": 4096,
                "top_p": 0.6,
                "repetition_penalty": 1.2,
            }

            try:
                prompt = prompt if prompt is not None else ""
            except Exception as e:
                prompt = ""

            try :
                if data.get("system_message") != None:
                    md["system_message"] = data.get("system_message")
                else:
                    md["system_message"] = ""

                if data.get("temperature") != None:
                    md["temperature"] = data.get("temperature")
                else:
                    md["temperature"] = 0.9
                
                if data.get("max_tokens") != None:
                    md["max_tokens"] = data.get("max_tokens")
                else:
                    md["max_tokens"] = 4096
                
                if data.get("top_p") != None:
                    md["top_p"] = data.get("top_p")
                else:
                    md["top_p"] = 0.6
                
                if data.get("repetition_penalty") != None:
                    md["repetition_penalty"] = data.get("repetition_penalty")
                else:
                    md["repetition_penalty"] = 1.2
            except Exception as e:
                md = {
                    "system_message": "",
                    "temperature": 0.9,
                    "max_tokens": 4096,
                    "top_p": 0.6,
                    "repetition_penalty": 1.2,
                }

            data = {}
            try:
                data = json.dumps({
                    "messages": messages if messages is not None else [],
                    "markdown": markdown if markdown is not None else False,
                    "stream": strm if strm is not None else False,
                    "model": "llama2",
                    "data": md
                })
            except Exception as e:
                data = json.dumps({
                    "messages": [],
                    "markdown": False,
                    "stream": False,
                    "model": "llama2",
                    "data": {
                        "gpu": False,
                        "prompt_improvement": False
                    }
                })

            response = requests.post(url="https://nexra.aryahcr.cc/api/chat/complements", headers=headers, data=data, stream=strm)
            if response.status_code == 200:
                if strm != True:
                    self.bingdata = None
                    err = None
                    result = None

                    count = -1
                    for i in range(len(response.text)):
                        if count <= -1:
                            if response.text[i] == "{":
                                count = i
                        else:
                            break
                    
                    if count <= -1:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None
                    else:
                        try:
                            js = response.text[count:]
                            js = json.loads(js)
                            if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                                result = js
                                err = None
                            else:
                                err = js
                                result = None
                        except Exception as e:
                            err = {
                                "code": 500,
                                "status": False,
                                "error": "INTERNAL_SERVER_ERROR",
                                "message": "general (unknown) error"
                            }
                            result = None

                        if result == None and err != None:
                            self.error = err
                            self.result = None
                        else:
                            self.result = result
                            self.error = None
                else:
                    self.error = None
                    self.result = None
                    self.bingdata = response
            else:
                data_err = {}
                try:
                    data_err = json.loads(response.text)
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                
                self.bingdata = None
                self.error = data_err
                self.result = None
        except Exception as e:
            self.error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.bingdata = None
            self.result = None
        pass
    def stream(self):
        if self.bingdata != None:
            try:
                tmp = None
                err = None
                for chunk in self.bingdata.iter_content(chunk_size=1024):
                    if err == None:
                        if chunk:
                            chk = chunk.decode()
                            chk = chk.split("")

                            for data in chk:
                                result = None

                                try:
                                    convert = json.loads(data)
                                    result = data
                                    tmp = None
                                except Exception as e:
                                    if tmp == None:
                                        tmp = data
                                    else:
                                        try:
                                            convert = json.loads(tmp)
                                            result = tmp
                                            tmp = None
                                        except Exception as e:
                                            tmp = tmp + data
                                            try:
                                                convert = json.loads(tmp)
                                                result = tmp
                                                tmp = None
                                            except Exception as e:
                                                tmp = tmp
                                
                                if result != None:
                                    if "code" not in result and "status" not in result:
                                        yield json.loads(result)
                                    else:
                                        err = result
                                        yield json.loads(err)
            except Exception as e:
                yield {"message":None,"original":None,"finish":True,"error":True}
        else:
            yield {"message":None,"original":None,"finish":True,"error":True}
        pass
    def error(self):
        return self.error
    def result(self):
        return self.result
    
class render3d():
    error = None
    result = None
    def __init__(self, prompt="", data={
        "prompt_negative": ""
    }) -> None:
        try:
            headers = {
                "Content-Type": "application/json"
            }
            headers.update(cred)

            try:
                prompt = prompt if prompt is not None else ""
            except Exception as e:
                prompt = ""

            md = {
                "prompt_negative": ""
            }

            try :
                if data.get("prompt_negative") != None:
                    md["prompt_negative"] = data.get("prompt_negative")
                else:
                    md["prompt_negative"] = ""
            except Exception as e:
                md = {
                    "prompt_negative": ""
                }

            data = {}
            try:
                data = json.dumps({
                    "prompt": prompt,
                    "model": "render3d",
                    "data": md
                })
            except Exception as e:
                data = json.dumps({
                    "prompt": "",
                    "model": "render3d",
                    "data": {
                        "prompt_negative": ""
                    }
                })
            
            response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
            if response.status_code == 200:
                err = None
                result = None

                count = -1
                for i in range(len(response.text)):
                    if count <= -1:
                        if response.text[i] == "{":
                            count = i
                    else:
                        break
                
                if count <= -1:
                    err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    result = None
                else:
                    try:
                        js = response.text[count:]
                        js = json.loads(js)
                        if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                            result = js
                            err = None
                        else:
                            err = js
                            result = None
                    except Exception as e:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None

                    if result == None and err != None:
                        self.error = err
                        self.result = None
                    else:
                        self.result = result
                        self.error = None
            else:
                data_err = {}
                try:
                    data_err = json.loads(response.text)
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                
                self.error = data_err
                self.result = None
        except Exception as e:
            self.error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.result = None
        pass
    def error(self):
        return self.error
    def result(self):
        return self.result

class animagine():
    error = None
    result = None
    def __init__(self, prompt="", data={
        "prompt_negative": "",
        "width": "",
        "height": "",
        "guidance_scale": "",
        "quality_tags": "",
        "style_present": "",
        "strength": "",
        "upscale": "",
        "sampler": "",
        "inference_steps": "",
    }) -> None:
        try:
            headers = {
                "Content-Type": "application/json"
            }
            headers.update(cred)

            try:
                prompt = prompt if prompt is not None else ""
            except Exception as e:
                prompt = ""

            md = {
                "prompt_negative": "",
                "width": 1024,
                "height": 1024,
                "guidance_scale": 7,
                "quality_tags": "Standard",
                "style_present": "(None)",
                "strength": 0.5,
                "upscale": 1.5,
                "sampler": "Euler a",
                "inference_steps": 28,
            }

            try :
                if data.get("prompt_negative") != None:
                    md["prompt_negative"] = data.get("prompt_negative")
                else:
                    md["prompt_negative"] = ""
                
                if data.get("width") != None:
                    md["width"] = data.get("width")
                else:
                    md["width"] = 1024
                
                if data.get("height") != None:
                    md["height"] = data.get("height")
                else:
                    md["height"] = 1024
                
                if data.get("guidance_scale") != None:
                    md["guidance_scale"] = data.get("guidance_scale")
                else:
                    md["guidance_scale"] = 7
                
                if data.get("quality_tags") != None:
                    md["quality_tags"] = data.get("quality_tags")
                else:
                    md["quality_tags"] = "Standard"
                
                if data.get("style_present") != None:
                    md["style_present"] = data.get("style_present")
                else:
                    md["style_present"] = "(None)"
                
                if data.get("strength") != None:
                    md["strength"] = data.get("strength")
                else:
                    md["strength"] = 0.5
                
                if data.get("upscale") != None:
                    md["upscale"] = data.get("upscale")
                else:
                    md["upscale"] = 1.5
                
                if data.get("sampler") != None:
                    md["sampler"] = data.get("sampler")
                else:
                    md["sampler"] = "Euler a"
                
                if data.get("inference_steps") != None:
                    md["inference_steps"] = data.get("inference_steps")
                else:
                    md["inference_steps"] = 28
            except Exception as e:
                md = {
                    "prompt_negative": "",
                    "width": 1024,
                    "height": 1024,
                    "guidance_scale": 7,
                    "quality_tags": "Standard",
                    "style_present": "(None)",
                    "strength": 0.5,
                    "upscale": 1.5,
                    "sampler": "Euler a",
                    "inference_steps": 28,
                }

            data = {}
            try:
                data = json.dumps({
                    "prompt": prompt,
                    "model": "animagine-xl",
                    "data": md
                })
            except Exception as e:
                data = json.dumps({
                    "prompt": "",
                    "model": "animagine-xl",
                    "data": {
                        "prompt_negative": "",
                        "width": 1024,
                        "height": 1024,
                        "guidance_scale": 7,
                        "quality_tags": "Standard",
                        "style_present": "(None)",
                        "strength": 0.5,
                        "upscale": 1.5,
                        "sampler": "Euler a",
                        "inference_steps": 28,
                    }
                })
            
            response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
            if response.status_code == 200:
                err = None
                result = None

                count = -1
                for i in range(len(response.text)):
                    if count <= -1:
                        if response.text[i] == "{":
                            count = i
                    else:
                        break
                
                if count <= -1:
                    err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    result = None
                else:
                    try:
                        js = response.text[count:]
                        js = json.loads(js)
                        if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                            result = js
                            err = None
                        else:
                            err = js
                            result = None
                    except Exception as e:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None

                    if result == None and err != None:
                        self.error = err
                        self.result = None
                    else:
                        self.result = result
                        self.error = None
            else:
                data_err = {}
                try:
                    data_err = json.loads(response.text)
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                
                self.error = data_err
                self.result = None
        except Exception as e:
            self.error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.result = None
        pass
    def error(self):
        return self.error
    def result(self):
        return self.result

class playground():
    error = None
    result = None
    def __init__(self, prompt="", data={
        "prompt_negative": "",
        "width": "",
        "height": "",
        "guidance_scale": ""
    }) -> None:
        try:
            headers = {
                "Content-Type": "application/json"
            }
            headers.update(cred)

            try:
                prompt = prompt if prompt is not None else ""
            except Exception as e:
                prompt = ""

            md = {
                "prompt_negative": "",
                "width": 1024,
                "height": 1024,
                "guidance_scale": 3
            }

            try :
                if data.get("prompt_negative") != None:
                    md["prompt_negative"] = data.get("prompt_negative")
                else:
                    md["prompt_negative"] = ""
                
                if data.get("width") != None:
                    md["width"] = data.get("width")
                else:
                    md["width"] = 1024
                
                if data.get("height") != None:
                    md["height"] = data.get("height")
                else:
                    md["height"] = 1024
                
                if data.get("guidance_scale") != None:
                    md["guidance_scale"] = data.get("guidance_scale")
                else:
                    md["guidance_scale"] = 3
            except Exception as e:
                md = {
                    "prompt_negative": "",
                    "width": 1024,
                    "height": 1024,
                    "guidance_scale": 3
                }

            data = {}
            try:
                data = json.dumps({
                    "prompt": prompt,
                    "model": "playground",
                    "data": md
                })
            except Exception as e:
                data = json.dumps({
                    "prompt": "",
                    "model": "playground",
                    "data": {
                        "prompt_negative": "",
                        "width": 1024,
                        "height": 1024,
                        "guidance_scale": 3
                    }
                })
            
            response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
            if response.status_code == 200:
                err = None
                result = None

                count = -1
                for i in range(len(response.text)):
                    if count <= -1:
                        if response.text[i] == "{":
                            count = i
                    else:
                        break
                
                if count <= -1:
                    err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    result = None
                else:
                    try:
                        js = response.text[count:]
                        js = json.loads(js)
                        if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                            result = js
                            err = None
                        else:
                            err = js
                            result = None
                    except Exception as e:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None

                    if result == None and err != None:
                        self.error = err
                        self.result = None
                    else:
                        self.result = result
                        self.error = None
            else:
                data_err = {}
                try:
                    data_err = json.loads(response.text)
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                
                self.error = data_err
                self.result = None
        except Exception as e:
            self.error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.result = None
        pass
    def error(self):
        return self.error
    def result(self):
        return self.result

class pixelart():
    error = None
    result = None
    def __init__(self, prompt="", data={
        "prompt_negative": ""
    }) -> None:
        try:
            headers = {
                "Content-Type": "application/json"
            }
            headers.update(cred)

            try:
                prompt = prompt if prompt is not None else ""
            except Exception as e:
                prompt = ""

            md = {
                "prompt_negative": ""
            }

            try :
                if data.get("prompt_negative") != None:
                    md["prompt_negative"] = data.get("prompt_negative")
                else:
                    md["prompt_negative"] = ""
            except Exception as e:
                md = {
                    "prompt_negative": ""
                }

            data = {}
            try:
                data = json.dumps({
                    "prompt": prompt,
                    "model": "pixel-art",
                    "data": md
                })
            except Exception as e:
                data = json.dumps({
                    "prompt": "",
                    "model": "pixel-art",
                    "data": {
                        "prompt_negative": ""
                    }
                })
            
            response = requests.post(url="https://nexra.aryahcr.cc/api/image/complements", headers=headers, data=data)
            if response.status_code == 200:
                err = None
                result = None

                count = -1
                for i in range(len(response.text)):
                    if count <= -1:
                        if response.text[i] == "{":
                            count = i
                    else:
                        break
                
                if count <= -1:
                    err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    result = None
                else:
                    try:
                        js = response.text[count:]
                        js = json.loads(js)
                        if js != None and js["code"] != None and js["code"] == 200 and js["status"] != None and js["status"] == True:
                            result = js
                            err = None
                        else:
                            err = js
                            result = None
                    except Exception as e:
                        err = {
                            "code": 500,
                            "status": False,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }
                        result = None

                    if result == None and err != None:
                        self.error = err
                        self.result = None
                    else:
                        self.result = result
                        self.error = None
            else:
                data_err = {}
                try:
                    data_err = json.loads(response.text)
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                
                self.error = data_err
                self.result = None
        except Exception as e:
            self.error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.result = None
        pass
    def error(self):
        return self.error
    def result(self):
        return self.result